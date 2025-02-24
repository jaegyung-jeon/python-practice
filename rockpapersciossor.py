from traceback import print_tb
# test something here.....
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
import random
user_of_rcp=[rock,paper,scissors]
user_input_number=int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors\n"))
print(user_of_rcp[user_input_number])


print("computer chose:")

computer_type_of_rcp=[rock,paper,scissors]
random_number=random.randint(0,2)
print(computer_type_of_rcp[random_number])

win_draw_lose=[0,1,2]
if win_draw_lose[user_input_number-1]==random_number:
    print("fuck you win")
elif user_input_number==random_number:
    print("draw")
else:
    print("fuck man you are loseerrrrr!!!!")