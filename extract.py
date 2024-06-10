import pandas as pd


def extract_from_csv(file_path):
    return pd.read_csv(file_path)


def extract_from_database(query, connection):
    return pd.read_sql(query, connection)
