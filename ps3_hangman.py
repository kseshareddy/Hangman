# Hangman game
#



import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    x=0
    for i in secretWord:
        if i in lettersGuessed:
            x+=1
    if len(secretWord)==x:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    x=''
    for i in secretWord:
        if i in lettersGuessed:
            x+=i
        else:
            x+='_ '
    return x



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    x=string.ascii_lowercase
    for i in lettersGuessed:
        if i in x:
            x=x.replace(i,'')
    return x
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    lettersGuessed=[]
    print('Welcome to tne game,Hangman!')
    print('I am thinking of a word that is ',len(secretWord),' letters long.')
    i=8
    while i>0:
        print('----------------')
        print('You have ',i,' guesses left.')
        print('Available letters:'+ getAvailableLetters(lettersGuessed))
        x=input('Please guess a letter:')
        x=x.lower()
        if x in secretWord and x not in lettersGuessed:
            lettersGuessed.append(x)
            print('Good guess:'+ getGuessedWord(secretWord,lettersGuessed))
            if isWordGuessed(secretWord,lettersGuessed):
                print(" ")
                print('Congratulations, you won!')
                break
            
        elif x in lettersGuessed:
            lettersGuessed.append(x)
            print("Oops!You've already guessed that letter:"+ getGuessedWord(secretWord,lettersGuessed))
        
        else:
            lettersGuessed.append(x)
            print("Oops!That letter is not in my word:" + getGuessedWord(secretWord,lettersGuessed))
            i-=1
    if i==0:
        print('Sorry,you ran out of guesses.The word was '+secretWord)
    
          





secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
