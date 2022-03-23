#Q1

import math
import numpy as np

#Find and return the position of element to be found
def findPosition(s,elmnt):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==elmnt:
                return [i,j]
    return -1

#Calculating Eucledian distance
def eucledian(s,g):
    #creating a matrix with all elements zero and of size len(s)*len(s[0])
    res_mat = np.zeros([len(s),len(s[0])],dtype = float)

    for x1 in range(len(s)):
        for y1 in range(len(s[0])):
            elmnt=s[x1][y1]
            pos=findPosition(g,elmnt)

            x2=pos[0]#(x2,y2) = (0th,1st)element of pos
            y2=pos[1]
            res_mat[x1][y1] = math.sqrt((x2-x1)**2 + (y2-y1)**2) #formula for euclidean
    Amaan=0

    for i in range(len(res_mat)):
        Amaan += sum(res_mat[i])
        return Amaan

#calculating mannhattan distance
def manhattan(s,g):
    #creating a matrix with all elements zero and of size len(s)*len(s[0])
    res_mat = np.zeros([len(s),len(s[0])],dtype = float)

    for x1 in range(len(s)):
        for y1 in range(len(s[0])):
            elmnt=s[x1][y1]
            pos=findPosition(g,elmnt)

            x2=pos[0]
            y2=pos[1]

            res_mat[x1][y1] = abs(x2-x1) + abs(y2-y1) #formula for manhattan
    Amaan=0
    for i in range(len(res_mat)):
        Amaan += sum(res_mat[i])
    return Amaan

#calculate minkowoski distance
def minkowoski(s,g,p):
    #creating a matrix with all elements zero and of size len(s)*len(s[0])
    res_mat = np.zeros([len(s),len(s[0])],dtype = float)

    for x1 in range(len(s)):
        for y1 in range(len(s[0])):
            elmnt=s[x1][y1]
            pos=findPosition(g,elmnt)
            x2=pos[0]
            y2=pos[1]
            res_mat[x1][y1] = ((abs(x2-x1)**p) + (abs(y2-y1)**p))**(1./p) # formula for minkowoski
    Amaan=0
    for i in range(len(res_mat)):
        Amaan += sum(res_mat[i])
    return Amaan

#main
if __name__ == "__main__":
    p_val = 3 #value of p is 3
    s0 =[[2,0,3],[1,8,4],[7,6,5]]#initial state
    g=[[1,2,3],[8,0,4],[7,6,5]]#final state
    #Function calls
    euc = eucledian(s0,g)
    man = manhattan(s0,g)
    mink = minkowoski(s0,g,p_val)
   
    print(euc,man,mink)