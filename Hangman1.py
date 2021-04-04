import random

WrongChoiceList = []
ExitGame = False
CorrectChoices = {}

WordList = ["Apple", "Symbol", "Birmingham", "Leaping", "Volcano", "Chess", "Bike", "Intersection", "Calculator", "Redwood"]
SelectedWord = random.choice(WordList)

CharacterDict = {}

indexcount = 0
for character in SelectedWord:   
    IndexList = [indexcount]
    if character not in CharacterDict.keys():    
        CharacterDict[character.lower()] = IndexList
    else:
        CharacterDict[character.lower()].append(indexcount)
    indexcount += 1

def CreateUnderscoredWord(EmptyWord):    # creates the blank word, like "_ _ _ _ _ ", or "_ _ a _ _"
    for c in CorrectChoices:    
        for index in CorrectChoices[c]:
            index = index * 2        
            EmptyWord = EmptyWord[:index] + c + EmptyWord[index + 1:]  # this replaces the ud          
    print(EmptyWord)

def get_input():
    RemainingLetters = len(SelectedWord)
    AttemptsLeft = len(SelectedWord) + 7

    EmptyWord = ""
    for index in range(0, len(SelectedWord)):
        EmptyWord += "_ "

    not_guessed = True 
    while not_guessed:
        userInput = input("Enter a letter or 'Exit' if you want to end game: ")
        userInput = userInput.lower()
        if userInput != "exit":
            if len(userInput) == 1:
                if userInput in CharacterDict.keys():
                    LetterList = CharacterDict[userInput]
                    RemainingLetters = RemainingLetters - 1
                    print(f'{RemainingLetters} letters remaining')                    
                    CorrectChoices[userInput] = LetterList        
                else:
                    WrongChoiceList.append({userInput})
                    AttemptsLeft = AttemptsLeft - 1

                CreateUnderscoredWord(EmptyWord)

                if AttemptsLeft != 0 and RemainingLetters != 0:
                    print(f'WrongChoices: {WrongChoiceList}')
                    print(f'{AttemptsLeft} turns remaining')
                elif RemainingLetters == 0:
                    print("Congratulations. You win")
                    not_guessed = False
                else:
                    print("End of game. You Lose")
                    not_guessed = False
            else:
                if userInput == SelectedWord.lower():
                    print("Congratulations. You Win")
                    not_guessed = False
                else:
                    print("Incorrect")
                    AttemptsLeft -= 1
                    print(f'{AttemptsLeft} turns remaining')
            
        else:
            print("End of game.")
            not_guessed = False

print(SelectedWord)
# CreateUnderscoredWord()
get_input()