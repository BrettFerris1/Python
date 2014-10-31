class Animal:
  def __init__(self,name):
    self.name=name
  def guess_who_am_i(self):
    if self.name=="elephant":
      self.hints=["I have exceptional memory","I am the largest land-living mammal in the world","I am grey"]
    if self.name=="tiger":
      self.hints=["I am the biggest cat","I come in black and white or orange and black","I like frosted flakes"]
    if self.name=="bat":
      self.hints=["I use echo-location","I can fly","I see well in the dark"]
    guess=""
    i=0
    print("\n\nI will give you three hints. Guess what animal I am..\n\n")
    while guess!=self.name:      
      print(self.hints[i])
      guess=input("Who am I?")
      i+=1
      if guess.lower()==self.name.lower():
        print("You got it! I am ", self.name)
        break
      elif i==3:
        print("I am out of hints! The answer is:",self.name)
        break
      else:
        print("Nope, try again!")
       


e=Animal("elephant")
t=Animal("tiger")
b=Animal("bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()

