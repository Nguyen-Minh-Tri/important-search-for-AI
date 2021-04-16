# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def general_searching(fringe, problem):
    def travel(v):
        path = []
        for node in v:
            path.append(node[1])
        return path
    fringe.push([(problem.getStartState(), None, 0)])
    visited = set()
    while not fringe.isEmpty():
        v = fringe.pop()
        if problem.isGoalState(v[-1][0]):
            return travel(v[1:])
        if v[-1][0] not in visited:
            visited.add(v[-1][0])
            successor = problem.getSuccessors(v[-1][0])
            for node in successor:
                fringe.push(v + [(node[0], node[1], node[2] + v[-1][2])])

def limit_search(limit,fringe, problem):
    depth = 0
    def travel(v):
        path = []
        for node in v:
            path.append(node[1])
        return path
    fringe.push([(problem.getStartState(), None, 0)])
    visited = set()

    while not fringe.isEmpty():
        if depth > limit:
            error("Not found within depth limit")
        v = fringe.pop()
        if problem.isGoalState(v[-1][0]):
            return travel(v[1:])
        if v[-1][0] not in visited:
            visited.add(v[-1][0])
            successor = problem.getSuccessors(v[-1][0])
            for node in successor:
                fringe.push(v + [(node[0], node[1], node[2] + v[-1][2])])
            depth +=1

def limit_search2(limit,fringe, problem):
    depth = 0
    def travel(v):
        path = []
        for node in v:
            path.append(node[1])
        return path
    fringe.push([(problem.getStartState(), None, 0)])
    visited = set()

    while not fringe.isEmpty():
        if depth > limit:
            return 0
        v = fringe.pop()
        if problem.isGoalState(v[-1][0]):
            return travel(v[1:])
        if v[-1][0] not in visited:
            visited.add(v[-1][0])
            successor = problem.getSuccessors(v[-1][0])
            for node in successor:
                fringe.push(v + [(node[0], node[1], node[2] + v[-1][2])])
            depth +=1


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    return general_searching(util.Stack(), problem)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return general_searching(util.Queue(), problem)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    def func(item):
        return item[-1][2]
    fringe = util.PriorityQueueWithFunction(func)
    return general_searching(fringe, problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    def func(item):
        return item[-1][2] + heuristic(item[-1][0], problem)
    fringe = util.PriorityQueueWithFunction(func)
    return general_searching(fringe, problem)

def depthLimitedSearch(problem):
    return limit_search(10000, util.Stack(), problem)
def iterative_deepening(problem):
    for i in range(0, 10000):
        temp = limit_search2(i, util.Stack(), problem)
        if temp == 0:
            pass
        else:
            return temp
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
dls = depthLimitedSearch
iddfs = iterative_deepening