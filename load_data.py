# load_data.py
import snowflake.connector

# Snowflake connection parameters
snowflake_user = 'your_username'
snowflake_password = 'your_password'
snowflake_account = 'your_account'
snowflake_database = 'your_database'
snowflake_schema = 'public'

# Sample data files
json_file = 'sample_impressions.json'
csv_file = 'sample_clicks_conversions.csv'
avro_file = 'sample_bid_requests.avro'

# Function to load data from JSON file into Snowflake table
def load_json_data(json_file, connection, cursor):
    with open(json_file, 'r') as file:
        data = file.read()
        cursor.execute(f"PUT 'file://{json_file}' @%{json_file}")
        cursor.execute(f"copy into impressions from @{json_file} file_format = (type = 'json')")

# Function to load data from CSV file into Snowflake table
def load_csv_data(csv_file, connection, cursor):
    cursor.execute(f"copy into clicks_conversions from 'file://{csv_file}' file_format = (type = 'csv')")

# Function to load data from Avro file into Snowflake table
def load_avro_data(avro_file, connection, cursor):
    cursor.execute(f"copy into bid_requests from 'file://{avro_file}' file_format = (type = 'avro')")

# Main function to connect to Snowflake and load data
def main():
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        database=snowflake_database,
        schema=snowflake_schema
    )
    cursor = conn.cursor()

    # Load data into Snowflake tables
    load_json_data(json_file, conn, cursor)
    load_csv_data(csv_file, conn, cursor)
    load_avro_data(avro_file, conn, cursor)

    # Close connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
