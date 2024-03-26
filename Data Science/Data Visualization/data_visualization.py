import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_line_chart():
    # Generate random data for line chart
    x = np.arange(10)
    y1 = np.random.rand(10)
    y2 = np.random.rand(10)

    # Create line chart
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='Line 1')
    ax.plot(x, y2, label='Line 2')

    # Add axis labels, title, and legend
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Line Chart Example')
    ax.legend()

    # Display the plot
    plt.show()

def visualize_bar_chart():
    # Generate random data for bar chart
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Value 1': np.random.rand(4),
            'Value 2': np.random.rand(4)}

    df = pd.DataFrame(data)

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Value 1'], label='Value 1')
    ax.bar(df['Category'], df['Value 2'], label='Value 2', bottom=df['Value 1'])

    # Add axis labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart Example')

    # Add legend
    ax.legend()

    # Display the plot
    plt.show()

def visualize_histogram():
    # Generate random data for histogram
    data = np.random.rand(1000)

    # Create histogram
    sns.histplot(data, kde=False)

    # Add axis labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram Example')

    # Display the plot
    plt.show()

def main():
    visualize_line_chart()
    visualize_bar_chart()
    visualize_histogram()

if __name__ == '__main__':
    main()
