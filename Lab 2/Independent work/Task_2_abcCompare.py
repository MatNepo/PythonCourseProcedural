a = 73
b = 10
c = 55

condition_1 = a < 45 < min(b, c)  # only 1st numer < 45
condition_2 = b < 45 < min(a, c)  # only 2nd numer < 45
condition_3 = c < 45 < min(a, b)  # only 3rd numer < 45

if condition_1 or condition_2 or condition_3:
    print("Одно из чисел меньше 45")
