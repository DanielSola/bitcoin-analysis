import unittest
from utils import get_all_block_transactions
from .expected_values import expected_number_of_transactions

class TestGetAllBlockTransactions(unittest.TestCase):

    def setUp(self):
      self.blocks_file_path = './data/blocks.json'
      self.result_dict = get_all_block_transactions(self.blocks_file_path)

    def test_number_of_blocks(self):
      expected_number_of_blocks = 144
      obtained_number_of_blocks = len(self.result_dict.keys())

      self.assertEqual(expected_number_of_blocks, obtained_number_of_blocks)

    def test_number_of_transactions(self):
      result_number_of_transactions = list(self.result_dict.values())

      self.assertEqual(result_number_of_transactions, expected_number_of_transactions)