import json
import csv
from avro.datafile import DataFileReader
from avro.io import DatumReader

def ingest_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def ingest_csv(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def ingest_avro(avro_file):
    data = []
    reader = DataFileReader(open(avro_file, "rb"), DatumReader())
    for record in reader:
        data.append(record)
    reader.close()
    return data

# Sample usage
if __name__ == "__main__":
    # Ingest sample data files
    json_data = ingest_json("sample_impressions.json")
    print("JSON Data:", json_data)

    csv_data = ingest_csv("sample_clicks_conversions.csv")
    print("CSV Data:", csv_data)

    avro_data = ingest_avro("sample_bid_requests.avro")
    print("Avro Data:", avro_data)
