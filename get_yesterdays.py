import datetime
import os
from typing import List
from get_transactions import get_transactions


def get_yesterdays_transactions() -> List[dict]:
    yesterday = ('2017-05-16' if os.getenv('PLAID_ENV') == 'sandbox' else (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    transactions = []

    for access_id in [os.getenv('CHASE_ACCESS_TOKEN'), os.getenv('BOFA_ACCESS_TOKEN')]:
        transactions += get_transactions(access_id, yesterday, yesterday)

    return transactions
