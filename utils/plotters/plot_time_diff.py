import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_diff(time_diff):
    """
    Generates a distribution plot for time differential between blocks
    """
    plt.figure()
    sns.distplot(time_diff, kde=False).set(xlim=(0, 5000))
    plt.title('Time between blocs')
    plt.xlabel('Time diff (seconds)')
    plt.ylabel('Frequency')
    plt.savefig('images/time_diff_line_plot.png')
