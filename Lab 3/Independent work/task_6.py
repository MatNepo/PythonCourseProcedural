ALLOW_SYMBOLS = ["0", "1"]  # Допустимые символы


def check_string(str_):
    return bool(str_) and set(str_) == set(ALLOW_SYMBOLS)


print(check_string("1010101010"))
print(check_string("101021231010103"))
print(check_string("asdawqe"))
print(check_string(""))
