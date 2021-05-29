import time
import random

#welcoming the user
name = input("What is your name? ")

print("Hello, " + name, "are you ready!!!")

print(" ")

#1 second wait
time.sleep(1)

print("Start guessing letters...")
time.sleep(0.5)

#here we set the secret words

words = ("pyhton","coding","recycle","dawn","vision","talkative","love","difficulty","late","bake","compact","old","employee","be","bubble","guess","home","urgency","buttocks","shop","fluctuation",
"snack","fling","structure","incentive","enemy","fastidious","overcharge","disagreement","consciousness","say","modernize","hostage","window","cake","demonstration","preoccupation",
"strikebreaker","consciousness","contradiction","entertainment","comprehensive")
word = random.choice(words)

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print(char, end =" ")    

        else:
    
        # if not found, print a dash
            print("_", end=" ")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print("\nYou won, The word was", word)

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = input("\nguess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print("Wrong")    

    #prints the letters you guessed
        print("\nYou have guessed:",guesses )
    # how many turns are left
        print("\nYou have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print("You Lose") 
            print("The word was",word)