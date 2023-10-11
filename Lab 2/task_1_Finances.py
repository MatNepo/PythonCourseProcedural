# Task_1: Financial airbag

# Input data:
money_capital = 20000  # Financial airbag
salary = 5000
spend = 6000
increase = 0.05  # Monthly price rise
months = 1

while money_capital >= spend:
    money_capital += salary  # finances after salary
    if months > 1:  # skip monthly prise rise for the 1st month
        spend *= (1 + increase)
    money_capital -= spend
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
