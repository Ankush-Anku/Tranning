a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a<b:
    if a<c:
        if a<d:
            print(f"min = {a}")
        else:
            print(f"min = {d}")
    else:
        if c<d:
            print(f"min = {c}")
        else:
            print(f"min = {d}")
else:
    if b<c:
        if b<d:
           print(f"min = {b}")
        else:
           print(f"min = {d}")
    else:
        if c<d:
            print(f"min = {c}")
        else:
            print(f"min = {d}")