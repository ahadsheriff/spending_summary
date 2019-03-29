import datetime
import os
from typing import List
from get_transactions import get_transactions

def get_yesterdays_transactions() -> List[dict]:

    chase = os.getenv('CHASE_ACCESS_TOKEN')
    bofa = os.getenv('BOFA_ACCESS_TOKEN')
    banks = [chase, bofa]

    yesterday = ('2019-03-19' if os.getenv('PLAID_ENV') == 'sandbox' else (
        datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    transactions = []

    for access_id in banks:
        transactions += get_transactions(access_id, yesterday, yesterday)
        
    return transactions