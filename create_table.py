# create_table_from_csv.py
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date
from sqlalchemy.types import TypeEngine
from config import DATABASE_URI


def get_column_type(dtype: str) -> TypeEngine:
    if pd.api.types.is_integer_dtype(dtype):
        return Integer
    elif pd.api.types.is_float_dtype(dtype):
        return Float
    elif pd.api.types.is_string_dtype(dtype):
        return String
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return Date
    else:
        return String


def create_table_from_csv(csv_file_path: str, table_name: str, connection_string: str):
    # Прочитать CSV файл
    df = pd.read_csv(csv_file_path)

    # Определить структуру таблицы
    columns = []
    for col_name, dtype in zip(df.columns, df.dtypes):
        col_type = get_column_type(dtype)
        columns.append(Column(col_name, col_type))

    # Создать таблицу в базе данных
    engine = create_engine(connection_string)
    metadata = MetaData()
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)

    # Загрузить данные в таблицу
    df.to_sql(table_name, engine, if_exists='replace', index=True)


if __name__ == "__main__":
    csv_file_path = 'melb_data.csv'
    table_name = 'your_table_name'
    create_table_from_csv(csv_file_path, table_name, DATABASE_URI)
