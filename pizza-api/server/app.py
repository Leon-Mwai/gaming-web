from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.models import db
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

# Create the SQLAlchemy db instance here
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize db with the app
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

# actual app instance
app = create_app()
