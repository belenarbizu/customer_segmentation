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


def check_data(data):
    print(data.head())


def main():
    data_path = "..\\data\\online_retail.csv"
    data = open_file(data_path)
    if data is None:
        print("Data loading failed. Exiting.")
        return
    check_data(data)

if __name__ == "__main__":
    main()