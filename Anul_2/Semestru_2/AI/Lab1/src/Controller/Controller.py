"""
Created on 10/03/2018
@author Stefan
"""

class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def BFS(self, root):
        q = [root]
        while len(q) > 0 :
            currentState = q.pop(0)
            if currentState.getValues()[-1].isComplete():
                    return currentState
            else:
                q = q + self.__problem.expand(currentState)

    def GBFS(self, root):
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            if node.getValues()[-1].isComplete():
                return node
            aux = []
            for x in self.__problem.expand(node):
                aux.append(x)
            aux = [ [x, self.__problem.heuristics(x,node)] for x in aux]
            aux.sort(key=lambda x:x[1])
            aux = [x[0] for x in aux]
            toVisit = aux[:] + toVisit