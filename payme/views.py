from payments.views import MerchantAPIView
from payments import Paycom
from .models import Order
from rest_framework.decorators import api_view 
from decimal import Decimal




from rest_framework.response import Response
from decimal import Decimal
from environs import Env
from .bot_telegram import sent_message

env = Env()
env.read_env()


class CheckOrder(Paycom):
    def check_order(self, amount: int, account: dict, *args, **kwargs):
        order = Order.objects.filter(order_no=account["order_id"], is_finished=False).first()

        if not order:
            return self.ORDER_NOT_FOND
        if order.summa * 100 == amount:
            return self.INVALID_AMOUNT
        
        return self.ORDER_FOUND
        
    def successfully_payment(self, account: dict, transaction, *args, **kwargs):
        order = Order.objects.filter(order_no=transaction.order_key).first()

        if not order:
            return self.ORDER_NOT_FOND
        
        order.is_finished = True
        order.save()

    def cancel_payment(self, account, transaction, *args, **kwargs):
        print(account)
      

class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


@api_view(['POST'])
def checkout_view(request):
    data = request.data
    if 'id' in data and 'amount' in data:
        order_id = data['id']
        amount = Decimal(data['amount'])
        if 'return_url' in data:
            return_url = data['return_url']
        else:
            return_url = env.str('DEFAULT_URL')
        paycom = Paycom()
        data['url'] = paycom.create_initialization(amount=amount, order_id=order_id, return_url=return_url)
    return Response(data)


