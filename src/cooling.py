__author__ = 'Christopher'



def cooling(T, iteration_count, change_at, multiplier):

    if (iteration_count % change_at) == 0:
        return multiplier * T
    else:
        return T


def cooling90(T, iteration_count):
    return cooling(T, iteration_count, 200, .9)

def cooling80(T, iteration_count):
    return cooling(T, iteration_count, 200, .8)

def cooling60(T, iteration_count):
    return cooling(T, iteration_count, 200, .6)

def cooling40(T, iteration_count):
    return cooling(T, iteration_count, 200, .4)

def cooling20(T, iteration_count):
    return cooling(T, iteration_count, 200, .2)