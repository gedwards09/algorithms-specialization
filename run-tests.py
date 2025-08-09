import os

## CONFIGURATION ##
Tester = '../stanford-algs/tester/python3/tester.py'
TestCasesDirPrefix = '../stanford-algs/testCases/'
Configuration = """0
./course-1/1/karatsuba.py course1/assignment1Multiplication/
./course-1/2/inversions.py course1/assignment2Inversions/
./course-1/3/quicksort.py course1/assignment3Quicksort/ max_size=100000
./course-1/4/mincut.py course1/assignment4MinCut/
./course-1/Q/ex1.py course1/optionalTheoryProblemsBatch1/question1/
./course-2/1/scc.py course2/assignment1SCC/
./course-2/2/dijkstra.py course2/assignment2Dijkstra/
./course-2/3/median.py course2/assignment3Median/
./course-2/4/two-sum.py course2/assignment4TwoSum/
./course-3/1/scheduling.py course3/assignment1SchedulingAndMST/questions1And2/
./course-3/1/MST.py course3/assignment1SchedulingAndMST/question3/
./course-3/2/clustering.py course3/assignment2Clustering/question1/
./course-3/2/hamming.py course3/assignment2Clustering/question2/
./course-3/3/huffman.py course3/assignment3HuffmanAndMWIS/question1And2/
./course-3/3/mwis.py course3/assignment3HuffmanAndMWIS/question3/
./course-3/4/knapsack.py course3/assignment4Knapsack/ max_size=100000
./course-4/1/all-pairs-shortest-path.py course4/assignment1AllPairsShortestPath/ max_size=512
./course-4/2/tsp.py course4/assignment2TSP/ max_size=19
./course-4/3/tsp-heuristic.py course4/assignment3TSPHeuristic/ max_size=4000
./course-4/4/two-sat.py course4/assignment4TwoSat/
"""
###################

def runTests():
    skipHeader = True
    ct = 0
    for line in Configuration.split('\n'):
        if skipHeader:
            skipHeader = False
            continue
        args = line.split(' ')
        if len(args) < 2:
            continue
        scriptName = args[0]
        dir = args[1]
        cmd = ' '.join(['python3', Tester, scriptName, TestCasesDirPrefix + dir] + args[2:])
        print(cmd)
        rc = os.system(cmd)
        if rc != 0:
            return -1
        else:
            ct += 1
    return ct

def __main__():
    ct = runTests()
    print('')
    if ct > 0:
        print("{0} tests passed".format(ct))
    else:
        print('Some tests failed')

if __name__ == '__main__':
    __main__()