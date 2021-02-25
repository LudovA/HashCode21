#%% IMPORTING MODULES
import matplotlib.pyplot as plt
import os


#%% DEFINING FUNCTIONS
def plot_histogram(values, bins, title='Histogram', output_dir=os.path.join(os.path.dirname(os.getcwd()), 'statistics/plots/')):
    plt.hist(values, bins=bins)
    plt.title(title)
    plt.xlabel('Values')
    plt.ylabel('Count')

    if output_dir:
        output_path = os.path.join(output_dir, title + '.png')
        plt.savefig(output_path)

    plt.show()

