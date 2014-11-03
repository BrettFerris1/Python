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
    pass
  answer=input(str(x)+"/"+str(y)+"=")
  try:
    int(answer)
  except ValueError:
    print("Please Enter Integers Only!")
    return
  if int(answer)==int(q):
    print("CORRECT!")
  else:
    print("INCORRECT!")
  return
print("INTEGER DIVISIONS\n")
again="yes"
while again == "yes":
  get_equation()
  again = input ("Do you want to play again?")
  
