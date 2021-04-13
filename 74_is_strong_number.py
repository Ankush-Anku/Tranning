"""
Strong number is a special number whose sum of factorial of digits is equal to the original number.
for example: 145 is strong number.Since,1! + 4! + 5! =145
"""
def get_factorial(n):
    fact =1
    for i in range(n,0,-1):
        fact = fact *1
    return fact
def is_strong(n):
    i=n
    sum = 0
   
    while i>0:
       rem = i % 10
       sum += get_factorial(rem)
       i = i // 10
    return n ==sum
    return True

def main():
    print("IS strong number:")
    print(f'1-->{is_strong(1)}')
    print(f'2-->{is_strong(2)}')
    print(f'145-->{is_strong(145)}')
    print(f'146-->{is_strong(146)}')

main()