from django.urls import path

from main.click import TestView
from main.create_payment import create_click_payment

urlpatterns = [
    path('click/transaction/', TestView.as_view(), name='click-transaction'),
    path('create-click-payment/', create_click_payment, name='create-click-payment'),
    path('testview/', TestView.as_view()),
]
