"""Processes the import data"""
class DataProcessor:
    """Can group data and find the extreme values in the data"""
    @staticmethod
    def prepare_data(data, group_column, value_column):
        """Groups the data"""
        return data.groupby(group_column)[value_column].mean().reset_index()

    @staticmethod
    def find_extreme_values(data):
        """Finds the extreme values in the data"""
        for column in data.select_dtypes(include='number').columns:
            print(f"Column: {column}")
            print(f"Minimum value: {data[column].min()}")
            print(f"Maximum value: {data[column].max()}")
