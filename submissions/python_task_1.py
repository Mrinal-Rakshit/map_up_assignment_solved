import pandas as pd
import numpy as np


dataset1_df = pd.read_csv('dataset-1.csv')
dataset2_df = pd.read_csv('dataset-2.csv')
dataset3_df = pd.read_csv('dataset-3.csv')

df = pd.DataFrame(dataset1_df)
# df = pd.DataFrame(dataset2_df)

def generate_car_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a DataFrame for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    car_matrix = df.pivot_table(index='id_1', columns='id_2', values='car', aggfunc='sum', fill_value=0)
    return car_matrix

car_matrix = generate_car_matrix(df)
print(car_matrix)


def get_type_count(df: pd.DataFrame) -> dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')], labels=['low', 'medium', 'high'])
    type_count = df['car_type'].value_counts().to_dict()
    return dict(sorted(type_count.items()))

type_count_result = get_type_count(df)
print(type_count_result)


def get_bus_indexes(df: pd.DataFrame) -> list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    mean_bus = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.to_list()
    return sorted(bus_indexes)


bus_indexes_result = get_bus_indexes(df)
print(bus_indexes_result)


def filter_routes(df: pd.DataFrame) -> list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    avg_truck_by_route = df.groupby('route')['truck'].mean()
    filtered_routes = avg_truck_by_route[avg_truck_by_route > 7].index.tolist()
    return sorted(filtered_routes)

filtered_routes_result = filter_routes(df)
print(filtered_routes_result)


def multiply_matrix(matrix_df: pd.DataFrame) -> pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix_df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    modified_matrix = matrix_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25).round(1)
    return modified_matrix

modified_matrix_result = multiply_matrix(car_matrix)
print(modified_matrix_result)


# def time_check(df: pd.DataFrame) -> pd.Series:
#     """
#     Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         pd.Series: return a boolean series
#     """
#     df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
#     df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
#     df['time_check'] = (df['end_datetime'] - df['start_datetime'] == pd.Timedelta(days=1) - pd.Timedelta(seconds=1))
#     return df.groupby(['id', 'id_2'])['time_check'].all()

# time_check_result = time_check(df)
# print(time_check_result)
