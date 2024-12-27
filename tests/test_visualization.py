import unittest
import pandas as pd
import matplotlib.pyplot as plt
from src.visualization import plot_data


class TestVisualization(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["X", "Y", "X", "Y", "X"]
        })

    def test_plot_data_box_plot(self):
        # Test Box Plot
        plot_data(self.df, None, "A", "Box Plot")
        plt.clf()  # Clear the plot after testing

    def test_plot_data_violin_plot(self):
        # Test Violin Plot
        plot_data(self.df, None, "A", "Violin Plot")
        plt.clf()  # Clear the plot after testing

    def test_plot_data_bar_plot(self):
        # Test Bar Plot
        plot_data(self.df, None, "C", "Bar")
        plt.clf()  # Clear the plot after testing

    def test_plot_data_scatter_plot(self):
        # Test Scatter Plot
        plot_data(self.df, "A", "B", "Scatter Plot")
        plt.clf()  # Clear the plot after testing


if __name__ == '__main__':
    unittest.main()
