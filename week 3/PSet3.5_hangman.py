__author__ = 'ryan@barnett.io'

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    #correct_letters = []
    guessed_word = []
    for length in secretWord:
        guessed_word.append('_ ')
    for letter in lettersGuessed:
        if letter in secretWord:
            #correct_letters.append(letter)
            letter_occurrence = secretWord.count(letter)
            next_index = 0
            for num_times in range(letter_occurrence):
                current_index = secretWord.find(letter, next_index)
                guessed_word[current_index] = letter
                next_index = current_index+1
    return ''.join(guessed_word)
    # for c in secretWord:
    #     print c
    #     if c not in correct_letters:
    #         return False
    # return True


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
    # FILL IN YOUR CODE HERE...

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %s letters long.' % len(secretWord)
    print '-------------'
    num_guesses = 8
    lettersGuessed = []
    while num_guesses > 0:
        print 'You have %s guesses left.' % num_guesses
        print 'Available letters:', getAvailableLetters(lettersGuessed)
        letterGuessed = raw_input('Please guess a letter: ')
        if letterGuessed in secretWord and letterGuessed not in lettersGuessed:
            lettersGuessed.append(letterGuessed.lower())
            print 'Good guess:', getGuessedWord(secretWord, lettersGuessed)
        elif letterGuessed in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed)
        elif letterGuessed not in secretWord and letterGuessed not in lettersGuessed:
            num_guesses -= 1
            lettersGuessed.append(letterGuessed.lower())
            print 'Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed)
        print '-------------'
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            return 'Congratulations, you won!'
    return 'Sorry, you ran out of guesses. The word was %s.' % secretWord


print hangman('apple')
