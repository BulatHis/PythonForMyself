from sqlalchemy import create_engine


def load_to_database(dataframe, table_name, connection_string):
    engine = create_engine(connection_string)
    dataframe.to_sql(table_name, engine, if_exists='replace', index=False)
