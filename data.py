import search

data = [
    ["Oradea","Zerind",71],
    ["Oradea","Sibiu",151],
    ["Zerind","Arad",75],
    ["Arad","Sibiu",140],
    ["Arad","Timisoara",118],
    ["Sibiu","Fagaras",99],
    ["Sibiu","Rimnicu Vilcea",80],
    ["Rimnicu Vilcea","Pitesti",97],
    ["Rimnicu Vilcea","Craiova",146],
    ["Fagaras","Bucharest",211],
    ["Pitesti","Bucharest",101],
    ["Craiova","Pitesti",138],
    ["Timisoara","Lugoj",111],
    ["Lugoj","Mehadia",70],
    ["Mehadia","Drobeta",75],
    ["Drobeta","Craiova",120],
    ["Bucharest","Urziceni",85],
    ["Bucharest","Glurgiu",90],
    ["Urziceni","Hirsova",98],
    ["Urziceni","Vaslui",142],
    ["Hirsova","Eforie",86],
    ["Vaslui","Iasi",92],
    ["Iasi","Neamt",87],
    ["Neamt","",0],
]

class roadmap:
    def __init__(self, fr, to, data):
        self.data = data
        self.fr = fr
        self.to = to

    def getStartState(self):
        return [self.fr,"",0]

    def isGoalState(self, data):
        if data[0] == self.to:
            return True

    def getSuccessors(self, state):
        succ = []
        for road in self.data:
            
            if road[0] == state[0]:
                succ.append(([road[1],road[0],road[2]], road[0], road[2]))
        #print(1)
        #print(succ)
        return succ

    def getCostOfActions(self, actions):
        sum = 0
        #print(actions)
        if len(actions) == 2:
            for dt in self.data:
                if dt[0] == actions[0] and dt[1] == actions[1]:
                    sum += dt[2]
            #print(sum)
            return sum
        elif len(actions) > 2:
            for i in range(len(actions) - 1):
                for dt in self.data:
                    if dt[0] == actions[i] and dt[1] == actions[i+1]:
                        sum += dt[2]
            #print(sum)
            return sum
        else:
            #print(0)
            return 0

if __name__ == '__main__':

    problem = roadmap("Arad", "Bucharest",data)
    pathBr = search.breadthFirstSearch(problem)
    print("Breadth First Search: {}".format(pathBr))
    # pathD = search.depthFirstSearch(problem)
    # print("Depth First Search: {}".format(pathD))
    # pathU = search.uniformCostSearch(problem)
    # print("Uniform Cost Search: {}".format(pathU))
    # pathA = search.aStarSearch(problem)
    # print("A Star Search: {}".format(pathA))