from flask import Flask
from app.config import Config
from app.routes.routes import main_routes
from app.routes.user_route import user_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_routes)
    app.register_blueprint(user_bp)
    return app
