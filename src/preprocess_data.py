import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def open_file(file_path):
    try:
        data = pd.read_csv(file_path, encoding='ISO-8859-1')
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def fill_desc_nulls(data):
    # Create a dictionary of StockCode and Description from rows where Description is not null
    valid_desc_map = data.dropna(subset=['Description']).drop_duplicates('StockCode').set_index('StockCode')['Description']

    # Fill missing descriptions by mapping the StockCode to the valid descriptions
    data['Description'] = data['Description'].fillna(data['StockCode'].map(valid_desc_map))
    data['Description'] = data['Description'].fillna('No Description')


def fill_customer_nulls(data):
    # Fill missing CustomerID values with 0
    data['CustomerID'] = data['CustomerID'].fillna(0)


def basic_cleaning(data):
    # Remove duplicates
    data = data.drop_duplicates()
    data.reset_index(drop=True, inplace=True)

    # Remove rows with InvoiceNo starting with 'C' (cancellations)
    data = data[~data['InvoiceNo'].str.startswith('C', na=False)]

    # Convert InvoiceDate to datetime
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    # Remove rows with non-positive Quantity or UnitPrice
    data = data[data['Quantity'] > 0]
    data = data[data['UnitPrice'] > 0]
    return data


def main():
    data_path = "..\\data\\online_retail.csv"
    data = open_file(data_path)
    if data is None:
        print("Data loading failed. Exiting.")
        return
    fill_desc_nulls(data)
    fill_customer_nulls(data)
    data = basic_cleaning(data)


if __name__ == "__main__":
    main()