# задание 1
zadacha = int(input("количество обязательных задач"))
dopzadacha = int(input("количество дополнительных задач"))
rezultat = zadacha * 15 + dopzadacha * 20
print("еффективность", rezultat)

# задание 2
otzuv = input ("введите отзыв:")
print("длинна отзыва", len(otzuv))
print("недостатки:", otzuv.lower().count("скучно"))
print("достоинства", otzuv.lower().count("круто"))

# задание 3
zp = float(input("среднемесячная зарплата:"))
hours = float(input("количество рабочих часов в выходные:"))
premia = zp * 0.01 * hours
print("премия", premia)

# задание 4
hours = int(input("количество рабочих часов в неделю (20 или 40):"))
price = int(input("стоимость одного часа:"))
summa = hours * 4 * price
print("зарплата в месяц:", summa)

# задание 7
m = int(input())
n = int(input())
if m == n:
    print(1)
else:
    print(0)

# задание 8
n = int(input())
m = int(input())
if m % n == 0:
    print(1)
else:
    print(0)

# задание 9
n = int(input())
m = int(input())
if n <= m:
    print(1)
else:
    print(0)

# задание 12
k = int(input("растояние:"))
d = int (input("километров в день:"))
finalyday = (k + d -1) // d
print(finalyday)

# задача 13
h = int(input("вывысота столба:"))
a = int(input("растояние пройденое за день:"))
b = int(input("растояние спуска за ночь"))
finalday = (h -a + (a - b) - 1) // (a - b) + 1
print(finalday)

# задача 14
pervya = int(input("результат первой команды"))
vtoraya = int(input("рузультат второй команды"))
if pervya > vtoraya:
    print(pervya)
else:
    print(vtoraya)
