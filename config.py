import datetime

REMEMBER_COOKIE_DURATION = datetime.timedelta(days=1)
DEBUG = True
SQLALCHEMY_DATABASE_URI = "mysql+driver://username:password@server/database"
SECRET_KEY = "secretKey"
JSON_SORT_KEYS = False
MAIL_SERVER = "emailServer"
MAIL_USERNAME = "emailUsername"
MAIL_PASSWORD = "emailPassword"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False