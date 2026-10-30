import os

import psycopg
from psycopg.rows import dict_row


def get_connection():
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        raise RuntimeError("DATABASE_URL is not configured")
    return psycopg.connect(database_url, row_factory=dict_row)


def database_is_ready() -> bool:
    try:
        with get_connection() as connection:
            connection.execute("SELECT 1")
        return True
    except (psycopg.Error, RuntimeError):
        return False


def list_operations() -> list[dict]:
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT id, name, status, created_at FROM operations ORDER BY id"
        ).fetchall()
    return [dict(row) for row in rows]


def create_operation(name: str, status: str) -> dict:
    with get_connection() as connection:
        row = connection.execute(
            "INSERT INTO operations (name, status) VALUES (%s, %s) "
            "RETURNING id, name, status, created_at",
            (name, status),
        ).fetchone()
    return dict(row)
