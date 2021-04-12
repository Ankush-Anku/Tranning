def print_multiplication(n):
    for i in range(1,5+1):
        print(f"{n}*{i}={n*i}")


def main():
    print("===== Multiplication Tables ====")
    print_multiplication(2)
    print("-----")
    print_multiplication(5)
    print("---")
    print_multiplication(10)

main()