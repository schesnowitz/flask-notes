from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "random_string"

    return app