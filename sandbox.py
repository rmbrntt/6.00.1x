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


aDict = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

aDict['d'] = ['donkey']
aDict['d'].append('dog')
aDict['d'].append('dingo')

aDict = {'a': [12, 11, 18, 11], 'c': [10, 13, 11, 17, 10], 'b': [20, 2, 14, 8, 0, 12, 17, 16, 9, 17]}
print aDict[(max(aDict))]

result_dict = {}
for k in aDict:
    result_dict[len(aDict[k])] = k
print result_dict[max(result_dict)]

