def guess_number(number):
    import random
    number1 = random.randint(1,10) + random.randint(1,10)
    check = input("введите цифру")
    if number1 == number:
        return "lucky"
    else:
        return "<",">"
print(guess_number(9))