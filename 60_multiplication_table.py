def print_multiplication(n):
    i=1
    while(i<=10):
        print(f"{n}*{i}={n*i}")
        i=i+1

def main():
    print("===== Multiplication Tables ====")
    print_multiplication(2)
    print("-----")
    print_multiplication(5)
    print("---")
    print_multiplication(10)

main()