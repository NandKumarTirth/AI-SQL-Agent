import sqlite3
import pandas as pd


def create_database(csv_file):

    df = pd.read_csv(csv_file)

    conn = sqlite3.connect("database.db")

    df.to_sql(
        "data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    return list(df.columns)


def run_query(query):

    conn = sqlite3.connect("database.db")

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result