# coding: utf-8
from .default import Config


class ProductionConfig(Config):
    # App config
    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
    SESSION_COOKIE_NAME = 'FlaskBookRead_session'

    # Site domain
    SITE_DOMAIN = "http://www.FlaskBookRead.com"

    # Db config
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/FlaskBookRead"

    # Sentry
    SENTRY_DSN = ''
