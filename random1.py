import random

print("Welcome to Rock, Paper, Scissors! Let's play!")
print("You will play against the computer")
user_action = input("choose an action: 'rock', 'paper', or 'scissors': ").strip().lower()

possible_actions = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_actions)

print(f"\nYou chose: {user_action}")
print(f"The computer chose: {computer_action}")

if user_action == computer_action:
    print("It's a tie!")
elif (user_action == 'rock' and computer_action == 'scissors') or \
     (user_action == 'paper' and computer_action == 'rock') or \
     (user_action == 'scissors' and computer_action == 'paper'):
    print("You win!")
else:
    print("You lose!")
    
