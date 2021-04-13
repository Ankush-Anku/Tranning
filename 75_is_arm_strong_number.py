"""
the sum of cubes of each digit is equal to the number itself. For example, 153 is an Armstrong number because
"""

n = int(input("Enter a number: "))

y= 0
i=n
while i > 0:
   x = i % 10  
   y = x*x*x + y 
   i= i // 10  

# display the result
if n == y:
   print(f"{n} is an Armstrong number")
else:
   print(f"{n} is not an Armstrong number")

   