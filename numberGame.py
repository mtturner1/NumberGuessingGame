def main():
    playAgain()

def playAgain(): 
    playAgain = input("do you want to play again? ")
    if playAgain == "yes" :
        print("Press play!")
    
    else:
        print("Bye!")
        
if __name__ == "__main__":
    main()