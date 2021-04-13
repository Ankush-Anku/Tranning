"""
declare alist of person names,
declare a list of wishes,

wish every person with all wishes

eg:
Name:Ankush,Arun
wishes:good morning,goog evening and goog night

out
good morning Ankush
good evening Ankush
good night Ankush
good morning Arun
good evening Arun
good night Arun
"""
def main():
  names=["Ankush","Arun","Varun","Ankit"]
  wishes=["Good Morning","Good evening","Good night"]
  wish(names,wishes)

def wish(names,wishes):
    for i in range(0,len(names),1):
      for j in range(0,len(wishes),1):
          print(f"{names[i]},{wishes[j]}")

main()


