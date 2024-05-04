your_wallet = 100000
#your_wallet = 32000
#your_wallet = 78500
course_price = 75000
# Введите ваше решение ниже
if your_wallet >= course_price:
    your_wallet = your_wallet - course_price
    if your_wallet < 5000:
        your_wallet = your_wallet + 1000
        print("Сделана скидка")
        print("Курс успешно приобретён!")
else:
    print ("Не хватает денег на счету")
print("Остаток на счету:", your_wallet)
print("Хорошего дня!")