import unittest
from utils import get_time_between_blocks
from .expected_values import expected_times_between_blocks

class TestGetTimeBetweenBlocks(unittest.TestCase):

    def setUp(self):
      self.blocks_file_path = './data/blocks.json'
      self.result_time = get_time_between_blocks(self.blocks_file_path)
    
    def test_time_between_blocks(self):
      self.assertEqual(self.result_time, expected_times_between_blocks)
