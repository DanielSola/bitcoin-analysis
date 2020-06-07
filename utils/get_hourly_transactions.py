import json
from datetime import datetime


def get_hourly_transactions(transactions_file_path):
    """
    Return the time between blocks in a file.
    """
    hourly_transactions = {}
    with open(transactions_file_path) as transactions_file:
        for line in transactions_file:
            transaction = json.loads(line)
            transaction_timestamp = transaction['time']
            date_hour_format = '%Y-%m-%d %H'
            transaction_time = datetime.fromtimestamp(transaction_timestamp).strftime(date_hour_format)

            if transaction_time in hourly_transactions:
                hourly_transactions[transaction_time] += 1
            else:
                hourly_transactions[transaction_time] = 1

    return hourly_transactions
