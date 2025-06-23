from flask import Flask
from flask_migrate import Migrate               # ✅ import Migrate
from server.config import Config
from server.models import db
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)                   # ✅ initialize Migrate

    app.register_blueprint(restaurant_bp, url_prefix='/')
    app.register_blueprint(pizza_bp, url_prefix='/')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/')

    return app

app = create_app()
