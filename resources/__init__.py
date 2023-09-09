from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv

from .info import blp as StoreBlueprint

def create_app():

    app = Flask(__name__)
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Backend Stage One Task"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    api = Api(app)

    api.register_blueprint(StoreBlueprint)

    return app