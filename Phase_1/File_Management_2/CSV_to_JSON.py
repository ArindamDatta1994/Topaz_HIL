import csv
import json

csv_file = "data.csv"
json_file = "data.json"

data = []

try:
    with open(csv_file, "r", encoding= "utf-8") as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            data.append(row)

    with open(json_file, "w", encoding= "utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print("Conversion completed successfully.")

except FileNotFoundError:
    print(f"Error: The file '{csv_file}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")