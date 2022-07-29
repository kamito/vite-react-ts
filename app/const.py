import os
from dotenv import load_dotenv

load_dotenv(override=True)

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
IS_LOCAL = os.getenv('IS_LOCAL', False)


class Const(object):

    IS_LOCAL = IS_LOCAL
