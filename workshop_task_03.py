# Пропустила эту задачу на семинаре, поэтому вот.

# Вагоны в электричке пронумерованы
# натуральными числами, начиная с 1 (при этом иногда
# вагоны нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

num_from_head = int (input ("Введите порядковый номер вагона от головы поезда: "))
num_from_tail = int (input ("Введите номер, написанный на вагоне: "))

if (num_from_head == num_from_tail):
    print ("Этих данных недостаточно для вычисления длины поезда")
else:
    print (f"Поезд состоит из {num_from_tail + num_from_head - 1} вагонов")