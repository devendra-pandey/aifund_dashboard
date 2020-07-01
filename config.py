import os

UPLOAD_FOLDER = 'uploads'
UPLOAD_FOLDER_PATH = os.path.join(os.path.dirname(__name__), UPLOAD_FOLDER)
if not os.path.exists(UPLOAD_FOLDER_PATH):
    os.mkdirs(UPLOAD_FOLDER_PATH)


class BaseCofig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseCofig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:sdp150516@localhost:3306/destimate_flask'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/destimate'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "aifunddashboardworkinfine"
    ENV = "development"
    UPLOAD_FOLDER = UPLOAD_FOLDER_PATH


class ProductionConfig(BaseCofig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/aifund'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "aifunddashboardworkinfine"
    UPLOAD_FOLDER = UPLOAD_FOLDER_PATH