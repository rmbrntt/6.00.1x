__author__ = 'barnett'
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 != 0:
        return base * recurPower(base, exp/2) * recurPower(base, exp/2)
    else:
        return base * recurPower(base, exp-1)


print recurPower(-4.52, 9)