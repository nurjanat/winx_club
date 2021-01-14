def delete(str1):
    if "help" in str1 or "asap" in str1 or "urgent" in str1:
        print("stiven")
    elif str1.endswith("!!!") and str1.isupper():
        print("stiven")
    else:
        print("ok")
delete(input())



