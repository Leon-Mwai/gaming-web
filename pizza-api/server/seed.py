from server.app import create_app
from server.models import db, Pizza, Restaurant, RestaurantPizza

app = create_app()

with app.app_context():
    # clear tables
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # seed data
    r1 = Restaurant(name="Pizza Palace", address="123 Cheese St")
    r2 = Restaurant(name="Tomato Town", address="456 Sauce Ave")

    p1 = Pizza(name="Pepperoni", ingredients="cheese, pepperoni, tomato sauce")
    p2 = Pizza(name="Margarita", ingredients="cheese, tomato, basil")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=8, pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("Database seeded successfully!")
