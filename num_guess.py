
import random
easy_level=10
hard_level=5
def check_ans(ans,guess,turns):
    if ans>guess:
        print("Too low")
        return turns-1
    elif ans <guess:
        print("Too high")
        return turns-1
    else:
        print("You guessed it right :)",ans)

def difficulty():
    level=input('choose difficulty,type "easy" or "hard"').lower()
    if level=='easy':
        return easy_level
    else:
        return hard_level

def main():
    #print(logo)
    print("Welcome to number guessing game")
    print("I am thinking of a number between 1 and 100")
    num= random.randint(1,100)
    #print(f"correct answer is {num}")
    turns = difficulty()
    guess = 0
    while guess != num and turns >0:
        print(f"you have {turns} left")
        guess = int(input("make a guess"))
        turns = check_ans(num, guess, turns)

        if turns==0:
            print("you ran out of chances!!")
        elif guess!=num and turns>0:
            print("Guess again")

main()



