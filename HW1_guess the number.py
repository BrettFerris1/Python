#Brett Ferris
#CSCI6672 - Python Programming
#September 12, 2014
#This program will guess what number you are thinking of between 1-100

name=input("Hi, what is your name?")
print("Hello",name,"! Let's play a game!")
print("Think of a random number from 1 to 100, and I'll try to guess it!")

more="yes"                                                                  
while (more == "yes"):
    low=1                                                                  
    high=100                                                                
    number=50                                                  
    count=0                                                                 
                                                                            
    answer=input("Is it "+str(number)+"?(yes/no)")
    count=count+1
    if answer=="yes":
        print("YAY, I guessed it in",count,"try")
        more=input("Do you want to play more? ")
        continue    
    greater=input("Is it greater than "+str(number)+"?(yes/no)")   
    while (answer != "yes"):                                                
 
           if greater == "yes": 
                   low=number+1                                               
                   number=(high+low)//2                    
           elif greater == "no":
                   high=number-1
                   number=(high+low)//2                      
 
           answer=input("Is it "+str(number)+"?(yes/no)")                   
           count=count+1                                                    
           if answer=="yes":                                                
               break
           greater=input("Is it greater than "+str(number)+"?(yes/no)")     
                
    print("YAY, I guessed it in",count,"tries")
    more=input("Do you want to play more? ")
print("BYE-BYE")
input("Press Enter to exit")

    
    

