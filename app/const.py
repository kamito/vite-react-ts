import os
import json
from dotenv import load_dotenv

load_dotenv(override=True)

FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
IS_LOCAL = os.getenv('IS_LOCAL', False)


class Const(object):

    IS_LOCAL = IS_LOCAL


    def __init__(self, is_debug=False):
        self.IS_DEBUG = is_debug
        self.IS_LOCAL = self.__class__.IS_LOCAL

        self.JAVASCRIPTS = []
        self.STYLESHEETS = []
        self.load_manifest()

    def load_manifest(self):
        if not self.IS_DEBUG:
            manifest = None
            manifest_path = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    "../frontend/dist/manifest.json"
                    ))
            with open(manifest_path) as fp:
                manifest = json.load(fp)

            if manifest:
                for k, m in manifest.items():
                    filename = m['file']
                    ext = filename.split('.').pop()
                    if ext == "js":
                        self.JAVASCRIPTS.append(filename)
                    elif ext == "css":
                        self.STYLESHEETS.append(filename)
