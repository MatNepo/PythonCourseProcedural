# Task_2: Financial airbag (opposite task to the 1st onw)

# Input data:
salary = 5000  # Financial airbag
spend = 6000
months = 10
increase = 0.03  # Monthly price rise
money_capital = 0

for this_month in range(months):
    if this_month > 0:
        spend *= (1 + increase)
    money_capital += spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.2f}")
