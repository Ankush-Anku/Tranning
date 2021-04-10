a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a<b and a <c:
    print(f"min = {a}")
elif b<a and b <c:
    print (f"Min = {b}")
else:
     print(f"Min = {c}")