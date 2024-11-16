import calculator

print("Вітаємо! Доступні операції: add, subtract, multiply, divide")
first = int(input("Введіть перше число: "))
second = int(input("Введіть друге число: "))

operation = input("Введіть операцію: ")

if operation == "add" :
    result = calculator.add(first, second)
elif operation == "subtract" :
    result = calculator.subtract(first, second)
elif operation == "multiply" :
    result = calculator.multiply(first, second)
elif operation == "divide" :
    result = calculator.divide(first, second)
else :
    print("Невірна операція")

print(f"Результат: {result}")
