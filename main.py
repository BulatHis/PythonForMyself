import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URI
from extract import extract_from_csv
from transform import transform
from load import load_to_database
# main.py
from create_table import create_table_from_csv
from config import DATABASE_URI


def main():
    csv_file_path = 'melb_data.csv'
    table_name = 'your_table_name'

    # Создание таблицы и загрузка данных
    create_table_from_csv(csv_file_path, table_name, DATABASE_URI)


if __name__ == "__main__":
    main()
