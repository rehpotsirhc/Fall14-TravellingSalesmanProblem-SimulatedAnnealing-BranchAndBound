__author__ = 'Chris Johnson'

import matplotlib.pyplot as plt
import time
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)




#VISUALIZATION OF TOUR
def plot_tour(tour):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            fxn()
            plt.ion()
            plotline(list(tour) + [tour[0]])
            plt.pause(0.0001)
            plotline([tour[0]], 'rs')
            plt.pause(0.0001)
            time.sleep(.065)
            plt.clf()

def plot_tour_stay(tour):
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
