__author__ = 'Chris Johnson'

import random
import math

#these methods are from tsp_start_code_no_greedy.py, provided by Dr. Flann

City = complex # Constructor for new cities, e.g. City(300, 400)

def total_distance(tour):
    "The total distance between each pair of consecutive cities in the tour."
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))

def distance(A, B):
    "The distance between two points."
    return abs(A - B)

def Cities(n):
    "Make a set of n cities, each with random coordinates."
    return [City(random.randrange(10, 890), random.randrange(10, 590)) for c in range(n)]



#cost function
def E(tour):
    return total_distance(tour)


def accept_with_prob(prob):
    r = random.uniform(0, 1)
    return r <= prob

def prob(t, e1, e2):

    if t > 0:
        x = (e1 - e2) / t
    else:
        return 0
    return math.exp(x)


def initialize_temp(average_cost_bad_move, initial_prob):
    return average_cost_bad_move / math.log(initial_prob)


