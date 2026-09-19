from fastapi import FastAPI, HTTPException # From the FastAPI Library, i import FastAPI class to create an instance of the FastAPI application.
from pydantic import BaseModel
app = FastAPI() # I have created an instance of the FastAPI application and assigned it to the varibale app. 
# This instance will be used to define routes and handle incoming requests.
@app.get("/") # .get method is used to define a route that responds to HTTP GET requests. 
# The route is defined for the root URL ("/") of the application. When a GET request is made to this URL, the associated function will be executed.
def home(): # The home function is defined to handle the GET requests for the root URL. It returns a JSON response with a message indicating that the E-commerce API is running.
    return {'messsage': "E-commerce API is running"} # Returns a JSON response with a message indicating that E-commerce API is running.

products = [
    {'id': 1, 'name': 'Laptop', 'price': 999},
    {'id': 2, 'name': 'Mouse', 'price': 25},
    {'id': 3, 'name': 'Keyboard', 'price': 50}
]
class Product(BaseModel):
    name: str
    price: float
# Products list is created to store the product data. Each product is represented as a dictionary with three key-value pairs: 'id', 'name', and 'price'.
@app.get("/products") # The .get method is used to define a route that responds to HTTP GET requests.
# Products route is defined for the URL "/products". When a GET request is made to this URL, the associated function will be executed.
def get_products(): # The get_products function is defined to handle the GET requests for the "/products" URL. 
# It returns the products list as a JSON response.
    return products # Products list is returned as a JSON response when a GET request is made to the "/products" URL. 
# This allows clients to retrieve the list of products available in the E-commerce API.
@app.get('/products/{product_id}') # The .get method is used to define a route that responds to HTTP GET requests.
# The route is defined for the URL "/products/{product_id}", where {product_id} is a path parameter that represents the ID of a specific product.
# The ID is a variable that can be passed in the URL to retrieve information about a specific product.
def get_product(product_id: int): # The get_product function is defined to handle the GET requests for the "/products/{product_id}" URL.
# int type hint is used to specify that the product_id parameter should be an integer. This ensures that the function expects an integer value for the product ID.
# Type hinting is a feature in Python that allows developers to indicate the expected data type of function parameters and return values.
# It helps improve code readability and can also be used by static type checkers to catch potential type-related errors during development.
# The product_id parameter is extracted from the URL and passed to the function. It represents the ID of the specific product being requested.
    for product in products: # For each product in the products list, the function checks if the product's ID matches the provided product_id.
        if product['id'] == product_id: # Checks if the product's ID matches the provided product_id.
            return product # Returns the product as a JSON response when a GET request is made to the "/products/{product_id}" URL with a valid product ID.
    raise HTTPException(status_code=404, detail='Product not found')
@app.post('/products') 

def create_product(product: Product):
    new_product = {
        'id': len(products) + 1,
        'name': product.name,
        'price': product.price
    }
    products.append(new_product)
    return new_product
@app.put('/products/{product_id}')

def update_product(product_id: int, product: Product):
    for existing_product in products:
        if existing_product['id'] == product_id:
            existing_product['name'] = product.name
            existing_product['price'] = product.price
            return existing_product
    raise HTTPException(status_code=404, detail='Product not found')

@app.delete('/products/{product_id}')

def delete_product(product_id: int):
    for existing_product in products:
        if existing_product['id'] == product_id:
            products.remove(existing_product)
            return {'message': f"Product {product_id} deleted"}
    raise HTTPException(status_code=404, detail='Product not found')