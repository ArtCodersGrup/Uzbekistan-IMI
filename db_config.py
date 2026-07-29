"""Shared DB connection config for the one-off migration scripts.

Reads credentials from .env so passwords never live in tracked source files.
"""
import os

_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')


def _load_env(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


if not os.path.exists(_ENV_PATH):
    raise FileNotFoundError(
        f".env fayl topilmadi: {_ENV_PATH}. DB_HOST/DB_PORT/DB_NAME/DB_USER/DB_PASSWORD shu faylda bo'lishi kerak."
    )

_load_env(_ENV_PATH)

DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
