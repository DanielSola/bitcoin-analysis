import matplotlib.pyplot as plt
import pandas as pd


def plot_all_block_transactions(transacion_count):
    """
    Generates a histogram plot for transactions counts
    """
    plt.figure()
    transaction_count_df = pd.Series(transacion_count).to_frame().reset_index()
    transaction_count_df.columns = ['Hash', '#transactions']
    transaction_count_df.plot.hist(bins=12)
    plt.title('Number of transactions in a block')
    plt.savefig('images/transactions_in_block.png')
