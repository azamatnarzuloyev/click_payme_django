from __future__ import annotations
from os import getenv

CLICK_SETTINGS = {
    'service_id':getenv("click_service_id"),
    'merchant_id':getenv("click_merchant_id"),
    'secret_key':getenv("click_secret_key"),
}


