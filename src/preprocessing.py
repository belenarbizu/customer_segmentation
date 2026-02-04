import pandas as pd


def open_file(file_path):
    try:
        data = pd.read_csv(file_path, encoding='ISO-8859-1')
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def basic_cleaning(data):
    # Remove duplicates
    data = data.drop_duplicates()
    data = data.dropna(subset=['CustomerID'])
    data.reset_index(drop=True, inplace=True)

    # Create a dictionary of StockCode and Description from rows where Description is not null
    valid_desc_map = data.dropna(subset=['Description']).drop_duplicates('StockCode').set_index('StockCode')['Description']

    # Fill missing descriptions by mapping the StockCode to the valid descriptions
    data['Description'] = data['Description'].fillna(data['StockCode'].map(valid_desc_map))
    data['Description'] = data['Description'].fillna('No Description')

    # Remove rows with InvoiceNo starting with 'C' (cancellations)
    data = data[~data['InvoiceNo'].str.startswith('C', na=False)]

    # Convert InvoiceDate to datetime
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    # Remove rows with non-positive Quantity or UnitPrice
    data = data[data['Quantity'] > 0]
    data = data[data['UnitPrice'] > 0]

    # Create TotalPrice column
    data['TotalPrice'] = data['Quantity'] * data['UnitPrice']
    return data


def build_rfm(data):
    rfm = (data.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (data['InvoiceDate'].max() - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).reset_index())

    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    return rfm
