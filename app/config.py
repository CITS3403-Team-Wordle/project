import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'cits3403'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_data.sqlite')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev_data.sqlite')# or os.environ.get('DEV_DATABASE_URL')


class ProductionConfig(Config):

    @classmethod
    def init_app():
        Config.init_app(app)

class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNGING)
        app.logger.addHandler(file_handler)

config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    
    'default': DevelopmentConfig,
}