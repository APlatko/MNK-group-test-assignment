import sqlite3
import pandas as pd


def get_price_comparison() -> None:
    """
    Create a sqlite database and load the content of files into tables.
    Read the SQL query from txt file.
    Reformat the result of the query to be correctly displayed in Excel.
    Save the result to csv file.
    """
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()

    # load two files (result, sample_supplier) to database 'prices' and create two tables
    result_file = pd.read_csv("../task_1/result.csv", sep="\t")
    sample_supplier_file = pd.read_csv("sample_supplier.csv", sep="\t")
    result_file.to_sql("result", conn, if_exists="replace", index=False)
    sample_supplier_file.to_sql("sample_supplier", conn, if_exists="replace", index=False)

    with open('query.txt') as file:
        query = file.read()
    cursor.execute(query)
    rows = cursor.fetchall()

    header = ['part_number', 'manufacturer', 'price', 'source']
    df = pd.DataFrame(rows, columns=header)

    # refactor row 'price' to str format with ';' delimiter
    df['price'] = df['price'].astype(str).str.replace('.', ',')
    df.to_csv("comparison.csv", index=False, sep=';')

    conn.close()


if __name__ == '__main__':
    get_price_comparison()
