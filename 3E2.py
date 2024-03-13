for x in range(1,41):
    if x == 13:
        continue
    if x%5 == 0:
        if x%7 == 0:
            print(x," is divided by 5 and 7")
        else:
            print(x," is divided by 5")
    elif x%7==0:
        print(x," is divided by 7")
    else:
        print(x," is not important")

x = 1
while x <= 40:
    if x == 13:
        x += 1
        continue
    if x%5 == 0:
        if x%7 == 0:
            print(x," is divided by 5 and 7")
        else:
            print(x," is divided by 5")
    elif x%7==0:
        print(x," is divided by 7")
    else:
        print(x," is not important")
    x += 1
    continue
