def print_sum(n):
    sum = (n * (n+1)) / 2
    print (f"Sum of first {n} Natural numbers = {sum}")

def main():
    n = int(input("Enter n: "))
    print_sum(n)

main()