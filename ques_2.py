#Q2 
import copy 

Amaan=[]
tried=[]#list to keep track of tried states

#Defining the heuristic function, i.e count the number of blocks that do not
#match with goal state

def heuristic(i0,f):
    count=0
    for i in range(len(i0)):
        for j in range(len(i0[0])):
            if i0[i][j]!=f[i][j]:
                count=count+1
    return count

#Adding/queueing new non-tried elements to the list 
def enqueue(newState):
    global Amaan
    global tried
    if newState[1] not in tried:
        Amaan = Amaan + [newState]
        
        
#Removing element from the list which has the least heuristic value
def dequeue():
    global Amaan
    Amaan.sort()
    newState=Amaan[0]
    del Amaan[0]
    return newState

#To compare if the current state is the same as the final state
def compare(i0,f):
    if i0==f:
        return 1
    else:
        return 0
    
#To Find the position of the blank space in the current state and return it
def findPosition(i0):
    for i in range(len(i0)):
        for j in range(len(i0[0])):
            if i0[i][j]==0:
                l=[]
                l=l+[i,j]
                return l
      
#To check and move the empty space forUp and return
def forUp(i0):
    l=findPosition(i0)
    row=l[0]
    col=l[1]
    i1=copy.deepcopy(i0)
    if row==0:
        return i0
    else:
        i1[row][col]=i1[row-1][col]
        i1[row-1][col]=0
        return i1
    
#To check and move the empty space left and return
def left(i0):
    l=findPosition(i0)
    row=l[0]
    col=l[1]
    i1=copy.deepcopy(i0)
    if col==0:
        return i0
    else:
        i1[row][col]=i1[row][col-1]
        i1[row][col-1]=0
        return i1
    
#To check and move the empty space down and return
def down(i0):
    l=findPosition(i0)
    row=l[0]
    col=l[1]
    i1=copy.deepcopy(i0)
    if row==2:
        return i0
    else:
        i1[row][col]=i1[row+1][col]
        i1[row+1][col]=0
        return i1
    
#To check and move the empty space right and return
def right(i0):
    l=findPosition(i0)
    row=l[0]
    col=l[1]
    i1=copy.deepcopy(i0)
    if col==2:
        return i0
    else:
        i1[row][col]=i1[row][col+1]
        i1[row][col+1]=0
        return i1

#main including function calls
def main():
    
    global tried
    i0=[[2,0,3],[1,8,4],[7,6,5]] #Initial state
    f= [[1,2,3],[8,0,4],[7,6,5]]  #Final state 
    if compare(i0,f):
            print("Final_State")
            return
        
    count=0 #Maintaining Count
    while(1):#loop works until the final state is reached
        count=count+1
        newState=forUp(i0)
        if compare(newState,f):
            print("Final_State")
            print(count)
            return
        
        h=heuristic(newState,f)
        h1=[]
        h1=h1+[h,newState]
        enqueue(h1)         #Taking into account the heuristic formed by the forUp command

        newState=down(i0)
        if compare(newState,f):
            print("Final_State")
            print(count)
            return
        h=heuristic(newState,f)
        h1=[]
        h1=h1+[h,newState]
        enqueue(h1)         #Taking into account the heuristic formed by the down command

        newState=left(i0)
        if compare(newState,f):
            print("Final_State")
            print(count)
            return
        h=heuristic(newState,f)
        h1=[]
        h1=h1+[h,newState]
        enqueue(h1)         #Taking into account the heuristic formed by the left command

        newState=right(i0)
        if compare(newState,f):
            print("Final_State")
            print(count)
            return
        h=heuristic(newState,f)
        h1=[]
        h1=h1+[h,newState]
        enqueue(h1)         #Taking into account the heuristic formed by the right command

        state=dequeue()
        tried=tried+[i0]
        i0=state[1]         #The minimum heuristic state executes 

if __name__ == "__main__":
    main()