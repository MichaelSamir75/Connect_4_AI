from audioop import minmax
import math
from pickle import FALSE, TRUE


class mimimax_algorithm:
    def minimax(self,node,cur_depth,height,heuristic,isMax):
        if(cur_depth == height): return heuristic[node]

        col = 1
        if(isMax):
            value = -math.inf  #negative infinity

            #get the max value of the 7 states
            #if the tree is 1-based the to get the i-th children --> node*2 + i   (i starts from 0 to 6)
            #if the tree is 0-based the to get the i-th children --> node*2 + i   (i starts from 1 to 7)


            for i in range (7):
                temp = minmax(node*2 + i,cur_depth+1,height,heuristic,False)
                if(temp > value): 
                    value = temp
                    col = i

            return value

        else:
            value = math.inf   #positive infinity     

            #get the min value of the 7 states
            #if the tree is 1-based the to get the i-th children --> node*2 + i   (i starts from 0 to 6)
            #if the tree is 0-based the to get the i-th children --> node*2 + i   (i starts from 1 to 7)
            for i in range (7):
                temp = minmax(node*2 + i,cur_depth+1,height,heuristic,TRUE)
                if(temp < value): 
                    value = temp
                    col = i

            return col


    def array_to_long(self,arr):






t = mimimax_algorithm()
t.test()