from flask import Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path


DB_NAME = 'database.db'
db = SQLAlchemy()


def creat_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'    
    app.config['SECRET_KEY'] = 'PIZZARIA'
    
    db.init_app(app)
    
    from .routes import routes
    
    app.register_blueprint(routes, url_prefix='/')
    
    creat_database(app, db)
    
    return app

def creat_database(app, db):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            