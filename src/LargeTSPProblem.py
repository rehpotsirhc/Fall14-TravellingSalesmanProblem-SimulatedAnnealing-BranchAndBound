__author__ = 'Chris Johnson'

import CompleteSolution
import basictourstuff
import visualization
import cooling
import operators
import sys

def read_in_cities(file_name):
    cities = []

    with open(file_name) as openfileobject:
        for line in openfileobject:
            if not line.isspace():
                sections = line.strip().split()
                city = basictourstuff.City(float(sections[1]), float(sections[2]))
                cities.append(city)
    return cities



def actual_optimal_solution(file_name):
    return basictourstuff.E(read_in_cities(file_name))


best_tour_cost = 0
perm_count = 0
best_tour = []

def large_tsp_problem(file_name, T, cooling_func, operator_func, max_bad_move, visualize=False):
    file_name = file_name
    cities = read_in_cities(file_name)
    cs = CompleteSolution.CompleteSolution()
    cs.hill_climber(cities, T, cooling_func, operator_func, max_bad_move, -1, visualize, True)
    global best_tour
    global best_tour_cost
    global perm_count
    best_tour_cost = cs.best_tour_cost
    perm_count = cs.permutation_count
    best_tour = cs.best_tour




#run the hill climber x number of times and return the best tour found
def iterate_tsp_problems(x):
    global best_tour
    global best_tour_cost
    global perm_count
    best_tour_so_far_cost = sys.float_info.max
    best_tour_so_far = []
    perm_count_so_far = 0
    for i in range(x):
        large_tsp_problem("tsp225.txt", 300, cooling.cooling60, operators.reverse_random_subsequence2, 200)
        if best_tour_cost < best_tour_so_far_cost:
            best_tour_so_far_cost = best_tour_cost
            best_tour_so_far = best_tour
            perm_count_so_far = perm_count

    best_tour_cost = best_tour_so_far_cost
    best_tour = best_tour_so_far
    perm_count = perm_count_so_far



#print actual_optimal_solution("tsp225.txt")


#no visualization
#large_tsp_problem("tsp225.txt", 300, cooling.cooling60, operators.reverse_random_subsequence2, 200)

#run this version to visualize each new best tour as its found
#large_tsp_problem("tsp225.txt", 300, cooling.cooling60, operators.reverse_random_subsequence2, 200, True)


#this runs the hill climber as many times as you tell it to and keeps track of the best tour it can find
iterate_tsp_problems(50)

#this is the cost of the best tour that was found
print best_tour_cost
#the number of permutations of cities it ran through
print perm_count

#this line will display the best tour found
visualization.plot_tour_stay(best_tour)







