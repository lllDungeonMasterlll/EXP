import requests
from backend.backend.celery import shared_task
from .models import Currency, Provider, Block
from django.utils.dateparse import parse_datetime

def fetch_block_data(currency_name):
    if currency_name == "BTC":
        # приклад запиту до CoinMarketCap
        return {
            'block_number': 12345678,
            'created_at': "2023-04-20T12:00:00Z"
        }
    elif currency_name == "ETH":
        # приклад запиту до BlockChair
        return {
            'block_number': 98765432,
            'created_at': "2023-04-20T12:05:00Z"
        }

@shared_task
def fetch_latest_blocks():
    for name in ["BTC", "ETH"]:
        data = fetch_block_data(name)
        currency, _ = Currency.objects.get_or_create(name=name)
        provider = Provider.objects.first()
        block, created = Block.objects.get_or_create(
            currency=currency,
            block_number=data['block_number'],
            defaults={
                'provider': provider,
                'created_at': parse_datetime(data['created_at'])
            }
        )