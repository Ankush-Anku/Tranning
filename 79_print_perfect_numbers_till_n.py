def is_perfect_number(n):
    i = 1
    y = 0
    while i < n:
        if(n % i==0):
           y = y+i

        i=i+1
    return n == y


def main():
    i = 1
    while i <= 10:
        if is_perfect_number(i):
            print(i)
        i = i + 1


main()