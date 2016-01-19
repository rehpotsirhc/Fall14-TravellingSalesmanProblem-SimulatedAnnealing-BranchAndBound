# based on http://nbviewer.ipython.org/url/norvig.com/ipython/TSPv3.ipynb
import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools
import sys

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

#permutations
#define globals
best_distance_global = 0
best_tour_global = []
solution_count = 0

alltours = itertools.permutations
#algorithms
def exact_TSP(cities):
    "Generate all possible tours of the cities and choose the shortest one."
    all_tours = alltours(cities)
    return (list(shortest(all_tours)))

def shortest(tours):
    "Return the tour with the minimum total distance."
    return min(tours, key=total_distance)

#recursive on the way down solution
def all_down_TSB(cities):
    tour = all_down_TSP_helper(cities)
    return tour

def all_down_TSP_helper (cities, tour=[]):
    global solution_count
    solution_count+= 1
    if cities == []:
        return tour
    else:
        best_distance = sys.maxint
        for city in cities:
            this_cities = cities[:] #copy
            this_cities.remove(city) #remove
            this_tour = all_down_TSP_helper(this_cities, [city] + tour) #add on the way down
            this_total_distance = total_distance(this_tour)
            if (this_total_distance < best_distance):
                best_distance = this_total_distance
                best_tour = this_tour
        return best_tour

#incremental distance on the way down
def all_incremental_TSP (cities):
    #helper function to get the correct inputs and outputs
    tour,_ = all_incr_TSP_helper(cities[1:], tour=[cities[0]], dist_so_far=0)
    return tour

#return (best_tour, best_distance)
def all_incr_TSP_helper (cities, tour=[], dist_so_far=0):
    global solution_count
    solution_count+=1
    if cities == []: #return tour and distance so far + dist start to finish
        return (tour, dist_so_far + distance(tour[0], tour[-1]))
    else:
        best_distance = sys.maxint
        for city in cities:
            this_cities = cities[:] #copy
            this_cities.remove(city) #remove
            this_dist_so_far = dist_so_far + distance(tour[0], city)
            this_tour, this_total_distance = all_incr_TSP_helper(this_cities, [city] + tour, this_dist_so_far)
            if (this_total_distance < best_distance):
                best_distance = this_total_distance
                best_tour = this_tour
        return (best_tour, best_distance)

#incremental distance on the way down GLOBAL
def all_global_TSP (cities):
    global best_distance_global
    global best_tour_global
    #helper function to get the correct inputs and outputs
    best_distance_global = sys.maxint
    best_tour_global = []
    all_global_TSP_helper(cities[1:], tour=[cities[0]], dist_so_far=0)
    return best_tour_global

#return (best_tour, best_distance)
def all_global_TSP_helper (cities, tour=[], dist_so_far=0):
    global best_distance_global
    global best_tour_global
    global solution_count
    solution_count+= 1
    if cities == []:
        tour_distance = dist_so_far + distance(tour[0], tour[-1])
        if tour_distance < best_distance_global:
            best_distance_global = tour_distance
            best_tour_global = tour
    else:
        for city in cities:
            this_cities = cities[:] #copy
            this_cities.remove(city) #remove
            this_dist_so_far = dist_so_far + distance(tour[0], city)
            all_global_TSP_helper(this_cities, [city] + tour, this_dist_so_far)

#bounding
def all_bound_TSP (cities):
    global best_distance_global
    global best_tour_global
    #helper function to get the correct inputs and outputs
    best_distance_global = sys.maxint
    best_tour_global = []
    all_bound_TSP_helper (cities[1:], tour=[cities[0]], dist_so_far=0) #sets global varables
    return best_tour_global

#return nothing, just set globals
def all_bound_TSP_helper (cities, tour=[], dist_so_far=0):
    global best_distance_global
    global best_tour_global
    global solution_count
    solution_count+= 1
    if cities == []:
        tour_distance = dist_so_far + distance(tour[0], tour[-1])
        if tour_distance < best_distance_global:
            best_distance_global = tour_distance
            best_tour_global = tour
    else:
        for city in cities:
            this_cities = cities[:] #copy
            this_cities.remove(city) #remove
            this_dist_so_far = dist_so_far + distance(tour[0], city)
            # bound lower bound of solution so far exceeds upper bound on whole solution
            if this_dist_so_far >= best_distance_global:
                break
            all_bound_TSP_helper(this_cities, [city] + tour, this_dist_so_far)







#VISUALIZATION OF TOURS
def plot_tour(algorithm, cities, doPlot = False):
    "Apply a TSP algorithm to cities, and plot the resulting tour."
    # Find the solution and time how long it takes
    global solution_count
    solution_count = 0
    t0 = time.clock()
    tour = algorithm(cities)
    t1 = time.clock()
    print("{} tour; distance = {:10.1f}; time = {:6.3f} secs {:25s}; calls = {:8d}".format(
          len(tour), total_distance(tour), t1-t0, algorithm.__name__, solution_count))
    # Plot the tour as blue lines between blue circles, and the starting city as a red square.
    if doPlot:
        plotline(list(tour) + [tour[0]])
        plotline([tour[0]], 'rs')
        plt.show()


def plotline(points, style='bo-'):
    "Plot a list of points (complex numbers) in the 2-D plane."
    X, Y = XY(points)
    plt.plot(X, Y, style)

def XY(points):
    "Given a list of points, return two lists: X coordinates, and Y coordinates."
    return [p.real for p in points], [p.imag for p in points]

#cities15 = Cities(15)
#cities9 = Cities(9)
#cities4 = Cities(4)
#cities5 = Cities(5)

##tour = exact_TSP(cities4)
##tour = all_down_TSB_wtf(cities4)
##tour = all_incremental_TSP(cities4)
##tour = all_global_TSP(cities4)
##tour = all_bound_TSP(cities4)
#print tour
#plot_tour(exact_TSP, cities4, True)
#plot_tour(all_down_TSB_wtf, cities4, True)

#while True:
    #cities9 = Cities(9)
    #cities12 = Cities(12)
    #plot_tour(all_down_TSB, cities9)
    #plot_tour(all_incremental_TSP, cities9)
    #plot_tour(all_global_TSP, cities9)
    #plot_tour(all_bound_TSP, cities9)
    #plot_tour(all_greedy_bound_TSP, cities9)



