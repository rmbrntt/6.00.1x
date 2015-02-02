__author__ = 'barnett'
# def timesFive(a):
# return a * 5
#
# def applyToEach(L, f):
#     for i in range(len(L)):
#         print 'i',i
#         print 'f(l[i])',f(L[i])
#         L[i] = f(L[i])
#         print 'l[i]', L[i]
#
#
#
# testList = [1, -4, 8, -9]
#
# print applyToEach(testList, timesFive)
# print testList

# def applyEachTo(L, x):
#     result = []
#     for i in range(len(L)):
#         print L[i](x)
#         result.append(L[i](x))
#         print result
#     return result
#
# def square(a):
#     return a*a
#
# def halve(a):
#     return a/2
#
# def inc(a):
#     return a+1
#
# print applyEachTo([inc, square, halve, abs], -3)

#
# animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
# animals['d'] = 'donkey'
# print animals.has_key('b')
# print animals.values()
# del animals['b']
# print animals.values()


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand_copy = hand.copy()
    for letter in word:
        if letter in hand_copy and hand_copy[letter] > 0:
            hand_copy[letter] -= 1
    return hand_copy

print updateHand({'a': 1, 'i': 1, 'm': 1, 'l': 2, 'q': 1, 'u': 1}, 'quail')