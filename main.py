import random

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

# Rules: 0 beats 2, 1 beats 0, 2 beats 1
print("It's Rock, Paper, Scissors!") 
choices = [rock, paper, scissors]  
human = int(input("Make your Choice: Type 0 for Rock, 1 for Paper, and 2 Scissors. "))
machine = random.randint(0, 2)

# check for invalid choices
if human < 0 or human >= 3:
  print("Not a valid choice, You Lose!")
else:
  print(f"\n You chose {choices[human]} ")
  print(f" Computer chose {choices[machine]} ")

  # win or lose?
  if (human == 0 and machine == 2) or (human == 1 and machine == 0) or (human == 2 and machine == 1):
    print("You Win!")
  elif (human == 2 and machine == 0) or (human == 0 and machine == 1) or (human == 1 and machine == 2):
    print("You Lose!")
  elif human == machine:
    print("It's a Draw!")
