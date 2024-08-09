import pandas as pd
import logging
import json
import sqlite3

# lets load the configuration
with open('config.json') as config_file:
    config = json.load(config_file)

conn = sqlite3.connect(config['source_db'])


# Configure logging
logging.basicConfig(filename='etl_pipeline.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Step 1: Extract data from the source database
def extract_data():
    logging.info('Starting data extraction.')
    try:
        conn = sqlite3.connect('source.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employees')
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
        conn.close()
        logging.info('Data extraction successful.')
        return df
    except Exception as e:
        logging.error(f'Data extraction failed: {e}')
        raise

# Step 2: Transform the data (e.g., clean or modify it)
def transform_data(df):
    logging.info('Starting data transformation.')
    try:
        df['department'] = df['department'].str.capitalize()
        logging.info('Data transformation successful.')
        return df
    except Exception as e:
        logging.error(f'Data transformation failed: {e}')
        raise

# Step 3: Load the transformed data into the destination database
def load_data(df):
    logging.info('Starting data loading.')
    conn = sqlite3.connect('destination.db')
    try:
        cursor = conn.cursor()
        for index, row in df.iterrows():
            cursor.execute('''
            INSERT INTO employees (id, name, age, department) VALUES (?, ?, ?, ?)
            ''', (row['id'], row['name'], row['age'], row['department']))
        conn.commit()  # Commit the transaction
        logging.info('Data loading successful.')
    except Exception as e:
        conn.rollback()  # Roll back the transaction on error
        logging.error(f'Data loading failed and transaction rolled back: {e}')
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        data = extract_data()
        transformed_data = transform_data(data)
        load_data(transformed_data)
        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.critical(f'ETL pipeline failed: {e}')

def validate_migration():
    logging.info('Starting data validation.')
    try:
        source_conn = sqlite3.connect('source.db')
        dest_conn = sqlite3.connect('destination.db')
        source_cursor = source_conn.cursor()
        dest_cursor = dest_conn.cursor()

        # Example validation
        source_cursor.execute('SELECT COUNT(*) FROM employees')
        dest_cursor.execute('SELECT COUNT(*) FROM employees')
        source_count = source_cursor.fetchone()[0]
        dest_count = dest_cursor.fetchone()[0]

        if source_count == dest_count:
            logging.info('Validation successful: Row counts match.')
        else:
            logging.error(f'Validation failed: Row counts do not match (source: {source_count}, destination: {dest_count}).')


        source_conn.close()
        dest_conn.close()
    except Exception as e:
        logging.error(f'Data validation failed: {e}')
        raise

if __name__ == "__main__":
    try:
        data = extract_data()
        transformed_data = transform_data(data)
        load_data(transformed_data)
        validate_migration()  # Add this call after loading data
        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.critical(f'ETL pipeline failed: {e}')
