def get_sum(n):
    sum= 0
    for i in range(1,n+1):
        sum = sum + i*i*i

    return sum

def main():
    n = int(input("Enter n:"))
    sum = get_sum(n)
    print(f"Sum of cube of {n} Natural numbers = {sum}")

main()