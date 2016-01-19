__author__ = 'Chris Johnson'

import operators

def genTestList():
    list = []
    for i in range(50):
        list.append(i)
    return list

def removeElements(listUnChanged, listChanged):

    for i in range(len(listChanged)):
        listUnChanged.remove(i)


def testSwap():

    list = genTestList()
    listUnChanged = list[:]


    print "TESTING SWAP:\n"
    print "ORIGINAL LIST:"
    print list
    print "SWAPS:"
    print operators.swap(list, 1,  10)
    print operators.swap(list, 49,  48)
    print operators.swap(list, 0,  49)
    print operators.swap(list, 0,  100)

    print "CHAINS:"

    list = operators.swap(list, 7,  25)
    print list
    list = operators.swap(list, 0,  5)
    print list
    list = operators.swap(list, 0,  49)
    print list


    print "SHOULD BE 50:"
    print len(list)
    print "SHOULD BE 50:"
    print len(listUnChanged)

    removeElements(listUnChanged, list)
    print "SHOULD BE ZERO:"
    print len(listUnChanged)

def testRandomSwap():

    list = genTestList()
    listUnChanged = list[:]

    print "TESTING Random SWAP:\n"
    print "ORIGINAL LIST:"
    print list
    print "RANDOM SWAPS:"

    print operators.swap_random(list)
    print operators.swap_random(list)
    print operators.swap_random(list)

    print "CHAINS:"

    list = operators.swap_random(list)
    print list
    list = operators.swap_random(list)
    print list
    list = operators.swap_random(list)
    print list


    print "SHOULD BE 50:"
    print len(list)
    print "SHOULD BE 50:"
    print len(listUnChanged)

    removeElements(listUnChanged, list)
    print "SHOULD BE ZERO:"
    print len(listUnChanged)


def testRandomXSwap(times):

    list = genTestList()
    listUnChanged = list[:]
    print "TESTING Random "+str(times)+" SWAP:\n"
    print "ORIGINAL LIST:"
    print list
    print "RANDOM SWAPS:"

    print operators.swap_random_xTimes(list, times)


    print "CHAINS:"

    list = operators.swap_random_xTimes(list, times)
    print list
    list = operators.swap_random_xTimes(list, times)
    print list
    list = operators.swap_random_xTimes(list, times)
    print list


    print "SHOULD BE 50:"
    print len(list)
    print "SHOULD BE 50:"
    print len(listUnChanged)

    removeElements(listUnChanged, list)
    print "SHOULD BE ZERO:"
    print len(listUnChanged)


def testReverseSubsquence(seqLimit):

    list = genTestList()
    listUnChanged = list[:]
    print "TESTING REVERSE SUBSEQUENCES NOT GREATER THAN "+str(seqLimit)+" SWAP:\n"
    print "ORIGINAL LIST:"
    print list
    print "SUBSEQUENCE REVERSED:"

    print operators.reverse_random_subsequence(list, seqLimit)


    print "CHAINS:"

    list = operators.reverse_random_subsequence(list, seqLimit)
    print list
    list = operators.reverse_random_subsequence(list, seqLimit)
    print list
    list = operators.reverse_random_subsequence(list, seqLimit)
    print list


    print "SHOULD BE 50:"
    print len(list)
    print "SHOULD BE 50:"
    print len(listUnChanged)

    removeElements(listUnChanged, list)
    print "SHOULD BE ZERO:"
    print len(listUnChanged)




testSwap()
print "\n\n"
testRandomSwap()
print "\n\n"
testRandomXSwap(10)
print "\n\n"
testRandomXSwap(30)
print "\n\n"
testReverseSubsquence(5)
print "\n\n"
testReverseSubsquence(10)
print "\n\n"
testReverseSubsquence(50)
print "\n\n"
