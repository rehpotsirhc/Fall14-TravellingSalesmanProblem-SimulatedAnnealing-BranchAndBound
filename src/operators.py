__author__ = 'Chris Johnson'

import random

#operators

#swap the two specified cities
def swap(tour, a, z):

    #keep the passed tour parameter intact
    tourtmp = tour[:]

    length = len(tourtmp)

    if a < length and z < length:
        tmp = tourtmp[a]
        tourtmp[a] = tourtmp[z]
        tourtmp[z] = tmp

    return tourtmp

#swap two random cities
def swap_random(tour):

    length = len(tour)
    first = random.randint(0, length - 1)
    second = random.randint(0, length - 1)

    return swap(tour, first, second)

#swap two random cities X times
def swap_random_xtimes(tour, x):
    for i in range(0, x):
        tour = swap_random(tour)

    return tour

def swap_random_50times(tour):
    return swap_random_xtimes(tour, 50)

def swap_random_10times(tour):
    return swap_random_xtimes(tour, 10)


def swap_random_5times(tour):
    return swap_random_xtimes(tour, 5)


def reverse_random_subsequence2(tour):
    return reverse_random_subsequence(tour, len(tour))


#reverse a subsequence
def reverse_random_subsequence(tour, seqlimit):

    length = len(tour)
    start = random.randint(0, length - 2)
    upperend = start + seqlimit

    if upperend > (length - 1):
        upperend = length - 1

    end = random.randint(start + 1, upperend)

    front = start
    back = end

    while front < back:
        tour = swap(tour, front, back)
        front += 1
        back -= 1

    return tour



