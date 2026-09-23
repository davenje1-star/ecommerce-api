# E-Commerce API

A Python e-commerce API built for learning backend development.

## Features

Create and manage products in the product inventory.
Add products and specified quantities to the shopping cart.
Remove items from the shopping cart.
Update or delete existing products.
Checkout items in the cart and create an order.
Automatically reduce product stock after checkout.
Retrieve previously created orders.
Filter products by category.
Validate product, stock, and cart quantity inputs.

## Technologies Used

Python — Primary programming language used to build the API.
FastAPI — Web framework used to create API routes and handle HTTP requests.
SQLModel — Used to define database models, validate data, and interact with the database.
SQLite — Database used to store products, cart items, and orders.
Uvicorn — ASGI server used to run the FastAPI application locally.
Git & GitHub — Used for version control and hosting the project repository.
Swagger UI — Used through FastAPI's /docs page to test and interact with API endpoints.

## API Endpoints

Method	Endpoint	Description
GET	/	Checks that the API is running.
GET	/products	Retrieves all products. Can optionally filter products by category.
GET	/products/{product_id}	Retrieves a specific product by its ID.
POST	/products	Creates a new product.
PUT	/products/{product_id}	Updates an existing product.
DELETE	/products/{product_id}	Deletes a product.
GET	/cart	Retrieves all items currently in the shopping cart.
POST	/cart	Adds a product and quantity to the shopping cart.
DELETE	/cart/{item_id}	Removes a specific item from the shopping cart.
POST	/checkout	Checks out the cart, creates an order, reduces product stock, and clears the cart.
GET	/orders	Retrieves all completed orders.

## Project Structure

```text
ecommerce-api/
├── app/
│   ├── models/
│   │   ├── cart.py
│   │   ├── order.py
│   │   └── product.py
│   ├── routers/
│   │   ├── cart.py
│   │   ├── orders.py
│   │   └── products.py
│   └── database.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

* **`main.py`** — Creates the FastAPI application, initializes the database at startup, and registers the API routers.
* **`database.py`** — Configures the SQLite database engine and provides database sessions.
* **`models/`** — Contains the SQLModel classes used to represent products, cart items, and orders.
* **`routers/`** — Contains the API endpoints for product, cart, and order functionality.
* **`requirements.txt`** — Lists the Python dependencies required to run the project.
* **`.gitignore`** — Prevents local files such as the virtual environment and SQLite database from being tracked by Git.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/davenje1-star/ecommerce-api.git
```

2. Navigate into the project directory:

```bash
cd ecommerce-api
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment.

**Windows Command Prompt:**

```bash
.venv\Scripts\activate.bat
```


5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

1. Make sure the virtual environment is activated.

2. Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

3. Once the server is running, the API is available locally at:

```text
http://127.0.0.1:8000
```

4. Open the interactive Swagger UI documentation to view and test the API endpoints:

```text
http://127.0.0.1:8000/docs
```

The root endpoint can also be used to verify that the API is running:

```text
GET /
```

which returns:

```json
{
  "message": "E-commerce API is running"
}
```


## Example Requests and Responses

### Create a Product

**Request:**

```http
POST /products
```

```json
{
  "name": "Wireless Mouse",
  "description": "Wireless mouse for everyday use",
  "category": "Electronics",
  "price": 25.99,
  "stock": 10
}
```

**Response:**

```json
{
  "name": "Wireless Mouse",
  "description": "Wireless mouse for everyday use",
  "category": "Electronics",
  "price": 25.99,
  "stock": 10,
  "id": 1
}
```

### Add a Product to the Cart

**Request:**

```http
POST /cart
```

```json
{
  "product_id": 1,
  "quantity": 2
}
```

**Response:**

```json
{
  "product_id": 1,
  "quantity": 2,
  "id": 1
}
```

### Checkout

**Request:**

```http
POST /checkout
```

**Response:**

```json
{
  "id": 1,
  "total_price": 51.98
}
```

During checkout, the API calculates the total price, creates an order, reduces the purchased product's stock, and clears the shopping cart.


## What I Learned

As my first project, I learned a lot about the different parts that make up the backend API. Some of the main concepts I learned include:

* Creating API endpoints using FastAPI and HTTP methods such as GET, POST, PUT, and DELETE.
* Organizing a larger Python project using separate models, routers, and database files.
* Using SQLModel and SQLite to store and retrieve persistent data.
* Creating database sessions and using dependency injection with FastAPI.
* Using request models to validate user input before storing data.
* Handling errors using HTTP status codes such as 400, 404, and 422.
* Implementing backend logic for shopping carts, checkout, inventory updates, and orders.
* Testing API endpoints using FastAPI's Swagger UI

## Debugging Challenges

I encountered some debugging situations such as a
`sqlite3.OperationalError: table product has no column named description`.
This error occurred when the Product model was updated with new fields but the existing SQLite database still had the old table structure. 
I was able to fix the error by deleting the existing database and allowing the application to recreate it with the updated table structure.
Another situation was when I kept getting hit by a `500 Internal Server Error` while changing the POST /products endpoint to use ProductCreate. 
I had to align the request model, database model, and route so the endpoint could process the request correctly. This helped me understand the difference between a server error such as 500 and a validation error such as 422.

## Future Improvements

Some features I would like to add to my E-commerce API in the future include:

* User accounts and authentication.
* More detailed order information, including the products and quantities included in each order.
* Improved product searching, filtering, and sorting.
* Automated tests for API endpoints and checkout functionality.
* Deployment of the API so it can be accessed outside of a local development environment.
