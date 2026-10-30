import logging
import os

from flask import Flask, jsonify, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

from app.database import create_operation, database_is_ready, list_operations
from app.logging_config import configure_logging

REQUESTS = Counter(
    "apex_api_requests_total",
    "Total HTTP requests handled by the API",
    ["method", "endpoint", "http_status"],
)


def create_app(test_config: dict | None = None) -> Flask:
    configure_logging(os.getenv("LOG_LEVEL", "INFO"))
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)
    logger = logging.getLogger("apex_operations_api")

    @app.after_request
    def record_request(response):
        endpoint = request.url_rule.rule if request.url_rule else "unmatched"
        REQUESTS.labels(request.method, endpoint, str(response.status_code)).inc()
        logger.info("http_request %s %s %s", request.method, request.path, response.status_code)
        return response

    @app.get("/")
    def index():
        return jsonify({"service": "apex-operations-api", "api_version": "v1"})

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.get("/ready")
    def ready():
        if not database_is_ready():
            return jsonify({"status": "not_ready", "database": "unavailable"}), 503
        return jsonify({"status": "ready", "database": "connected"}), 200

    @app.get("/api/v1/operations")
    def get_operations():
        try:
            return jsonify({"items": list_operations()}), 200
        except Exception:
            logger.exception("operations_list_failed")
            return jsonify({"error": "internal_server_error"}), 500

    @app.post("/api/v1/operations")
    def post_operation():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "invalid_json"}), 400
        name = payload.get("name")
        status = payload.get("status", "created")
        if not isinstance(name, str) or not name.strip() or len(name) > 100:
            return jsonify({"error": "name must be a non-empty string of at most 100 characters"}), 400
        if not isinstance(status, str) or status not in {"created", "in_progress", "completed"}:
            return jsonify({"error": "invalid status"}), 400
        try:
            item = create_operation(name.strip(), status)
            return jsonify(item), 201
        except Exception:
            logger.exception("operation_create_failed")
            return jsonify({"error": "internal_server_error"}), 500

    @app.get("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    return app


app = create_app()
