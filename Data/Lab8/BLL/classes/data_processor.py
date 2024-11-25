class DataProcessor:
    @staticmethod
    def prepare_data(data, group_column, value_column):
        return data.groupby(group_column)[value_column].mean().reset_index()

    @staticmethod
    def find_extreme_values(data):
        for column in data.select_dtypes(include='number').columns:
            print(f"Column: {column}")
            print(f"Minimum value: {data[column].min()}")
            print(f"Maximum value: {data[column].max()}")