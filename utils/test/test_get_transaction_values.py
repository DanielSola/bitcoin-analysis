import unittest
from utils import get_transaction_values
from .expected_values import expected_transaction_values

class TestGetTransactionValues(unittest.TestCase):

    def setUp(self):
      self.blocks_file_path = './data/blocks.json'
      self.transactions_file_path = './data/txs.json'
      self.result = get_transaction_values(self.blocks_file_path, self.transactions_file_path)
    
    def test_get_transaction_values(self):
      values = list(self.result.values())
      self.assertEqual(values, expected_transaction_values)
