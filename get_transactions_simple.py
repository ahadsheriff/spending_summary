import os
import math
from decimal import Decimal
from pprint import pprint
from typing import List

# twilio.rest has a Client too, so let's avoid a namespace collision
from plaid import Client as PlaidClient

plaid_client = PlaidClient(client_id=os.getenv('PLAID_CLIENT_ID'), secret=os.getenv('PLAID_SECRET'), public_key=os.getenv('PLAID_PUBLIC_KEY'), environment=os.getenv('PLAID_ENV'))

def get_some_transactions(access_token: str, start_date: str, end_date: str) -> List[dict]:
    return plaid_client.Transactions.get(access_token, start_date, end_date)

some_transactions = get_some_transactions(
    os.getenv('CHASE_ACCESS_TOKEN'), '2019-01-01', '2019-03-27')

for transaction in some_transactions['transactions']:
    name = transaction['name']
    amount = transaction['amount']
    round_up = math.ceil(amount)
    calc_change = round_up - amount
    change = round(calc_change, 2)

    print('You spent $' + str(amount), 'at', name + '. Spare change:', change)

"""
print(f'there are {some_transactions["total_transactions"]} total transactions between those dates.')
print(f'get_some_transactions returned {len(some_transactions["transactions"])} transactions.')

pprint(some_transactions['transactions'][0].keys())

print({category
    for transaction in some_transactions['transactions'] if transaction['category'] is not None
    for category in transaction['category']})

pprint(some_transactions['accounts'])
"""
