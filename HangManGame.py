import random
import time
#Initial steps to invite in the game
print("Welcome to Hangman Game:->")
name=input("Enter your name")
print("Hello"+name+"!Best Of Luck")
time.sleep(2)
print("The game is about to start! Lets play Hangman")
time.sleep(3)
#Define the main function
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess=["january","border","image","film","promise","kids","lungs","doll",
    "rhyme","damage","plants"]
    word=random.choice(words_to_guess)
    length=len(word)
    count=0
    display=''*length
    already_guessed=[]
    play_game=""
#a loop to re-execute the game when the first round ends
def play_loop():
    global play_game
    play_game=input("Do you want to play the game again? y=yes,n=no")
    while play_game not in ["y","n","Y","N"]:
        play_game=input("Do you want to play again? y=yes,n=no")
        if play_game=="y":
            main()
        elif play_game=="n":
            print("Thanks for playing...We expect you back again")
            exit()
#initialising all the conditions for hangman game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit=5
    guess=input("This is the hangman word:"+display+"Enter your guess")
    guess=guess.strip()
    if(len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9"):
        print("Invalid input",Try a letter)
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+"_"+word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print(display+"")
    elif guess in already_guessed:
        print("Try another letter")
    else:
        count+=1
        if count==1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess."+str(limit-count)+"guesses remaining")
        elif count==2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess."+str(limit-count)+"guesses remaining")
        elif count==3:
            time.sleep(1)
            print("  _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess."+str(limit-count)+"guesses remaining")
        elif count==4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess."+str(limit-count)+"last guess remaining")
        elif count==5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess.You are hanged!!!")
            print("The word was:",already_guessed,word)
            play_loop()
        if word=='_'*length:
            print("Congrats,You have guessed the word correctly.")
            play_loop()

        elif count!=limit:
            hangman()
    main()
        hangman()
