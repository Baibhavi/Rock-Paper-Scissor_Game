rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
a = [rock, paper,scissors]
if choice>=3 or choice<0 :
  print("You entered invalid value. You loss!")
else:
 print(a[choice])

 computer_choice = random.randint(0,2)
 print(f"Computer chose {computer_choice}")
 print(a[computer_choice])


 if choice==0 and computer_choice==2  :
  print("You Win!") 
 elif choice ==2 and computer_choice == 0 :  
  print("You loss!")
 elif choice > computer_choice :     
  print("You Win!")
 elif choice < computer_choice :
  print("You Loss")
 elif choice == computer_choice:
  print("It's a Draw")  