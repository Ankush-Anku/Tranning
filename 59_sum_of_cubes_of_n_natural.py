def get_sum(n):
    sum= 0
    i=1
    while(i<=n):
        sum = sum + i*i*i
        i=i+1
    return sum


def main():
    n = int(input("Enter n:"))
    sum = get_sum(n)
    print(f"Sum of cube of {n} Natural numbers = {sum}")

main()