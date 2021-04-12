#Assignment

"""
Accept p,n and r
si = pnr/100
print si
"""

def print_interest(n,p,r):
    si = (p*n*r)/100
    print(f"Simple interest is = {si}")

def main():
    n = float(input("Enter n: "))
    p = float(input("Enter p: "))
    r = float(input("Enter r: "))
    print_interest(n ,p,r)

main()