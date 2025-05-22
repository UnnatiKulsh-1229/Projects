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
images=[rock,paper,scissors]
import random
user_ch=int(input("0 for rock,1 for paper and 2 for scissors \n"))
print(images[user_ch])
sys_ch=random.randint(0,2)
print("Computer chose")
print(images[sys_ch])
if user_ch==0 and sys_ch==2:
    print('you win')
elif sys_ch>user_ch:
    print('you lose')
elif sys_ch==user_ch:
    print("Tie")
elif sys_ch==1 and user_ch==2:
    print("You win!")
elif sys_ch==0 and user_ch==2:
    print("System wins!")
elif user_ch==1 and sys_ch==0:
    print("you win !")
else:
    print("invalid")


