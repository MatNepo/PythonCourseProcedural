import re


def remove_whitespace(input_string):
    cleaned_string = re.sub(r' +', ' ', input_string)
    return cleaned_string


str_with_space = """123.    test bks
print   test11"""
print(remove_whitespace(str_with_space))
