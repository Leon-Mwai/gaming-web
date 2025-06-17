# Pizza API

A RESTful Flask API for managing restaurants, pizzas, and their associations.

## Setup Instructions

1. Clone the repo and navigate to the project folder:

2. Install dependencies and activate virtual environment:

3. Run the application:

## Database Setup

1. Initialize and migrate the database:

2. Seed the database:

## API Routes

### GET /restaurants
Returns a list of all restaurants.

### GET /restaurants/<int:id>
Returns details of a specific restaurant with its pizzas.  
Returns 404 with `{ "error": "Restaurant not found" }` if not found.

### DELETE /restaurants/<int:id>
Deletes the specified restaurant and all related restaurant-pizzas.  
Returns 204 on success, 404 if not found.

### GET /pizzas
Returns a list of all pizzas.

### POST /restaurant_pizzas
Creates a new RestaurantPizza.

**Request body:**
```json
{
"price": 5,
"pizza_id": 1,
"restaurant_id": 3
}
{
  "errors": ["Price must be between 1 and 30"]
}
