import matplotlib.pyplot as plt
import pandas as pd


def plot_block_transaction_values(block_values):
    """
    Generates a histogram plot for block values
    """
    plt.figure()
    block_values_df = pd.Series(block_values).to_frame().reset_index()
    block_values_df.columns = ['Block Hash', 'Value (BTC)']
    block_values_df.hist()
    block_values_df.plot.hist(bins=20)
    plt.title('Block value (BTC)')
    plt.savefig('images/value_per_block_histogram.png')
