__author__ = 'Chris Johnson'
import random

import basictourstuff

import visualization
import sys



class CompleteSolution:


    def __init__(self):
        self.reset()

    def reset(self):
        self.permutation_count = 0
        self.average_cost_bad_move = 0
        self.bad_move_costs = 0
        self.bad_move_count = 0
        self.best_tour = None
        self.best_tour_cost = 0
        self.bad_consecutive_move_attempts = 0




    #max_bad_consecutive_move_attempts and max_permutations_considered < 0 means unlimited
    #for this to terminate either
    #max_bad_consecutive_move_attempts OR max_permutations_considered must be >= 0
    def hill_climber(self, cities, T, cooling_func, operator_func, max_bad_consecutive_move_attempts, max_permutations_considered, visualize, shuffle):

        #set an upper limit to the number of bad consecutive move attempts
        if max_bad_consecutive_move_attempts < 0 and max_permutations_considered < 0:
            max_bad_consecutive_move_attempts = 5000


        near_zero = sys.float_info.min * (1 + sys.float_info.min)

        if shuffle:
            random.shuffle(cities)

        current_tour = cities[:]
        current_tour_cost = basictourstuff.E(current_tour)

        self.best_tour = cities[:]
        self.best_tour_cost = current_tour_cost



        while (self.bad_consecutive_move_attempts <= max_bad_consecutive_move_attempts or max_bad_consecutive_move_attempts < 0) and (self.permutation_count <= max_permutations_considered or max_permutations_considered < 0):

            self.permutation_count += 1

            if T > 0:
                T = cooling_func(T, self.permutation_count)

            next_tour = operator_func(current_tour)
            next_tour_cost = basictourstuff.E(next_tour)

            if next_tour_cost < self.best_tour_cost:
                self.bad_consecutive_move_attempts = 0
                self.best_tour = next_tour
                self.best_tour_cost = next_tour_cost
                if visualize:
                    visualization.plot_tour(self.best_tour)


            if next_tour_cost < current_tour_cost:
                current_tour = next_tour
                current_tour_cost = next_tour_cost

            else:
                if basictourstuff.accept_with_prob(basictourstuff.prob(T, current_tour_cost, next_tour_cost)):
                    self.bad_move_costs += (current_tour_cost - next_tour_cost) #this should be negative
                    self.bad_move_count += 1
                    current_tour = next_tour
                    current_tour_cost = next_tour_cost

                if T < near_zero:
                    self.bad_consecutive_move_attempts += 1


        if self.bad_move_count > 0:
            self.average_cost_bad_move = (self.bad_move_costs / self.bad_move_count)
        else:
            self.average_cost_bad_move = 0

        return self.best_tour











#cities = basictourstuff.Cities(13)




#bbtour = tsp_start_code_no_greedy.all_bound_TSP(cities)

#print "ACTUAL BEST:"
#opttourcost = basictourstuff.total_distance(bbtour)
#print opttourcost
#matchCount = 0
# print "\n\n"
# for i in range(0, 50):
#     cs = CompleteSolution()
#     cs.hill_climber(cities, 1000, cooling.cooling90, operators.reverse_random_subsequence2, -1, -1, False)
#     tourcost = cs.best_tour_cost
#     print "TOUR COST: " +str(tourcost)
#     print "AVG BAD MOVE COST: " + str(cs.average_cost_bad_move)
#     print "BAD MOVE COST: " + str(cs.bad_move_costs)
#     print "BAD MOVE COUNT: " + str(cs.bad_move_count)
#     print "PERM COUNT: " + str(cs.permutation_count)
#     print "BAD CONS MOVE ATTEMPTS: " + str(cs.bad_consecutive_move_attempts)
    # if opttourcost is tourcost:
    #     matchCount += 1
    #     print "!!!!MATCH!!!  " + str(matchCount)
