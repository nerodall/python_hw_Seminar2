# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.


n = int(input("Введите число: "))

result = 1
while result < n:
    print (result)
    result = result * 2
