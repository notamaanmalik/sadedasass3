#Q3 Hill climbing
import copy 

#Compares final and initial states
def compare(i0,f):                              
    if i0==f:
        return 1
    else:
        return 0
       
#Adds elements that have not been visited to the queue and returns
def enqueue(finalState):                      
    global queue
   
    if finalState[1] not in visited:
        queue=queue+[finalState]
    else:
        return queue

#Removes and returns least heuristic element from the queue
def dequeue():                               
    global queue
    queue.sort()
    finalState=queue[0]
    queue=[]
    return finalState

#Calculates Number of operations to perform
def distance(s3,f):                          
    c=0
    for i in range(len(s3)):
        for j in range(len(s3[0])):
            if s3[i][j]!=f[i][j]:
             c=c+1
    return c
           
queue=[]
visited=[]
  
#Finds position of the blank space in the progressive states 
def find_pos(s1):                            
    for i in range(len(s1)):
        for j in range(len(s1[0])):
            if s1[i][j]==0:
                l=[]
                l+=[i,j]
                return l
    return 0
#Checks the current state and moves the block up 
def up(i0,pos):                              
    row=pos[0]
    col=pos[1]
    s1=copy.deepcopy(i0)
    if row==0:
        return i0
    else:
      s1[row][col]=s1[row-1][col]
      s1[row-1][col]=0
      return s1
  
#Checks the current state and moves the block left  
def left(i0,pos):
    row=pos[0]
    col=pos[1]
    s2=copy.deepcopy(i0)
    if col==0:
        return i0
    else:
      s2[row][col]=s2[row][col-1]
      s2[row][col-1]=0
      return s2
 
#Checks the current state and moves the block right
def right(i0,pos):
    s3=copy.deepcopy(i0)
    row=pos[0]
    col=pos[1]
    if col==2:
        return i0
    else:
      s3[row][col]=s3[row][col+1]
      s3[row][col+1]=0
      return s3

#Checks the current state and moves the block down
def down(i0,pos):
    row=pos[0]
    col=pos[1]
    s4=copy.deepcopy(i0)
    if row==2:
        return i0
    else:
      s4[row][col]=s4[row+1][col]
      s4[row+1][col]=0
      return s4

#defining main and function calls
def main():
    global visited
    s0=[[2,0,3],[1,8,4],[7,6,5]]#initial state
    f=[[1,2,3],[8,0,4],[7,6,5]]#final state
    while(1):
        dist=distance(s0,f)
        print("Distance is (calculated with the help of heuristic): ",dist)
        pos=find_pos(s0)
        
        
        finalState=up(s0,pos)
        d1=distance(finalState,f)
        i=compare(f,finalState)#compare the final state and initial state
        if(i==1):
            exit(0)
        else:
            t1=[]
            t1=t1+[finalState,d1]
            enqueue([d1,finalState])#enqueueing the up part in the list

        
        finalState=down(s0,pos)
        d2=distance(finalState,f)
        i=compare(f,finalState)
        if(i==1):
            exit(0)
        else:
            t2=[]
            t2=t2+[finalState,d2]
            enqueue([d2,finalState])#enqueueing the down part in the list
   
        finalState=left(s0,pos)
        d3=distance(finalState,f)
        i=compare(f,finalState)
        if(i==1):
            exit(0)
        else:
            t3=[]
            t3=t3+[finalState,d3]
            enqueue([d3,finalState])#enqueueing the left part in the list
     
        finalState=right(s0,pos)
        d4=distance(finalState,f)
        i=compare(f,finalState)
        if(i==1):
            exit(0)
        else:
            t3=[]
            t3=t3+[finalState,d3]
            enqueue([d4,finalState])
 
        state=dequeue()
        state1=state[1]
        if (dist>=state[0]):
            print("Final state reached is:")
            print(state)
            return
        else:
          s0=state1

if __name__ =="__main__":
    main()