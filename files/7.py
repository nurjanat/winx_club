def guess_number(number):
    tries = 0
    import random
    number1 = random.randint(1,10) + random.randint(1,10)
    i = 0
    while tries < 5:
         check = input("введите цифру")
        if number1 == number:
            return "lucky"
        else:
            return "<",">"
print(guess_number(9))