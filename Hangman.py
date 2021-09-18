import random 

""" 
Hangman Game 

1) Create an array with random words: Japan, America, Switzerland, France, England, Spain, Italy 
and randomly select them. 

2) Find a way to end the loop if all the turns end and if the player gets all the words 

3) Enjoy yourself! :) 
""" 

civilizations = ["America","Switzerland","Spain","Russia","Canada"]

chosen_place = random.choice(civilizations) 

print("This is the random word chosen",chosen_place) 

turns = 10 

counter = 0

word_length = len(chosen_place)

victory = False 

while turns > 0: 
    
    letter = input("Enter a letter from the randomly chosen word ")
    
    if letter in chosen_place: 
        print("The letter",letter,"is in the word")
        print("Good, keep going")
        turns -= 1 
        counter += 1 
    else:
        print("Unfortunately, the letter",letter,"is not in the word")
        turns -= 1 
        
    if counter == word_length: 
        victory = True 
        break 
    
if victory == True:
    print("Congratulations, you got the randomly chosen word:",chosen_place)
else:
    print("You didn't get the randomly chosen word",chosen_place,". Better luck next time")
    

        
    






