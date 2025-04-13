import random
print("Welcome to the Game!")
print("Enter 'Rock','Paper' and 'Scissors'")
print("Enter a Value: ")
val=input()
cc=["Rock","Paper","Scissors"]
comp=random.choice(cc)
print("Computer's Choice",comp)
if(comp==val):
    print("Tie. Try Again.")
elif(comp=="Rock" and val=="Scissors") or (comp=="Paper" and val=="Rock") or (comp=="Scissors" and val=="Paper"):
    print("Computer Won! Try Again.")
else:
    print("You Win!!!")
   