

from asyncio.log import logger
from clickchat import ClickUz
from .models import OrderPayment



def create_click_payment(amount:float, order:object ):
    """
    Create click payment
    args: amount, order
    return: url for click `payment
    """
    try:
        order, _ = OrderPayment.objects.get_or_create(
            amount=amount,
            order=order
        )
        url = ClickUz.generate_url(order_id=str(order.id), 
        amount=str(order.amount))
        return True, url
    except Exception as e:
        logger.error(e)
        return False, e