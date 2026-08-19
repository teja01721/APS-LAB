import random
def birthday_problem(n):
  birthdays=[]
  for i in range(n):
     birthday=random.randint(1,365)
     if birthday == birthdays:
       return True
   
     birthdays.append(birthday)
  return False
n=int(input("Enter the number of peoples"))

t=500
matches=0


