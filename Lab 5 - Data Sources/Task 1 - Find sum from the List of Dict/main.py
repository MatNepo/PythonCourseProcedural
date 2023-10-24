import json

FILENAME = "input.json"


def task() -> float:
    """The function finds the sum of products from a list of dictionaries"""
    reader = json.load(open(FILENAME, 'r'))  # read the file
    total_sum = sum(item.get("score", 0.0) * item.get("weight", 1) for item in reader)  # summarise results from reader
    return round(total_sum, 3)  # Round the result to 3 decimal places


if __name__ == '__main__':
    print(task())
