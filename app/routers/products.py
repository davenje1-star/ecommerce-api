from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.product import Product, ProductCreate
from app.database import get_session

router = APIRouter()

@router.get('/products')
def get_products(category: str | None = None, session: Session = Depends(get_session)):
    statement = select(Product)

    if category:
        statement = statement.where(Product.category == category)

    products = session.exec(statement).all()
    return products

@router.get('/products/{product_id}')
def get_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.post('/products')
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product.model_validate(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.put('/products/{product_id}')
def update_product(product_id: int, updated_product: Product, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    product.name = updated_product.name
    product.price = updated_product.price
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.delete('/products/{product_id}')
def delete_product(product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    session.delete(product)
    session.commit()
    return {'message': f'Product {product_id} deleted'} 