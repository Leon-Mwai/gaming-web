from flask import Blueprint, jsonify
from server.models.pizza import Pizza
from server.models import db


pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas')
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "ingredients": p.ingredients
    } for p in pizzas])
