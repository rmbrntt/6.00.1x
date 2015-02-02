__author__ = 'ryan@barnett.io'
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    count = 0
    result = ()
    for item in aTup:
        count += 1
        if count % 2 != 0:
            result += (item,)
    return result


toop = ('I', 'am', 'a', 'test', 'tuple')

print oddTuples(toop)

print sum(range(10, 3, -1))