from __future__ import annotations
from os import getenv


PAYCOM_SETTINGS = {
    "KASSA_ID": getenv("Payme_KASSA_ID"),  # token
    "SECRET_KEY": getenv("Payme_SECRET_KEY"),  # password
    # "ACCOUNTS": {
    #     "KEY": "order_id"
    # },
    "ACCOUNTS": {
        "KEY":getenv("Payme_ACCOUNTS_clint_id")
    },
    "Token":getenv("Payme_Token")
}
