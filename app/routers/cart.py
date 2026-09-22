from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.cart import CartItem, CartItemCreate
from app.models.product import Product
from app.database import get_session

router = APIRouter()

@router.post('/cart')
def add_to_cart(cart_item: CartItemCreate, session: Session = Depends(get_session)):
    product = session.get(Product, cart_item.product_id)

    if not product:
        raise HTTPException(status_code=404, detail='Product not found')

    if cart_item.quantity > product.stock:
        raise HTTPException(status_code=400, detail='Not enough stock available')

    db_cart_item = CartItem.model_validate(cart_item)

    session.add(db_cart_item)
    session.commit()
    session.refresh(db_cart_item)

    return db_cart_item 

@router.get('/cart')
def get_cart(session: Session = Depends(get_session)):
    cart_items = session.exec(select(CartItem)).all()
    return cart_items

@router.delete('/cart/{item_id}')
def remove_from_cart(item_id: int, session: Session = Depends(get_session)):
    cart_item = session.get(CartItem, item_id)

    if not cart_item:
        raise HTTPException(status_code=404, detail='Cart item not found')

    session.delete(cart_item)
    session.commit()

    return {'message': 'Cart item removed'}