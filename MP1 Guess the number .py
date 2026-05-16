# PROJECT 1: Guess the number 
""" The program chooses a random integer between 1 and 100 and repeatedly 
prompts the user to guess it (or quit). For each input it checks the guess vs. 
the secret number and responds with "too small", "too big", or "Success: Correct Guess!"
when matched, then ends. When the user quits or the game ends it prints 
"----------GAME OVER----------".""" 
import random
 
target = random.randint(1, 100)

while True:
    userchoice = int(input("Guess the target number or Quit(Q):"))
    if(userchoice == "Q" or userchoice == "q"):
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success: Correct Guess!")
        break
    
    elif(userchoice < target):
        print("Your number was too small. Take a bigger guess!")
    else:
        print("Your number was too big. Take a smaller guess!")

print("----------GAME OVER----------")



