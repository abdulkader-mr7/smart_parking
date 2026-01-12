from flask import Flask
from config import Config
import os



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


    # Register Blueprint
    from routes import bp
    from verify import verify
    app.register_blueprint(bp)
    app.register_blueprint(verify)

    return app
