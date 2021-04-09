a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a>b:
    if a >c:
        if a>d:
           print(f"max = {a}")
        else:
           print(f"max = {d}")
    else:
        if c>d:
           print(f"max = {c}")
        else:
           print(f"max = {d}")
else:
    if b>c:
        if b>d:
            print(f"max = {b}")
        else:
            print(f"max = {d}")
    else:
        if c>d:
            print(f"max = {c}")
        else:
            print(f"max = {d}")



