def get_reverse(n):
     i=n
     rev = 0
   
     while i>0:
       rem = i % 10
       rev = rev * 10 + rem
       i = i // 10
     return rev
def is_palindrome (n):
    return n == get_reverse(n)   

def main():
    print(f"5678<--> {get_reverse(5678)} ")
    print(f"5335<--> {get_reverse(5335)} ")


main()