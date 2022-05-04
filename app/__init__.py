from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

'''
import sys
sys.path.insert(0,'../')
'''
from config import config

bootstrap   =Bootstrap()
db          =SQLAlchemy()

def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    
    bootstrap.init_app(app)
    db.init_app(app)
    
    #attach routes & errors
    #
    from main import main as m_blueprint
    app.register_blueprint(m_blueprint)
    
    return app
