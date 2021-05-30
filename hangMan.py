import time 
import random

#welcoming the user
name = input("Whats your name? ")


#1 second wait
time.sleep(1)

difficulty = input("What difficulty would you like? ")


#----------------------------------------------------
#----------------------EASY--------------------------
#----------------------------------------------------

if difficulty == "Easy" or difficulty == "easy":

    print("Hello", name, "get ready to play hangman!")

    print(" ")

    time.sleep(1)

    print("Start guessing letters...")
    time.sleep(0.5)

    #here we set the secret words

    ewords = ("be","to","hello","piano","rock","question","yard","choose","tycoon","diagram","defend","gossip","topple","particle","concede","module","store")
    eword = random.choice(ewords)

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
        for char in eword:      

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
            print("\nYou won, The word was", eword)

        # exit the script
            break              

        print

        # ask the user go guess a character
        guess = input("\nguess a character:") 

        # set the players guess to guesses
        guesses += guess                    

        # if the guess is not found in the secret word
        if guess not in eword:  
 
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
                print("The word was",eword)

#----------------------------------------------------
#----------------------MEDIUM------------------------
#----------------------------------------------------

elif difficulty == "Medium" or difficulty == "medium":

    print("Hello", name, "get ready to play hangman!")

    print(" ")

    time.sleep(1)

    print("Start guessing letters...")
    time.sleep(0.5)

    #here we set the secret words

    mwords = ("permission","mechanical","collection","tradition","aluminium","notorious","emergency","horseshoe","biography","publisher","relevance","magnitude","orchestra")
    mword = random.choice(mwords)

    #creates an variable with an empty value
    mguesses = ''

    #determine the number of turns
    turns = 10

    # Create a while loop

    #check if the turns are more than zero
    while turns > 0:         

        # make a counter that starts with zero
        failed = 0             

        # for every character in secret word    
        for char in mword:      

        # see if the character is in the players guess
            if char in mguesses:    
    
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
            print("\nYou won, The word was", mword)

        # exit the script
            break              

        print

        # ask the user go guess a character
        mguess = input("\nguess a character:") 

        # set the players guess to guesses
        mguesses += mguess                    

        # if the guess is not found in the secret word
        if mguess not in mword:  
 
        # turns counter decreases with 1 (now 9)
            turns -= 1        
 
        # print wrong
            print("Wrong")    

        #prints the letters you guessed
            print("\nYou have guessed:",mguesses )
        # how many turns are left
            print("\nYou have", + turns, 'more guesses' )
 
        #   if the turns are equal to zero
            if turns == 0:           
    
         # print "You Lose"
                print("You Lose") 
                print("The word was",mword)

#----------------------------------------------------
#----------------------HARD--------------------------
#----------------------------------------------------

elif difficulty == "Hard" or difficulty == "hard":

    print("Hello", name, "get ready to play hangman! You are brave!")

    print(" ")

    time.sleep(1)

    print("Start guessing letters...")
    time.sleep(0.5)

    #here we set the secret words

    hwords = ("extraterrestrial","recommendation","discrimination","characteristic","discrimination","superintendent","disappointment","constitutional","comprehensive","concentration","identification")
    hword = random.choice(hwords)

    #creates an variable with an empty value
    hguesses = ''

    #determine the number of turns
    turns = 10

    # Create a while loop

    #check if the turns are more than zero
    while turns > 0:         

        # make a counter that starts with zero
        failed = 0             

        # for every character in secret word    
        for char in hword:      

        # see if the character is in the players guess
            if char in hguesses:    
    
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
            print("\nYou won, The word was", hword)

        # exit the script
            break              

        print

        # ask the user go guess a character
        hguess = input("\nguess a character:") 

        # set the players guess to guesses
        hguesses += hguess                    

        # if the guess is not found in the secret word
        if hguess not in hword:  
 
        # turns counter decreases with 1 (now 9)
            turns -= 1        
 
        # print wrong
            print("Wrong")    

        #prints the letters you guessed
            print("\nYou have guessed:",hguesses )
        # how many turns are left
            print("\nYou have", + turns, 'more guesses' )
 
        #   if the turns are equal to zero
            if turns == 0:           
    
         # print "You Lose"
                print("You Lose") 
                print("The word was",hword)

else:
    print("\033[1;31;40m (!) sorry", name,"That is not a diffulty.Try Easy, Medium or Hard (!) \n")