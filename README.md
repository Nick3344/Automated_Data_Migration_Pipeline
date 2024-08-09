# Automated Data Migration Pipeline

This project is an automated data migration pipeline that extracts data from a source SQLite database, transforms it according to specified rules, and loads it into a destination SQLite database. The project includes enhancements such as logging, error handling, configuration management, and data validation to ensure robustness and flexibility.



## Features
- **ETL Pipeline**: Extract, Transform, and Load data between SQLite databases.
- **Logging**: Detailed logging of each step in the ETL process.
- **Error Handling**: Graceful handling of errors with transaction rollbacks.
- **Configuration Management**: External configuration file for database paths and logging settings.
- **Data Validation**: Validation checks to ensure successful data migration.


![Screenshot 2024-08-09 092603](https://github.com/user-attachments/assets/44f2c941-d614-4cbf-abc6-d571ca398a5b)

## Usage

1. **Create the source database with initial data:**
    ```bash
    python create_source_db.py
    ```

2. **Create the destination database:**
    ```bash
    python create_destination_db.py
    ```

3. **Run the ETL pipeline:**
    ```bash
    python etl_pipeline.py
    ```

4. **Check the logs for detailed information:**
    - Logs are written to `etl_pipeline.log` in the root directory.

## Configuration

This project uses a configuration file `config.json` to manage database paths and logging settings. Here's an example configuration:

```json
{
    "source_db": "source.db",
    "destination_db": "destination.db",
    "log_file": "etl_pipeline.log"
}
