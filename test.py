import unittest
from utils.test import\
  TestGetAllBlockTransactions, \
  TestGetAverageBlockSizeByHour, \
  TestGetHourlyTransactions, \
  TestGetTimeBetweenBlocks, \
  TestGetTransactionValues

suite_get_all_block_transactions = unittest.TestLoader().loadTestsFromTestCase(TestGetAllBlockTransactions)
suite_get_avg_block_size_by_hour = unittest.TestLoader().loadTestsFromTestCase(TestGetAverageBlockSizeByHour)
suite_get_hourly_transactions = unittest.TestLoader().loadTestsFromTestCase(TestGetHourlyTransactions)
suite_get_time_between_blocks = unittest.TestLoader().loadTestsFromTestCase(TestGetTimeBetweenBlocks)
suite_get_transaction_values = unittest.TestLoader().loadTestsFromTestCase(TestGetTransactionValues)

all_suites = unittest.TestSuite([
  suite_get_all_block_transactions,
  suite_get_avg_block_size_by_hour,
  suite_get_hourly_transactions,
  suite_get_time_between_blocks,
  suite_get_transaction_values
  ])

unittest.TextTestRunner(verbosity = 2).run(all_suites)