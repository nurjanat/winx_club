# w = int(input())
# if 2 <= w <= 100:
#     if w % 2 == 0:
#         print('yes')
#     else:
#         print("no")


str1 = input()
if len(str1) > 10:
    len_str = len(str1) - 2
    print(str1[0]+str(len_str)+str1[-1])
else:
    print(str1)



