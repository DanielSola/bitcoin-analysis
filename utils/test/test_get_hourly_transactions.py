import unittest
from utils import get_hourly_transactions
from .expected_values import expected_hourly_transactions

class TestGetHourlyTransactions(unittest.TestCase):

    def setUp(self):
      self.transactions_file_path = './data/txs.json'
      self.result_dict = get_hourly_transactions(self.transactions_file_path)
    
    def test_expected_number_of_values(self):
      expected_number_of_keys = 27
      number_of_keys = len(self.result_dict.keys())
      
      self.assertEqual(expected_number_of_keys, number_of_keys)

    def test_hourly_transactions(self):
      hourly_transactions = list(self.result_dict.values())      

      self.assertEqual(hourly_transactions, expected_hourly_transactions)
