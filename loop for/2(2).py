# a = 4
# b = 7
# while a <= b :
#     i = 0
#     a *= 3
#     b *= 2
#     print(i)


# a = int(input())
# b = int(input())
# count_years = 0
# if 1 <= a <= b <= 10:
#     while a <= b:
#         a = a * 3
#         b = b * 2
#         count_years += 1
# print(count_years)


# split only for str


numbers = list(map(int,input().split()))
a = numbers[0]
b = numbers[1]
count_years = 0
if 1 <= a <= b <= 10:
    while a <= b:
        a = a * 3
        b = b * 2
        count_years += 1
    print(count_years)
list(int(input()))