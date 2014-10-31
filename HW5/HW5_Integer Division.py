from random import randrange

def get_equation():  
  while True:
    try:
      x=randrange(100)
      y=randrange(100)
      if int(x/y) == float(x/y):
        break
    except ZeroDivisionError:
      pass
  try:
    q=x/y
  except (ZeroDivisionError,ValueError):
    get_equation()
  answer=input(str(x)+"/"+str(y)+"=")
  try:
    int(answer)
  except ValueError:
    print("Please Enter Integers Only!")
    get_equation()
  if int(answer)==int(q):
    print("CORRECT!")
    get_equation()
  else:
    print("INCORRECT!")
    get_equation() 

print("INTEGER DIVISIONS\n")
get_equation()
  
