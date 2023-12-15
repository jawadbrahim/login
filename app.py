# app.py
from flask import Flask
from flask_migrate import Migrate

from helpers.app_creation import create_app
from database.postgres import sqlalchemy_db

app = create_app()
sqlalchemy_db.init_app(app)

migrate = Migrate(app, sqlalchemy_db)

if __name__ == "__main__":
    app.run(debug=True)
