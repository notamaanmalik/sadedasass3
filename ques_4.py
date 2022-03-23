#Q4
import copy
import sys
#initialising initial and final states
Q=[]
Goal=[[1,2,3],[8,0,4],[7,6,5]]
initial_State=[[2,8,3],[1,5,4],[7,6,0]]
visited_State=[]

def find_Position(initial_State):
    #for blank space
    for i in range(len(initial_State)):
        for j in range(len(initial_State)):
            if(initial_State[i][j]==0):
                return [i,j]
            
            
def find_Position_Plate(initial_State,val):
    #for finding the position of input element in current state
    for i in range(len(initial_State)):
        for j in range(len(initial_State)):
            if(initial_State[i][j]==val):
                return [i,j]
 #Add element to the queue           
def enqueue(Q,key):
    # print(Q)
    # print(key)
    Q+=[key]
    return Q

#Delete the top element
def dequeue(Q):
    if(len(Q)==0):
        return Q
    del Q[0]
    return Q
#Define Heuristic function
def Heuristic_Manhattan(initial_State,Goal):
    Heuristic_Manhattan_value=0
    for i in range(len(Goal)):
        for j in range(len(Goal[0])):
            L=find_Position_Plate(Goal,initial_State[i][j])
            Heuristic_Manhattan_value+=abs(i-L[0])+abs(j-L[1])
    return Heuristic_Manhattan_value

#compare final and initial states
def comp(initial_State,G):
    if(initial_State==G):
        return True
    return False

#moving the blank to the left
def left(initial_State):
    L=find_Position(initial_State)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(initial_State)
    if(col==0):
        return final_State 
    final_State[row][col]=final_State[row][col-1]
    final_State[row][col-1]=0
    return final_State

#moving the blank to the right
def right(initial_State):
    L=find_Position(initial_State)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(initial_State)
    if(col==len(initial_State[0])-1):
        return final_State
    final_State[row][col]=final_State[row][col+1]
    final_State[row][col+1]=0
    return final_State

#moving the blank to the up
def up(initial_State):
    L=find_Position(initial_State)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(initial_State)
    if(row==0):
        return final_State
    final_State[row][col]=final_State[row-1][col]
    final_State[row-1][col]=0
    return final_State

#moving the blankto the down
def down(initial_State):
    L=find_Position(initial_State)
    row=L[0]
    col=L[1]
    final_State=copy.deepcopy(initial_State)
    if(row==len(initial_State)-1):
        return final_State
    final_State[row][col]=final_State[row+1][col]
    final_State[row+1][col]=0
    return final_State
if(comp(initial_State,Goal))==True:
    exit()
def search(initial_State,visited_State):
    for i in range(len(visited_State)):
        if(initial_State==visited_State[i]):
            return True
    return False

#Sort the entries in heuristic function
def sorting_Heuristic(Q,Goal):
    min=100000000
    j=-1
    for i in range(len(Q)):
        Heuristic_Manhattan_Value=Heuristic_Manhattan(Q[i],Goal)
        if(Heuristic_Manhattan_Value<min):
            min=Heuristic_Manhattan_Value
            j=i
    initial_State=Q[j]
    del Q[j]
    return initial_State

Q+=[initial_State]
while(len(Q)!=0):
    initial_State=sorting_Heuristic(Q,Goal)
    if(search(initial_State,visited_State)==False):
        visited_State+=[initial_State]
    if((comp(initial_State,Goal))==True):
        print("Number of states visited = ",len(visited_State))
        sys.exit(0)

    
    if(search(left(initial_State),visited_State)==False):
        # print(initial_State)
        Q=enqueue(Q,left(initial_State))
    if(search(right(initial_State),visited_State)==False):
        Q=enqueue(Q,right(initial_State))
    if(search(up(initial_State),visited_State)==False):
        Q=enqueue(Q,up(initial_State))
    if(search(down(initial_State),visited_State)==False):
        Q=enqueue(Q,down(initial_State))