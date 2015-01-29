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

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)

