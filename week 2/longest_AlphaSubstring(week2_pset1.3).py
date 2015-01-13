__author__ = 'ryan@barnett.io'
'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc'''

s = 'azcbobobegghakl'
#s = 'afjyiqtzaliyo'
alpha_capture = ''
longest_alpha = ''


for current_letter in s:
    if alpha_capture == '':
        alpha_capture = current_letter
        longest_alpha = alpha_capture
    elif alpha_capture[-1] <= current_letter:
        alpha_capture += current_letter
        if len(alpha_capture) > len(longest_alpha):
            longest_alpha = alpha_capture
    if alpha_capture[-1] > current_letter:
        alpha_capture = current_letter

print "Longest substring in alphabetical order is:", longest_alpha
