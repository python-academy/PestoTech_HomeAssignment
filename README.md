# AdvertiseX Data Engineering Solution

## Overview

This repository contains the code and scripts for implementing a data engineering solution for AdvertiseX, a digital advertising technology company. The solution includes data ingestion, processing, storage, and optimization components to handle and analyze ad campaign data efficiently.

## Components

### 1. Data Ingestion (`data_ingestion.py`)

- Python script for ingesting ad impressions, clicks/conversions, and bid requests data from JSON, CSV, and Avro files.
- Uses libraries like `json`, `csv`, and `avro-python3` for handling different data formats.

### 2. Data Processing (`data_processing.py`)

- Python script for transforming ad campaign data, including standardization, enrichment, validation, filtering, and deduplication.
- Provides functions for processing impressions, clicks/conversions, and bid requests data.

### 3. Database Schema Definition (`create_tables.sql`)

- SQL script to define the schema of Snowflake database tables for impressions, clicks/conversions, and bid requests.
- Includes partitioning specifications for time-based partitioning of data.

### 4. Data Loading (`load_data.py`)

- Python script to load sample data into Snowflake database tables.
- Uses Snowflake's Python connector to connect to the database and load data from JSON, CSV, and Avro files.

## Usage

1. **Clone Repository**: Clone this repository to your local machine using Git.

2. **Set Up Snowflake**: Ensure you have access to a Snowflake account and create a database for AdvertiseX.

3. **Run Scripts**: Execute the Python scripts (`data_ingestion.py`, `data_processing.py`, `load_data.py`) and SQL script (`create_tables.sql`) in your Snowflake environment.

4. **Follow Documentation**: Refer to the documentation provided in each script and SQL file for detailed instructions on usage and configuration.

## Contributions

Contributions to improve or extend this data engineering solution are welcome! If you encounter any issues or have suggestions for enhancements, please open an issue or submit a pull request.
