from __future__ import division
__author__ = 'Chris Johnson'

import basictourstuff
import CompleteSolution
import tsp_start_code_no_greedy
import Graph
import cooling
import operators
import math


class Experiment:

    #want_experiment = True will use B&B to determine optimal tour costs and run the class experiments
    #want_experiment = False if you just want to determine the optimal initial temperature or just visualize

    #det_temp = True will recalculate the best initial temperature using the cities for the current experiment
    #det_temp = False will use 300 for the initial temperature, a precomputed value found using determine_Temp_Cumulative

    #want_visualize = True if you want to visualize while the experiment is running
    #want_visualize = False will speed the experiment up
    def __init__(self, want_experiment=True, det_temp=False, want_visualize=False):
        self.reset()
        self.table_avg_costs_bad_move = []
        self.domain = [2, 15]
        self.range = [50, 105]
        self.jump_multiplier = 1.5

        self.initial_prob = .6

        self.initial_cooling_func = cooling.cooling80

        self.problems = []
        self.opttourcosts = []
        self.num_problems = 10
        self.problem_size = 14

        self.set_up_problems()

        self.want_visualize = want_visualize

        if want_experiment:
            self.det_opt_tour_costs()


        if det_temp:
            self.T = 5000
            self.T = self.determine_Temp()
        else:
            #this was determined experimentally running the function determine_Temp_Cumulative
            self.T = 300






    def reset(self):
        self.table_number_states_explored = []
        self.table_terminal_solution_qualities = []


    def single_problem(self, T, cities, cooling_func, operator, jump_multiplier, opttourcost):


        #don't limit the number of failed attempts, the algorithm will terminate when the max_permutations_considered is reached
        max_bad_consecutive_move_attempts = -1

        #set starting number of states to consider
        max_permutations_considered = math.pow(2, self.domain[0])

        list_number_states_explored = []
        list_terminal_solution_qualities = []
        list_avg_costs_bad_move = []

        cs = CompleteSolution.CompleteSolution()
        while max_permutations_considered <= math.pow(2, self.domain[1]):

            cs.hill_climber(cities, T, cooling_func, operator, max_bad_consecutive_move_attempts, max_permutations_considered, self.want_visualize, True)
            list_avg_costs_bad_move.append(cs.average_cost_bad_move)

            #calculate the log base 2 of  the states explored
            log_states_explored = math.log(cs.permutation_count, 2)
            list_number_states_explored.append(log_states_explored)

            #calculate quality
            quality = (opttourcost / cs.best_tour_cost) * 100
            list_terminal_solution_qualities.append(quality)

            #reset CompleteSolution variables (not sure if this is necessary)
            cs.reset()

            #increase the number of permutations by a set factor
            max_permutations_considered *= jump_multiplier

        self.table_number_states_explored.append(list_number_states_explored)
        self.table_terminal_solution_qualities.append(list_terminal_solution_qualities)
        self.table_avg_costs_bad_move.append(list_avg_costs_bad_move)






    #cooling function is kept constant
    #cooling.cooling80 is used
    def experiment_1(self):
        "For 10 problems, each of the same problem size. Compare 6 different algorithms and plot the solution quality vs average states explored"
        "Independent variable = state explored"
        "Dependent variable = solution quality"
        "Algorithms are the six combinations of [hill climbing and simulated annealing] X [swap two random cities, swap two random cities 5 times, reverse random subsequence"



        title = "Quality as a Function of States Explored with Algorithm Variations"
        x_label = "number of states explored (log base 2)"
        y_label = "quality (optimal solution / complete solution) * 100"
        caption = "Problem size: ("+str(self.problem_size)+"). \n"
        caption += "Temperature set using 60% as initial probability. \nCooled by 20% every 200 explored states. \nTemperature is 0 for pure hill climbing versions"



        #all six algorithms
        graph_all = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)

        #only the 3 hills
        graph_hill = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)

        #only the 3 SA
        graph_sa = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)

        # hill and SA for the 3 operators...
        graph_swap = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)
        graph_5_swap = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)
        graph_sub = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)

        graphs_hill_swap = [graph_all, graph_hill, graph_swap]
        graphs_hill_5_swap = [graph_all, graph_hill, graph_5_swap]
        graphs_hill_sub = [graph_all, graph_hill, graph_sub]

        graphs_sa_swap = [graph_all, graph_sa, graph_swap]
        graphs_sa_5_swap = [graph_all, graph_sa, graph_5_swap]
        graphs_sa_sub = [graph_all, graph_sa, graph_sub]

        graphs_all = [graph_all, graph_hill, graph_sa, graph_swap, graph_5_swap, graph_sub]


        self.hill_swap(self.problems, self.jump_multiplier, self.initial_cooling_func, self.opttourcosts,  graphs_hill_swap)
        self.hill_5_swap(self.problems, self.jump_multiplier, self.initial_cooling_func,  self.opttourcosts, graphs_hill_5_swap)
        self.hill_sub(self.problems, self.jump_multiplier, self.initial_cooling_func,  self.opttourcosts, graphs_hill_sub)





        self.sa_swap(self.T, self.problems, self.jump_multiplier, self.initial_cooling_func,  self.opttourcosts, graphs_sa_swap)
        self.sa_5_swap(self.T, self.problems, self.jump_multiplier, self.initial_cooling_func, self.opttourcosts, graphs_sa_5_swap)
        self.sa_sub(self.T, self.problems, self.jump_multiplier, self.initial_cooling_func,  self.opttourcosts, graphs_sa_sub)


        for graph in graphs_all:
            graph.graph()

    #comparing cooling functions with best operator found in experiment 1

    def experiment_2(self):

        title = "Quality as a Function of States Explored using Reverse Random Subsequence Operator with Cooling Variations"
        x_label = "number of states explored (log base 2)"
        y_label = "quality (optimal solution / complete solution) * 100"

        caption = "Problem size: ("+str(self.problem_size)+").\n"
        caption += "Temperature set using 60% as initial probability. \nCooled by a specific percentage every 200 explored states."


        graphs_all = Graph.Graph(self.domain, self.range, x_label, y_label, title, caption)

        graphs = [graphs_all]

        self.sa_cooling20(self.T, self.problems, self.jump_multiplier, self.opttourcosts, graphs)
        self.sa_cooling40(self.T, self.problems, self.jump_multiplier, self.opttourcosts, graphs)
        self.sa_cooling60(self.T, self.problems, self.jump_multiplier, self.opttourcosts, graphs)
        self.sa_cooling90(self.T, self.problems, self.jump_multiplier, self.opttourcosts, graphs)

        for graph in graphs:
            graph.graph()

    def visualize(self, cool_func, operator):
        cs = CompleteSolution.CompleteSolution()
        for i in range(0, len(self.problems)):
            cs.hill_climber(self.problems[i], self.T, cool_func, operator, -1, math.pow(2, self.domain[1]), True, True)
            cs.reset()

    def hill_swap(self, problems, jump_multiplier, cooling_func, opttourcosts, graphs):
        line_label = "hill climbing: swap 2 random cities"
        #do hill, swap two random cities
        self.several_problems(0, problems, operators.swap_random, cooling_func,  jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def hill_5_swap(self, problems, jump_multiplier, cooling_func,  opttourcosts, graphs):
        line_label = "hill climbing: swap 2 random cities 5 times"
        #do hill, swap two random cities 5 times
        self.several_problems(0, problems, operators.swap_random_5times, cooling_func,  jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def hill_sub(self, problems, jump_multiplier, cooling_func,  opttourcosts, graphs):
         line_label = "hill climbing: reverse random subsequence"
         #do hill, reverse random subsequence
         self.several_problems(0, problems, operators.reverse_random_subsequence2, cooling_func,  jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def sa_swap(self, T, problems, jump_multiplier, cooling_func,  opttourcosts, graphs):
        line_label = "Simulated Annealing: swap 2 random cities"
        self.several_problems(T, problems, operators.swap_random, cooling_func,   jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def sa_5_swap(self, T, problems, jump_multiplier, cooling_func,  opttourcosts, graphs):
        line_label = "Simulated Annealing: swap 2 random cities 5 times"
        self.several_problems(T, problems, operators.swap_random_5times, cooling_func,  jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def sa_sub(self, T, problems, jump_multiplier, cooling_func,  opttourcosts, graphs):
        line_label = "Simulated Annealing: reverse random subsequence"
        self.several_problems(T, problems, operators.reverse_random_subsequence2, cooling_func,  jump_multiplier, opttourcosts, graphs, line_label, "-", "")


    def sa_cooling20(self, T, problems, jump_multiplier, opttourcosts, graphs):
        line_label = "Cooled by 80% every 200 operations"
        self.several_problems(T, problems, operators.reverse_random_subsequence2, cooling.cooling20, jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def sa_cooling40(self, T, problems, jump_multiplier, opttourcosts, graphs):
        line_label = "Cooled by 60% every 200 operations"
        self.several_problems(T, problems, operators.reverse_random_subsequence2, cooling.cooling40, jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def sa_cooling60(self, T, problems, jump_multiplier, opttourcosts, graphs):
        line_label = "Cooled by 40% every 200 operations"
        self.several_problems(T, problems, operators.reverse_random_subsequence2, cooling.cooling60, jump_multiplier, opttourcosts, graphs, line_label, "-", "")

    def sa_cooling90(self, T, problems, jump_multiplier, opttourcosts, graphs):
        line_label = "Cooled by 10% every 200 operations"
        self.several_problems(T, problems, operators.reverse_random_subsequence2, cooling.cooling90, jump_multiplier, opttourcosts, graphs, line_label, "-", "")



    def several_problems(self, T, problems, operator, cooling_func, jump_multiplier, opttourcosts, graphs, line_label, line_style, line_marker):


        for i in range(0, len(problems)):
            self.single_problem(T, problems[i], cooling_func, operator, jump_multiplier, opttourcosts[i])

        list_avg_number_states_explored = self.avg_of_list(self.table_number_states_explored)
        list_avg_terminal_solution_qualities = self.avg_of_list(self.table_terminal_solution_qualities)

        if graphs is not None:
            for graph in graphs:
                graph.add_line(list_avg_number_states_explored, list_avg_terminal_solution_qualities, line_label, line_style, line_marker)
        self.reset()



    def set_up_problems(self):
        for i in range(0, self.num_problems):
            cities = basictourstuff.Cities(self.problem_size)
            self.problems.append(cities)

    def det_opt_tour_costs(self):
        for i in range(0, self.num_problems):
            #find the optimal tour costs using B&B
            bbtour = tsp_start_code_no_greedy.all_bound_TSP(self.problems[i])
            self.opttourcosts.append(basictourstuff.total_distance(bbtour))

    def determine_Temp(self):
        list_avg_costs_bad_move = []
        cs = CompleteSolution.CompleteSolution()
        for i in range(0, len(self.problems)):
            cs.hill_climber(self.problems[i], self.T, self.initial_cooling_func, operators.reverse_random_subsequence2, -1, math.pow(2, self.domain[1]), False, True)
            list_avg_costs_bad_move.append(cs.average_cost_bad_move)
            cs.reset()
        avg_bad_move_cost = self.mean(list_avg_costs_bad_move)
        return basictourstuff.initialize_temp(avg_bad_move_cost, self.initial_prob)



    #taken from http://stackoverflow.com/questions/10919664/averaging-list-of-lists-python

    def mean(self, a):
        return sum(a) / len(a)

    def avg_of_list(self, a):
        return map(self.mean, zip(*a))

    #test avg_of_list

    # a = [[240, 240, 239],
    #       [250, 249, 237],
    #       [242, 239, 237],
    #       [240, 234, 233]]
    #
    # print avg_of_list(a)


#used to determine a good temperature by running Experiment.determine_Temp many times and averaging
def determine_Temp_Cumulative():

    count = 10
    T = 0
    for i in range(count):
        e = Experiment(False, True)
        T += e.T

    return T / count


#run this line to print a good value for the initial temperature

#print determine_Temp_Cumulative()








#run these lines to JUST visualize the tour changes with the specified cooling function and operator
#other than these arguments, uses the values set in the Experiment constructor, e.g., for the problem size

#e = Experiment(False, False)
#e.visualize(cooling.cooling60, operators.reverse_random_subsequence2)







#run these lines for the assignment experiments 1 and 2
#the graphs for experiment 1 will display one at a time once it's done. These need to be closed before experiment 2's graphs will display
#parmeters like problem size and number of problems can be set in the Experiment constructor

#just run the experiment. This is fastest
e = Experiment(True, False)

#run the experiment and visualize. visualization has a delay, so this is a lot slower
#e = Experiment(True, False, True)


#you can run just 1, just 2, or both
#you can run them in either order

#runs experiment 1
e.experiment_1()

#runs experiment 2
e.experiment_2()










