from sqlalchemy import create_engine

POSTGRES_PASSWORD = 'postgres'
POSTGRES_USER     = 'postgres'
POSTGRES_DB       = 'test_alembic'

connect_string = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"
engine = create_engine(connect_string)
