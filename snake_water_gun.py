#      ////////////////////// SNAKE WATER GUN GAME ///////////////////////////
import random 
def user():
  while True:
    user_=input("Enter your choice (snake/water/gun) : ").lower()
    if user_ in ["snake","water","gun"]:
     return user_
    else:
       print("Wrong input !! Again enter ")

def computer():
   computer_=['snake','water','gun']
   return random.choice(computer_)

user_input=user()
computer_input=computer()
print(f"Player 1 choice is : {user_input}")
print(f"Player 2 choice is : {computer_input}")

if(user_input==computer_input):
  print("Tie")
elif(user_input=='gun'and computer_input=='snake'):
  print("You Win")
elif(user_input=='water'and computer_input=='gun'):
  print("You Win")
elif(user_input=='snake'and computer_input=='water'):
  print("You Win")
elif(user_input=='gun'and computer_input=='water'):
  print("You Loose")
elif(user_input=='water'and computer_input=='snake'):
  print("You Loose")
elif(user_input=='snake'and computer_input=='gun'):
  print("You Loose")
