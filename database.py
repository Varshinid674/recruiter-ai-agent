from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///candidates.db")

# force create database by executing query
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY);"))

print("Database created successfully")