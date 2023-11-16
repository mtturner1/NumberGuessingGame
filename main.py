
import random

def generate_random_number(): 
    return random.randint (1,100) #If you need to adjust the range feel free to do so
  
def players_guess():
    return int (input("Player enter a guess"))

def give_the_player_feedback(random_correct_number, guess):
    if guess < random_correct_number: 
        return "Response is too low, please try again"
    elif guess > random_correct_number: 
        return "Response is too high, please try again"
    elif guess == random_correct_number:
     return "Response is correct!"

if __name__ == "__main__":
    players_guess() 
