from random import sample


def get_random_password(value: int = 8) -> str:
    """The function generates a random password of length n"""
    list_letters = [chr(ord('a') + i) for i in range(26)] + [chr(ord('A') + i) for i in range(26)]
    numbers = [str(i) for i in range(10)]
    characters = list_letters + numbers
    return ''.join(sample(characters, k=value))


print(get_random_password())
