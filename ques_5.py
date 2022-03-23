#Q5
def  uniformCostSearch(goal, start):
    # goal state from starting
    global Amaan,Malik
    listNew = []
    queue = []#making priority queue according to the cost given below
 
    # set the listNew vector to max value
    for i in range(len(goal)):
        listNew.append(10**8)
 
    # insert the starting index
    queue.append([0, start])
 
    # visited nodes ka store
    visited = {}
    count = 0
    while (len(queue) > 0):
 
        # get the top element
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]#pop
 
        # get the original value
        p[0] *= -1     # value is multiplied by -1 so that
             # least priority is at the top
        if (p[1] in goal):
 
            # get the current position
            index = goal.index(p[1])
 
            # if goal is reached
            if (listNew[index] == 10**8):
                count += 1
            if (listNew[index] > p[0]):
                listNew[index] = p[0]
 

            del queue[-1]#pop
 
            queue = sorted(queue)
            if (count == len(goal)):
                return listNew
 
        # check for the non visited nodes
        # which are adjacent to present node
        if (p[1] not in visited):
            for i in range(len(Amaan[p[1]])):
 
                queue.append( [(p[0] + Malik[(p[1], Amaan[p[1]][i])])* -1, Amaan[p[1]][i]])
 
        # mark node as visited
        visited[p[1]] = 1
 
    return listNew
 
# main function
if __name__ == '__main__':
    Amaan,Malik = [[] for i in range(6)],{}
 
    # Creating the graph, Adding the edges
    Amaan[0].append(1)
    Amaan[0].append(4)
    Amaan[1].append(3)
    Amaan[3].append(4)
    Amaan[1].append(2)
    Amaan[2].append(4)
 
    # Creating the graph, Adding the cost
    Malik[(0, 1)] = 1
    Malik[(0, 4)] = 10
    Malik[(1, 3)] = 15
    Malik[(3, 4)] = 5
    Malik[(1, 2)] = 5
    Malik[(2, 4)] = 5
    
 
    goal = []#initialising final state
    goal.append(4)#Goal is 4(G)
 
    Solution = uniformCostSearch(goal, 0)#(0 is A)
    print("Minimum distance from 0 to 4 is = ",Solution[0])