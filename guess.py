import random
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)

print(chosen_word)
#TODO1 create a place holder
place = ""
correct = []
for position in range(len(chosen_word)):
    place = place + "_"

    
print(place)


game_over = False
attempt =6
while attempt != 0:
    print(f"you have {attempt} attempts ")
    guess = input("Guess a letter:\n").lower()
    
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display = display + letter
            correct.append(guess)
            
        elif letter in correct:
            display = display + letter
            
        else:
            display = display + "_"
            
    print(display)
    
    if "_" not in display:
        game_over = True
        print("you win")
        
    attempt = attempt - 1
    


print("You lose")   
    