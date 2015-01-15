__author__ = 'ryan@barnett.io'
'''Assume "s" is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl',
then your program should print

Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated
testing will provide a value of s for you - so the code you submit in the following box should assume s is already
defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem
set.'''

s = 'azcbobobegghakl'
bob = 'bob'
bob_count = 0
s_position = 0
for letter in s:
    check = s[s_position:s_position+3]
    if bob in check:
        bob_count += 1
    s_position += 1

print "Number of times bob occurs is:", bob_count