#задание 1
time = int(input("введите текущее время"))
while 10 <=time < 20:
    print("мы открыты")
    time = int(input("введите текущее время:"))
print("мы закрыты. часы работы с 10 до 24.")

#задание 2
promokode = int(input("Введите промокод:"))
while promokode != "life":
    print("этот промокод недейсвителен")
    promokode = int(input("Введите промокод:"))
print("промокод принят")            

#задание 3
promo = int(input("Введите промокод:"))
while promo != "life" and promo != "healt":
    print("этот промокод недейсвителен:")
    promo = int(input("Введите промокод:"))
print("промокод принят")

#задание 4
otzuv = input("введите ваш отзыв:")
while otzuv != "off":
    print("ваш отзыв принят")
    otzuv = input("введите ваш отзыв:")
print("работа завершена")

#задание 5
price = int(input("стоимость товара (0 - покупок больше нет):"))
total_price = 0
while price != 0:
    total_price += price
    price = int(input("стоимость товара (0 - покупок больше нет):"))
print("стоимость всех покупок:" total_price)

#задание 6
price = int(input("Введите стоимость (0 - закончить)"))
while price != 0:
    result = price * 0.9
    print("стоимость со скидкой", result)
    price = int(input("Введите стоимость (0 - закончить)"))
print("работа завершенна")

#задание 7
card = input("введите номер карты:")
attempts = 1
while attempts <= 3:
   print("поздравляю! вы получили скидку 10%")
   attempts += 1      
   card = input("введите номер карты:")
print("скидки закончились")

#задание 8
category = input("введите категорию (and - закончить):")
count = 0
while category != "and":
    count += 1
    category = input("введите категорию (and - закончить):")
print("всего категорий товаров:", count)

#задание 9
promo = input("введите промокод:")
attempt = 1
while promo != "fresh" and attempt < 3:
    attempt += 1
    promo = input("введите промокод:")
if promo == "fresh":
    print("принято с попытки номер", attempt)
else:
    print("попытки закончились") #душа требовала этого

# задание 10
category = input("введите категорию (stop - закончить)")
while category != "stop":
    if category == "мясные изделия":
        print("скидка 10%")
    elif category == "напитки":
        print("скидка 30%")
    else:
        print("скидки нет")
    category = input("введите категорию (stop - закончить)")    
