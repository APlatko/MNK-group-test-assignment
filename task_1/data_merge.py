import pandas as pd


def get_data_merged() -> None:
    """
    Take 3 csv files data, prices, quantity and merge them by part_number.
    Make result.csv file where only lines with availability and price greater than zero.
    The result file has a format: part_number, manufacturer, price, quantity.
    !!! to the quantity.csv file was manually added a header 'part_number	quantity' !!!
    """
    data = pd.read_csv('data.csv', sep='\t')
    price = pd.read_csv('prices.csv', sep='\t')
    quantity = pd.read_csv('quantity.csv', sep='\t')

    merged_data = pd.merge(data, price, on='part_number')
    merged_data = pd.merge(merged_data, quantity, on='part_number')

    # refactor quantity in order to make filtering
    merged_data['price'] = merged_data['price'].str.replace(',', '.').astype(float)
    merged_data['quantity'] = merged_data['quantity'].replace('>10', 11).astype(int)
    filtered_data = merged_data[(merged_data['quantity'] > 0) & (merged_data['price'] > 0)]

    # refactor quantity back to initial value
    filtered_data['quantity'] = filtered_data['quantity'].replace(11, '>10').astype(str)

    filtered_data.to_csv('result.csv', index=False, sep='\t')


if __name__ == '__main__':
    get_data_merged()
