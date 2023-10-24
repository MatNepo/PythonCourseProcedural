import os

OUTPUT_FILE = "output.csv"


def to_csv_file(filename: str, headers: list[str], rows: list[list[float]], delimiter=",", new_line="\n"):
    """The function writes data in CSV format without using the csv module"""
    # Open file for writing
    with open(filename, "w") as file:
        # Write headers
        file.write(delimiter.join(headers) + new_line)

        # Write data
        for row in rows:
            # May be needed if delimiter is a special character that might conflict with the CSV format
            formatted_row = [str(value).replace(delimiter, f'\\{delimiter}') for value in row]
            row_str = delimiter.join(formatted_row)
            file.write(row_str + new_line)


if __name__ == '__main__':

    headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
    data = [
        ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
        ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
        ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
        ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
    ]

    to_csv_file("output.csv", headers_list, data)  # call function to_csv_file()

    # Needed to check the task
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE) as output_f:
            for line in output_f:
                print(line, end="")
