list1 = [3000,900,1199]
x = 5000

result = sum(list1)
if x > result:
    result = x - result
    print(result)
else:
    print('not enough')

