# def save_princess(heads,tails,health):
#     hits = 0
#     while (heads > 0 or tails > 0) and health > 0:
        # if heads % 2 == 0 and heads > 0:
        #     heads -= 2
        # elif tails % 2 == 0 and tails > 0:
        #     if heads % 2 == 1:
        #         tails += 1
        # elif tails % 2 == 0:
        #     tails -= 2
        #     heads += 1
        # elif tails % 2 == 1:
        #     tails += 1
        # hits += 1
        # health -= 20
        # print(heads,tails,hits)

# save_princess(1,1,100)



def save_princess(heads,tails,health):
    hits = 0
    # while (heads > 0 or tails > 0) and health > 0:
    #     if heads == 1 and tails == 1:
    #         tails += 1
    #     elif tails % 2 == 0 and tails > 0:
    #         heads += 1
    #         tails -= 2
    #     elif heads % 2 == 0 and heads > 0:
    #         heads -= 2
    #     hits += 1
    #     health -= 20
    #     print(heads,tails,health)

save_princess(2,2,100)