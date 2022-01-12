SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/wjxtest?charset=utf8'
class BaseConfig(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class DevelopmentConfig(BaseConfig):
    DATABASE_URI = 'sqlite://:memory:'
