from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from app.models.order import Order
from app.models.cart import CartItem
from app.models.product import Product
from app.database import get_session


router = APIRouter()


@router.post('/checkout')
def checkout(session: Session = Depends(get_session)):
    cart_items = session.exec(select(CartItem)).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail='Cart is empty')

    total_price = 0

    # First loop: validate everything and calculate total
    for cart_item in cart_items:
        product = session.get(Product, cart_item.product_id)

        if not product:
            raise HTTPException(status_code=404, detail='Product not found')

        if cart_item.quantity > product.stock:
            raise HTTPException(
                status_code=400,
                detail='Not enough stock available'
            )

        total_price += product.price * cart_item.quantity

    # Second loop: reduce inventory
    for cart_item in cart_items:
        product = session.get(Product, cart_item.product_id)
        product.stock -= cart_item.quantity
        session.add(product)

    # Create the completed order
    order = Order(total_price=round(total_price, 2))
    session.add(order)

    # Clear purchased items from cart
    for cart_item in cart_items:
        session.delete(cart_item)

    session.commit()
    session.refresh(order)

    return order


@router.get('/orders')
def get_orders(session: Session = Depends(get_session)):
    orders = session.exec(select(Order)).all()
    return orders