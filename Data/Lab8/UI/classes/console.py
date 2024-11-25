from Data.Lab8.BLL.classes.data_processor import DataProcessor
from Data.Shared.classes.data_io import DataIO
import matplotlib.pyplot as plt
import seaborn as sns
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(filename='Logs/logs.log', encoding='utf-8', level=logging.DEBUG)

class Console:
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Console, self).__call__(*args, **kwargs)
        else:
            self._instances[self].__init__(*args, **kwargs)
        return self._instances[self]

    def __init__(self, file_path='data.csv', group_column='Category', value_column='Purchase Amount (USD)'):
        self.file_path = f"Data/Lab8/Imports/{file_path}"
        self.data = None
        self.group_column = group_column
        self.value_column = value_column
        self.main()

    @staticmethod
    def annotate(ax, group_column, data, is_boxplot=False):
        unique_categories = data[group_column].unique()
        for i, element in enumerate(ax.patches[:len(unique_categories)]):
            category_name = unique_categories[i]
            center_x = element.get_x() + element.get_width() / 2  # Центр стовпця
            height_y = element.get_height()  # Висота стовпця
            if is_boxplot:
                center_x = element.get_x() + element.get_width() / 2
                height_y = element.get_y() + element.get_height()
            ax.text(center_x, height_y + 0.5, category_name, ha='center', fontsize=10)

    def basic_visualization(self):
        prepared_data = DataProcessor.prepare_data(self.data, self.group_column, self.value_column)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(prepared_data[self.group_column], prepared_data[self.value_column], color='skyblue')
        ax.set_xlabel(self.group_column)
        ax.set_ylabel(self.value_column)
        ax.set_title(f"Average {self.value_column} by {self.group_column}")
        ax.tick_params(axis='x', rotation=45)
        # noinspection PyTypeChecker
        self.annotate(ax, self.group_column, prepared_data)
        DataIO.save_visualization(fig, "basic_visualization")
        plt.tight_layout()
        plt.show()
        logger.info("[Lab 8] Ended making basic graph")

    def advanced_visualization(self):
        prepared_data = DataProcessor.prepare_data(self.data, self.group_column, self.value_column)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(prepared_data[self.value_column], kde=True, ax=ax, color='green')
        ax.set_title(f"Histogram of {self.value_column}")
        ax.set_xlabel(self.value_column)
        ax.set_ylabel('Frequency')
        DataIO.save_visualization(fig, "advanced_visualization_histogram")
        plt.tight_layout()
        plt.show()
        logger.info("[Lab 8] Ended making advanced graph")

    def multiple_subplots(self):
        prepared_data = DataProcessor.prepare_data(self.data, self.group_column, self.value_column)
        fig, axs = plt.subplots(1, 2, figsize=(14, 6))
        sns.barplot(x=self.group_column, y=self.value_column, data=prepared_data, ax=axs[0], color='skyblue')
        axs[0].set_title(f"Barplot of {self.value_column}")
        axs[0].set_xlabel(self.group_column)
        axs[0].set_ylabel(self.value_column)
        axs[0].tick_params(axis='x', rotation=45)
        self.annotate(axs[0], self.group_column, prepared_data)
        sns.histplot(prepared_data[self.value_column], kde=True, ax=axs[1], color='green')
        axs[1].set_title(f"Histogram of {self.value_column}")
        axs[1].set_xlabel(self.value_column)
        axs[1].set_ylabel('Frequency')
        DataIO.save_visualization(fig, "multiple_subplots_with_categories")
        plt.tight_layout()
        plt.show()
        logger.info("[Lab 8] Ended making multiple graphs")

    def main(self):
        try:
            self.data = DataIO.load_data(self.file_path)
        except FileNotFoundError as e:
            print(e)
        while True:
            prompt = input("1 - Extreme values\n"
                           "2 - Display basic graph\n"
                           "3 - Display advanced graph\n"
                           "4 - Display multiple graphs\n"
                           "Your choice: ")
            match prompt:
                case '1':
                    logger.info("[Lab 8] Found extreme values")
                    DataProcessor.find_extreme_values(self.data)
                case '2':
                    logger.info("[Lab 8] Started making basic graph")
                    self.basic_visualization()
                case '3':
                    logger.info("[Lab 8] Started making advanced graph")
                    self.advanced_visualization()
                case '4':
                    logger.info("[Lab 8] Started making multiple graphs")
                    self.multiple_subplots()
                case _:
                    return