from server.config import db  # ✅ Use the real one from config
from .pizza import Pizza
from .restaurant import Restaurant
from .restaurant_pizza import RestaurantPizza

__all__ = ["db", "Pizza", "Restaurant", "RestaurantPizza"]
