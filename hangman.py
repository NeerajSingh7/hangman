import random


# function to take input
def bandekainput():
    valid_letter = 'abcdefghijklmnopqrstuvwxyz'
    letter = input("Guess the word and save man:")
    if letter in valid_letter:
        letter = letter
    else:
        print("Wrong input:")
        bandekainput()
    return letter


# function to display the fill in the blanks
def display():
    print(blanks)
    print()
    return


# function to form the man
def manformation(chances):
    if chances == 9:
        print("-------")
    elif chances == 8:
        print("-------")
        print("   o   ")
    elif chances == 7:
        print("-------")
        print("   o   ")
        print("   |   ")
    elif chances == 6:
        print("-------")
        print("   o   ")
        print("   |   ")
        print("  /    ")
    elif chances == 5:
        print("-------")
        print("   o   ")
        print("   |   ")
        print("  / \  ")
    elif chances == 4:
        print("-------")
        print("  \o   ")
        print("   |   ")
        print("  / \  ")
    elif chances == 3:
        print("-------")
        print("  \o/  ")
        print("   |   ")
        print("  / \  ")
    elif chances == 2:
        print("-------")
        print("  \o/| ")
        print("   |   ")
        print("  / \  ")
    elif chances == 1:
        print("-------")
        print("  \o/_|")
        print("   |   ")
        print("  / \  ")
    elif chances == 0:
        print("-------")
        print("   o_| ")
        print("  /|\  ")
        print("  / \  ")

    return
        



blanks = ['_','_','_','_','_','_']
# print(blanks)

name = input("Enter your name:")
print("Welcome ",name)
print("-------------------")
print("Try to guess the words in less than 10 guesses")
print()

word = random.choice(["red","blue","pink","brown","silver","green","orange","violet","black","golden"])
chances = 10

number = len(word)
print(blanks[0:number])
blanks = blanks[0:number]

#print(word)

while chances>0:
    if "_" in blanks:
        letter = bandekainput()
        if letter in word:
            index = word.find(letter)
            blanks[index] = letter
            display()
        else:
            print("it is not in word")
            chances=chances-1
            display()
            manformation(chances)
            
        print("the remaining chances are:",chances)
    else:
        break

if "_" in blanks:
    print("You Lose! You murdered a kind person.")
else:
    print("You Won! You have guessed right in ",10-chances," chances")


 

