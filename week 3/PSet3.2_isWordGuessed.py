__author__ = 'ryan@barnett.io'
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    correct_letters = []
    for letter in lettersGuessed:
        if letter in secretWord:
            correct_letters.append(letter)
    for c in secretWord:
        if c not in correct_letters: return False;
    return True

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)