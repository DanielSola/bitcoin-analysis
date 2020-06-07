import matplotlib.pyplot as plt
import pandas as pd


def plot_avg_block_size(avg_block_sizes):
    """
    Generates a bar plot for average block sizes for a given date and hour
    """
    plt.figure()

    avg_block_sizes_df = pd.Series(avg_block_sizes).to_frame().reset_index()
    avg_block_sizes_df.columns = ['Date', 'Average Size']
    avg_block_sizes_df.sort_values(by='Date')
    avg_block_sizes_df.plot.bar()
    plt.xticks(range(len(avg_block_sizes)), list(avg_block_sizes.keys()))
    plt.tight_layout()

    plt.title('Average block size')
    plt.savefig('images/avg_block_size.png')
