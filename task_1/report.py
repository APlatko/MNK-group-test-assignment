import pandas as pd


def get_report_by_brands() -> None:
    """
    Count unique brads and rows mentioned under brand.
    Output in format BRAND1 - 5000 rows saves to txt file.
    """
    data = pd.read_csv('result.csv', sep='\t')
    positions_by_brand = data.groupby('manufacturer').size().reset_index(name='rows_count')

    # refactor rows to required format
    positions_by_brand = positions_by_brand.apply(format_brand_rows, axis=1)
    positions_by_brand.to_csv('report.txt', index=False, header=None, sep='\t')


def format_brand_rows(row) -> str:
    return f"{row['manufacturer']} - {row['rows_count']} rows"


if __name__ == '__main__':
    get_report_by_brands()
