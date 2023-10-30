import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    """Function is reading JSON file and creates the corresponding CSV file"""
    data = []  # Create empty list to save data

    # Read the input file
    with open(INPUT_FILENAME, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=',', quotechar='\n')

        # Add new row to the list data[]
        for row in csv_reader:
            data.append(row)

    # Write data to the output file
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
