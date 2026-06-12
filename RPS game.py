import random
print("     ROCK PAPER SCISSOR    ")
user_score=0
computer_score=0
for round_no in range(1,6):
    print(f"Round no:{round_no}")
    print(" 0-rock \n 1-Paper \n 2-Scissor")
    user_choice=int(input(" It's your turn. Enter the number: "))
    l=(0,1,2)
    if user_choice not in [0,1,2]:
       print("Invalid choice")
       continue
    computer_choice=random.choice(l)
    print(f"Computer choice is {computer_choice}")
    if(computer_choice==user_choice):
        print("It's a draw. NO point")
    elif((computer_choice>user_choice) or (user_choice==2 and computer_choice==0)):
        print("You loose")
        computer_score+=1
    else:
        print("You won")
        user_score+=1
print("     FINAL SCORE     ")
print(f" User Score is:{user_score} \n Computer Score is:{computer_score} ")
if(user_score==computer_score):
    print("It's a draw")
elif(user_score>computer_score):
    print(f"You won by {user_score-computer_score}")
else:
    print(f"Computer won by {computer_score-user_score}")