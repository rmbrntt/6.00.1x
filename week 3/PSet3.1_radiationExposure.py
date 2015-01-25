__author__ = 'ryan@barnett.io'


def f(x):
    import math
    return 60*math.e**(math.log(0.5)/55.6 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    # first attempt below does not work for decimal use cases due to range limitation
    # total_exposure = 0
    # for num in [num * step for num in range(0, stop)]:
    #     print num
    #     if num >= start:
    #         total_exposure += f(num)
    # return total_exposure


    # second attempt scraps the first and goes for a while loop but is close to passing all use cases but fails
    # total_exposure = 0
    # current_year = 0
    # while float(current_year) < float(stop):
    #     print 'current yr',current_year
    #     if float(current_year) >= float(start) and float(current_year) <= float(stop):
    #         exposure = (f(current_year))*step
    #         current_year += step
    #         print 'total exposure',total_exposure
    #         total_exposure += exposure
    #     if float(current_year) < float(start):
    #         current_year += step
    #return total_exposure

    #third times a charm (after some research on stackoverflow) to find a clever way to iterate a range using floats
    def floatRange(x, y, step):
        while x < y:
            yield x
            x += step
    total_exposure = 0
    for x in floatRange(start, stop, step):
        exposure = (f(x) * step)
        total_exposure += exposure
    return total_exposure

print radiationExposure(0, 60, .5)


