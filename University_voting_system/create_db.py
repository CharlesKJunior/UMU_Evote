# create_db.py
from app import app
from models import db
import logging
from sqlalchemy import inspect

logging.basicConfig(level=logging.INFO)

with app.app_context():
    db.create_all()
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    logging.info(f"Database tables: {tables}")
    if 'user' in tables and 'vote' in tables:
        print("Database created and tables exist!")
    else:
        print("Database created but required tables do not exist!")
