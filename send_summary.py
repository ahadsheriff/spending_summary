import os
from typing import List
from twilio.rest import Client as TwilioClient
import math

from get_yesterdays import get_yesterdays_transactions

twilio_client = TwilioClient(
    os.getenv('TWILIO_SID'), os.getenv('TWILIO_TOKEN'))

def send_summary(transactions: List[dict]) -> None:    
    total_spent = sum(transaction['amount'] for transaction in transactions)
    round_up = math.ceil(total_spent)
    calc_change = round_up - total_spent
    change = round(calc_change, 2)
    organization = "12for12"

    print(f"total spent: ${total_spent}")
    print(f"change: ${change}")

    message = f'You spent ${total_spent} yesterday. 💸 We will donate ${change} to {organization}. ❤'
    twilio_client.api.account.messages.create(to=os.getenv('MY_CELL'), from_=os.getenv('MY_TWILIO_NUM'), body=message)

if __name__ == "__main__":
    send_summary(get_yesterdays_transactions())
