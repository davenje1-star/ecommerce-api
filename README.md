# E-Commerce API

A Python e-commerce REST API built with FastAPI for learning backend development, database integration, API design, and deployment.

## Live API

The API is deployed on Render and uses Neon PostgreSQL as the production database.

Live API:

```text
https://ecommerce-api-438s.onrender.com
```

The root URL automatically redirects to the interactive Swagger UI documentation:

```text
https://ecommerce-api-438s.onrender.com/docs
```

## Features

- Create and manage products in the product inventory.
- Retrieve all products or a specific product by ID.
- Filter products by category.
- Update or delete existing products.
- Add products and specified quantities to the shopping cart.
- Remove items from the shopping cart.
- Checkout items in the cart and create an order.
- Automatically reduce product stock after checkout.
- Clear the shopping cart after checkout.
- Retrieve previously created orders.
- Validate product prices, stock quantities, and cart quantities.

## Technologies Used

- **Python** — Primary programming language used to build the API.
- **FastAPI** — Web framework used to create API routes and handle HTTP requests.
- **SQLModel** — Used to define database models, validate data, and interact with the database.
- **SQLite** — Used as the default local development database.
- **PostgreSQL** — Used as the production database.
- **Neon** — Hosts the production PostgreSQL database.
- **Uvicorn** — ASGI server used to run the FastAPI application.
- **Render** — Hosts and deploys the live API.
- **Git & GitHub** — Used for version control and hosting the project repository.
- **Swagger UI** — Available through FastAPI's `/docs` page for testing and interacting with API endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Redirects to the Swagger UI documentation. |
| GET | `/products` | Retrieves all products. Can optionally filter products by category. |
| GET | `/products/{product_id}` | Retrieves a specific product by ID. |
| POST | `/products` | Creates a new product. |
| PUT | `/products/{product_id}` | Updates an existing product. |
| DELETE | `/products/{product_id}` | Deletes a product. |
| GET | `/cart` | Retrieves all items currently in the shopping cart. |
| POST | `/cart` | Adds a product and quantity to the shopping cart. |
| DELETE | `/cart/{item_id}` | Removes a specific item from the shopping cart. |
| POST | `/checkout` | Checks out the cart, creates an order, reduces product stock, and clears the cart. |
| GET | `/orders` | Retrieves all completed orders. |

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

- **`main.py`** — Creates the FastAPI application, initializes database tables at startup, registers the API routers, and redirects the root route to Swagger UI.
- **`database.py`** — Configures the database engine and provides database sessions.
- **`models/`** — Contains the SQLModel classes used to represent products, cart items, and orders.
- **`routers/`** — Contains the API endpoints for product, cart, and order functionality.
- **`requirements.txt`** — Lists the Python dependencies required to run the project.
- **`.gitignore`** — Prevents local files such as the virtual environment and SQLite database from being tracked by Git.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/davenje1-star/ecommerce-api.git
```

### 2. Navigate into the project directory

```bash
cd ecommerce-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Install the required dependencies

On Windows:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Running the API Locally

Start the FastAPI application using Uvicorn:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Once the server is running, open:

```text
http://127.0.0.1:8000
```

The root URL redirects automatically to the Swagger UI documentation:

```text
http://127.0.0.1:8000/docs
```

## Database Configuration

The application reads its database connection from the `DATABASE_URL` environment variable.

If no `DATABASE_URL` is provided, the application uses the local SQLite database:

```text
sqlite:///./ecommerce.db
```

To connect to PostgreSQL locally, set the environment variable before starting the application.

Example:

```powershell
$env:DATABASE_URL="postgresql+psycopg://USERNAME:PASSWORD@HOST/DATABASE"
```

The deployed Render service uses a Neon PostgreSQL database through the `DATABASE_URL` environment variable.

Database credentials are stored as environment variables and are not included in the source code.

## Example Requests and Responses

### Create a Product

**Request**

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

**Response**

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

**Request**

```http
POST /cart
```

```json
{
  "product_id": 1,
  "quantity": 2
}
```

**Response**

```json
{
  "product_id": 1,
  "quantity": 2,
  "id": 1
}
```

### Checkout

**Request**

```http
POST /checkout
```

**Response**

```json
{
  "id": 1,
  "total_price": 51.98
}
```

During checkout, the API calculates the total price, creates an order, reduces the purchased product stock, and clears the shopping cart.

## Deployment

The API is deployed using:

- **GitHub** for source control.
- **Render** for hosting the FastAPI web service.
- **Neon** for the production PostgreSQL database.

Render installs the dependencies using:

```bash
pip install -r requirements.txt
```

and starts the application using:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

The production database connection is provided through Render's `DATABASE_URL` environment variable.

## What I Learned

As my first backend project, I learned about several parts of building and deploying an API, including:

- Creating API endpoints using FastAPI and HTTP methods such as GET, POST, PUT, and DELETE.
- Organizing a larger Python project using separate models, routers, and database files.
- Using SQLModel to define database models and interact with databases.
- Using SQLite during local development and PostgreSQL in production.
- Creating database sessions and using dependency injection with FastAPI.
- Using request models to validate user input before storing data.
- Handling errors using HTTP status codes such as 400, 404, 422, and 500.
- Implementing backend logic for shopping carts, checkout, inventory updates, and orders.
- Testing API endpoints using FastAPI's Swagger UI.
- Using environment variables to protect database credentials.
- Connecting a FastAPI application to a hosted PostgreSQL database.
- Deploying a backend API to Render using GitHub.
- Using Neon to host a production PostgreSQL database.

## Debugging Challenges

One debugging issue I encountered was:

```text
sqlite3.OperationalError: table product has no column named description
```

This occurred after the `Product` model was updated with new fields while the existing SQLite database still contained the old table structure.

I fixed the issue by deleting the existing development database and allowing the application to recreate it with the updated table structure.

Another issue occurred while changing the `POST /products` endpoint to use `ProductCreate`, which resulted in a `500 Internal Server Error`.

I had to align the request model, database model, and route so the endpoint could process the request correctly. This helped me better understand the difference between server errors such as `500` and validation errors such as `422`.

During deployment, I also learned how database drivers affect SQLAlchemy connection strings. The PostgreSQL connection needed to explicitly use the Psycopg driver:

```text
postgresql+psycopg://
```

This helped me understand how the application, database driver, SQLAlchemy, and hosted PostgreSQL database work together.

## Future Improvements

Some features I would like to add in the future include:

- User accounts and authentication.
- More detailed order information, including the products and quantities included in each order.
- Improved product searching, filtering, and sorting.
- Automated tests for API endpoints and checkout functionality.
- Database migrations for managing schema changes.
- Pagination for larger product and order collections.
- A frontend interface that allows users to interact with the API as a complete e-commerce application.