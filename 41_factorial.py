def get_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def main():
    print(f"3! = {get_factorial(3)}")
    print(f"5! = {get_factorial(5)}")

main()