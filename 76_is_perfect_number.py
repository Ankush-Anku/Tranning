n = int(input("Enter any number: "))

y = 0
for i in range(1, n):
    if(n % i == 0):
        y = y + i
if (y == n):
    print(f"{n} is a Perfect number!")
else:
    print(f"{n} is not a Perfect number!")      