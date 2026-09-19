from fastapi import APIRouter, HTTPException
from app.models.product import Product

router = APIRouter()

products = [
    {'id': 1, 'name': 'Laptop', 'price': 999},
    {'id': 2, 'name': "Mouse", 'price': 25},
    {'id': 3, 'name': 'Keyboard', 'price': 50}
]

@router.get('/products')
def get_products():
    return products

@router.get('/products/{product_id}')
def get_product(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return product
    raise HTTPException(status_code=404, detail='Product not found')

@router.post('/products')
def create_product(product: Product):
    new_product = {
        'id': len(products) + 1,
        'name': product.name,
        'price': product.price
    }
    products.append(new_product)
    return new_product

@router.put('/products/{product_id}')
def update_product(product_id: int, product: Product):
    for existing_product in products:
        if existing_product['id'] == product_id:
            existing_product['name'] = product.name
            existing_product['price'] = product.price
            return existing_product
    raise HTTPException(status_code=404, detail='Product not found')

@router.delete('/products/{product_id}')
def delete_product(product_id: int):
    for existing_product in products:
        if existing_product['id'] == product_id:
            products.remove(existing_product)
            return {'message': f'product {product_id} deleted'}
    raise HTTPException(status_code=404, detail='Product not found')