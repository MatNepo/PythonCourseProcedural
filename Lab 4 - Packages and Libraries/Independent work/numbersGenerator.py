from random import sample


def get_number() -> str:
    numbers = [str(i) for i in range(10)]
    while True:
        """Infinite cycle is needed to go through it until 1st character won't be 1-9 (not 0)"""
        number_str = ''.join(sample(numbers, k=3))
        if number_str[0] != '0':
            return number_str


print(get_number())
