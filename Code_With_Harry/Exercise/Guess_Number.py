n=19
guess_initial_count=1

def computeNumberOfGuesses(n,guess_initial_count):
    while(guess_initial_count<=9):
        if n<19:
            print ("Entered number is small, please increment")
        elif n>19:
            print ("Entered number is higher, please decrement")
        else:
            print("You Won")
            print (guess_initial_count,"Guess Count")
            break
        print(9-guess_initial_count, "Guess Left")
        guess_initial_count+=1
    
    if(guess_initial_count>9):
        print ("Game Over")

computeNumberOfGuesses(19,9)
             

