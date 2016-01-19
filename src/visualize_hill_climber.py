__author__ = 'Chris Johnson'

import CompleteSolution
import cooling
import operators
import basictourstuff
import visualization
def visualize(problem_size, T, cool_func, operator):
        cs = CompleteSolution.CompleteSolution()
        cities = basictourstuff.Cities(problem_size)
        cs.hill_climber(cities, T, cool_func, operator, -1, -1, True, True)
        return cs.best_tour
        cs.reset()



best_tour = visualize(1000, 300, cooling.cooling60, operators.reverse_random_subsequence2)


#best_tour =visualize(50, 300, cooling.cooling60, operators.swap_random)

print "HILL CLIMBER FINISHED. DISPLAYING BEST TOUR FOUND"

#this line will display the best tour found
visualization.plot_tour_stay(best_tour)