import random

def guess_number(number_wanted, top_range):
  guess = int(input("Guess a number between 0 and " + str(top_range) + ": "))

  if guess < number_wanted:
    print ("Your guess was too low, guess again.")
    guess_number(number_wanted, top_range)
  
  elif guess > number_wanted:
    print ("Your guess was too high, guess again.")
    guess_number(number_wanted, top_range)
  else:
    print ("You've guessed correctly!")
    play_again = input("Would you like to play again? (Yes or No): ")
    if(play_again == "Yes" or play_again == "YES" or play_again == "y" or play_again == "y" or play_again == "yes"):
      play_game()
    else:
      print ("Thanks for playing! Come back again soon!")
      
def play_game(): 
  """Runs the game and uses the function guess_number. top_range must be greater than 0 or a value error will occur."""
  
  top_range = int(input("Enter a number for the top range:  "))
  if (top_range < 1):
    raise ValueError("top_range must be greater than 0")
  #if (top_range < 1):
    #print("The top range must be greater than 0")
    #play_game()
    
  number_wanted = random.randint(0, top_range)
  guess_number(number_wanted, top_range)

play_game()