import unittest
from utils import get_avg_block_size_by_hour
from .expected_values import expected_block_sizes

class TestGetAverageBlockSizeByHour(unittest.TestCase):

    def setUp(self):
      self.blocks_file_path = './data/blocks.json'
      self.result_dict = get_avg_block_size_by_hour(self.blocks_file_path)

    
    def test_expected_number_of_values(self):
      expected_number_of_keys = 27
      number_of_keys = len(self.result_dict.keys())
      
      self.assertEqual(expected_number_of_keys, number_of_keys)

    def test_avg_block_sizes(self):
      block_sizes = list(self.result_dict.values())      

      self.assertEqual(block_sizes, expected_block_sizes)
