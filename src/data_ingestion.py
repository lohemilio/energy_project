import pandas as pd
from sqlalchemy import create_engine

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """
    Perform any necessary preprocessing on the data.
    """
    # Here you can perform any necessary preprocessing, such as handling missing values, converting data types, etc.
    # For example:
    # data['column'] = data['column'].astype(int)

    return data

def create_sqlite_database(data, db_file):
    """
    Create a SQLite database and load preprocessed data into it.
    """
    engine = create_engine(f'sqlite:///{db_file}')
    data.to_sql('energy_data', engine, index=False)

if __name__ == "__main__":
    # Path to the CSV file
    file_path = '../data/energy_dataset.csv'

    # Load data
    data = load_data(file_path)

    # Preprocess data
    preprocessed_data = preprocess_data(data)

    # Create SQLite database and load preprocessed data
    db_file = '../data/energy_forecast.db'
    create_sqlite_database(preprocessed_data, db_file)

    print("Data ingestion and preprocessing process completed.")
