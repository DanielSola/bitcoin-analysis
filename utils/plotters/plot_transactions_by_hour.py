import matplotlib.pyplot as plt
import pandas as pd


def plot_transactions_by_hour(transactions_by_hour):
    """
    Generates a bar plot for transactions by hour
    """
    plt.figure()

    avg_block_sizes_df = pd.Series(transactions_by_hour).to_frame().reset_index()
    avg_block_sizes_df.columns = ['Date', '#Transactions']
    avg_block_sizes_df.sort_values(by='Date')
    avg_block_sizes_df.plot.bar()
    plt.xticks(range(len(transactions_by_hour)), list(transactions_by_hour.keys()))
    plt.title('Transactions by hour')
    plt.tight_layout()

    plt.savefig('images/transactions_by_hour.png')
