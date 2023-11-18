import random

while(True):
 print("Type r to roll dice || e to exit")
 user_choice = input("enter your choice: ")
 if(user_choice == 'r'):
  dice_number = random.randint(1,6)
  print(dice_number)
 elif(user_choice == 'e'):
  break
