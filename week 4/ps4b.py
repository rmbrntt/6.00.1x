from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    n = HAND_SIZE
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = ''
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score_check = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score_check > best_score:
                # Update your best score, and best word accordingly
                best_word = word
                best_score = score_check
    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "Current hand:",
        displayHand(hand)
        # Ask user for input
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word != '':
            total_score += getWordScore(word, n)
            print '"{0}" earned {1} points. Total: {2} points'.format(word, getWordScore(word, n), total_score)
            # Update the hand
            hand = updateHand(hand, word)
            if calculateHandlen(hand) == 0:
                print "Total score: {0} points.".format(total_score)
                print ''
                return
            print ''
        elif word == '':
            # End the game (break out of the loop)
            print "Total score: {0} points.".format(total_score)
            print ''
            return
        # Otherwise (the input is not a single period):
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    n = HAND_SIZE
    hand = {}
    while True:
        game_status = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print ''
        if game_status == 'r' and not hand:
            print 'You have not played a hand yet. Please play a new hand first!'
            print ''
        elif game_status == 'r' and hand:
            player_type = raw_input('Enter u to have yourself play, c to have the computer play: ')
            print ''
            if player_type == 'u':
                playHand(hand_copy, wordList, n)
            elif player_type == 'c':
                compPlayHand(hand, wordList, n)
            else:
                print "Invalid command."
        elif game_status == 'e':
            break
        elif game_status not in ['n', 'e', 'r']:
            print "Invalid command."
        else:
            player_type = raw_input('Enter u to have yourself play, c to have the computer play: ')
            print ''
            if player_type == 'u':
                if game_status == 'n':
                    hand = dealHand(n)
                    hand_copy = hand.copy()
                    playHand(hand, wordList, n)
            elif player_type == 'c':
                    hand = dealHand(n)
                    hand_copy = hand.copy()
                    compPlayHand(hand, wordList, n)
            else:
                print "Invalid command."

    return
        
#
# Build data structures used for entire session and play game
#
HAND_SIZE = 7
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


