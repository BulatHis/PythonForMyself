# transform.py
def transform(dataframe):
    # Проверим, что столбец 'existing_column' существует
    if 'existing_column' not in dataframe.columns:
        raise KeyError(f"Column 'existing_column' not found in DataFrame. Available columns are: {list(dataframe.columns)}")

    # Пример простой трансформации
    dataframe.dropna(inplace=True)
    dataframe['new_column'] = dataframe['existing_column'] * 2
    return dataframe
