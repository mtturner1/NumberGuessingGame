import random
def main(): 
    rndm_nmbr_gm()
    

def rndm_nmbr_gm(): 
    return random.randint (1,100) #If you need to adjust the range feel free to do so
  
    return int (input("Player enter a guess"))
    
    if guess < random_correct_number: 
        return "Response is too low, please try again"
    elif guess > random_correct_number: 
        return "Response is too high, please try again"
    elif guess == random_correct_number:
     return "Response is correct!"

def playAgain(): 
    playAgain = input("do you want to play again? ")
    if playAgain == "yes" :
        print("Press play!")
    
    else:
        print("Bye!")
        
if __name__ == "__main__":
  main() 
   