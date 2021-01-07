def guess_number():
    import random
    number1 = random.randint(1,10)
    print(number1)
    tries = 0
    while tries < 5:
        check = int(input("введите цифру"))
        if check > number1:
            print(">")
        elif number1 < check:
            print("<")
        elif number1 == check:
            print("lucky")
            break
        tries += 1
    if tries == 5:
        print("game over")

guess_number()
