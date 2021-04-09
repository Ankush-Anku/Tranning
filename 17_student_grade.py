marks_1 = int(input("Enter marks1: "))
marks_2 = int(input("Enter marks2: "))
marks_3 = int(input("Enter marks3: "))
THRESHOLD = 40
total = marks_1 + marks_2 + marks_3
avg = total / 3

print ("=============")
print("===Report====")
print("marks_1  :" + str(marks_1))
print("marks_2  :" + str(marks_2))
print("marks_3  :" + str(marks_3))
print("Total     : " + str(total))
print("Percentage:" + str(avg))

if marks_1 >= THRESHOLD and marks_2 >= THRESHOLD and marks_3 >= THRESHOLD:
    print ("Status  :Passed")
else:
    print ("Status  :Failed")