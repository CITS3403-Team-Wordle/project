from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#from wtfroms import StringField, SubmitField
#from wtfroms.validators import Required

'''
import sys
sys.path.insert(0,'../')
'''
from app.config import config

bootstrap   =Bootstrap()
db          =SQLAlchemy()

def create_app(config_type):
    app = Flask(__name__)
    app.config.from_object(config[config_type])
    
    bootstrap.init_app(app)
    db.init_app(app)
    
    #attach routes & errors
    from app.main import main as m_blueprint
    app.register_blueprint(m_blueprint)
    

    from app.auth import auth as a_blueprint
    app.register_blueprint(a_blueprint)

    return app
