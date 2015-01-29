__author__ = 'ryan@barnett.io'
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    available_letters = []
    for letter in alphabet:
        if letter not in lettersGuessed:
            available_letters.append(letter)
    return ''.join(available_letters)


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)