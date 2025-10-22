import random
from art import logo
from game_data import data
print(logo)

score=0
def format_data(account_1):
    acc_name1=account_1["name"]
    acc_des=account_1["description"]
    acc_country=account_1['country']
    return f"{acc_name1},a {acc_des},from {acc_country}"
#func to check guess
def check_guess(guess,account1followers,account2followers):
    if account1followers > account2followers:
        return guess=="a"
    else:
        return guess=="b"
play=True
account_2=random.choice(data)
while(play):
    #choose 2 accounts randomly from dataset
    account_1=account_2
    account_2=random.choice(data)
    if account_1==account_2:
        account_2 = random.choice(data)

    print(f"Compare A:{format_data(account_1)}")
    print("vs")
    print(f"Compare B:{format_data(account_2)}")
    #ask user's guess
    guess=input("Make a guess:").lower()
    #clear the screen
    print('\n'*20)
    print(logo)

    #Check user's guess
    account_1_cnt=account_1['follower_count']
    account_2_cnt=account_2['follower_count']
    is_correct=check_guess(guess,account_1_cnt,account_2_cnt)
    #give feedback to users
    if is_correct:
        score+=1
        print(f"You are correct!!, current score is {score}")
    else:
        print(f"Wrong guess, Final score is {score}")
        play=False
