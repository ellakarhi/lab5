import random

def Game():
flag = True
while flag:
  number = input("Type a number for an upper bound: ")
  if number.isdigit():
    print("Let's begin!")
    number = int(number)
    flag = False
  else:
    print("Invalid input. Try again.")
    
number_wanted = random.randint(1,number)
guess = None


while guess != number_wanted:
  guess = (input("guess a number between 0 and " + str(number) + ": "))
  if guess.isdigit():
    guess = int(guess)
    
  if guess == number_wanted:
    print("you guess correctly!")
  else:
    print("Guess again.")

