# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int (input("Введите трёхзначное число: "))

digit3 = number % 10
temp = number//10

digit2 = temp % 10
digit1 = temp //10

print(f"Сумма цифр числа {number}  составляет {digit1} + {digit2} + {digit3} = {digit1 + digit2 + digit3}")

