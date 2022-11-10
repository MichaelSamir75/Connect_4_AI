from asyncio.windows_events import NULL
from ctypes import sizeof
from ctypes.wintypes import LONG
from itertools import tee
import math
from pickle import FALSE, TRUE
# from pygame import init
from bitManuplation import bit
from heuristic import heuristic

class mimimax_bruning_algorithm:
    
    final_result = 0

    # initialize the global variables
    def __init__(self):
        self.decision_tree = []

    def minimax(self,state,max_height,cur_depth,isMax,alpha,beta):
        if(cur_depth == max_height): 
            heur = heuristic()
            if(isMax):
                return heur.get_heuristic(state)
            else:
                return heur.get_heuristic(state)
            

        final_state = 0
        col = []

        # max is the yellow player (bit 1)
        if isMax:
            value = -math.inf  #negative infinity
            #get the max value of the 7 states
            for i in range (7):
                # get the first empty place in the col and add to it 
                startDigitOfCol = 9*i
                x = 7 # 0000 0111
                x = x << startDigitOfCol # shift left to the col i
                first_empty =  x & state
                first_empty = first_empty >> startDigitOfCol # shift right to know the number in decimal
                if(first_empty == 6): return -math.inf  #the column is full
                next_state = state | (1 << (startDigitOfCol + first_empty + 3))     # 1 indicate the player color
                first_empty+=1
                first_empty = first_empty << startDigitOfCol
                next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
                next_state = next_state | first_empty   # set the first empty in the next state

                #add to the tree
                col.append([next_state,alpha,beta])

                temp = self.minimax(next_state,max_height,cur_depth+1,False,alpha,beta)
                if(temp > value): 
                    value = temp
                    final_state = next_state
                alpha = max(alpha,temp)
                if beta <= alpha:
                    break

            # col.append([final_state,alpha,beta])
            self.decision_tree.append(col)
            self.final_result = final_state
            return value
        # min is the red player (bit 0)
        else:
            value = math.inf   #positive infinity     
            #get the min value of the 7 states
            for i in range (7):

                # get the first empty place in the col and add to it 
                startDigitOfCol = 9*i
                x = 7 # 0000 0111
                x = x << startDigitOfCol # shift left to the col i
                first_empty =  x & state
                first_empty = first_empty >> startDigitOfCol # shift right to know the number in decimal
                if(first_empty == 6): return math.inf  #the column is full
                next_state = state | (0 << (startDigitOfCol + first_empty + 3))  # 0 indicate the player color(redundant step because it's actually equal 0)
                first_empty+=1
                first_empty = first_empty << startDigitOfCol
                next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
                next_state = next_state | first_empty   # set the first empty in the next state

                #add to the tree
                col.append([next_state,alpha,beta])


                temp = self.minimax(next_state,max_height,cur_depth+1,1,alpha,beta)
                if(temp < value): 
                    value = temp
                    final_state = next_state
                    
                beta = min(beta,temp)
                if beta <= alpha:
                    break

            # col.append([final_state,alpha,beta])
            self.decision_tree.append(col)
            self.final_result = final_state
            return value



    def solve(self,state,max_height):

        # convert the current state to int
        bit_manp = bit()
        cur_state = int(bit_manp.arr2dToInt(state))

        # add the current state to the decision tree
        # col = []
        # col.append(cur_state)
        # self.decision_tree.append(col)
        
        print(state)
        
        self.minimax(cur_state,max_height,0,1,-math.inf,math.inf) #assume that the agent is the yellow player
        final_state_int = self.final_result
        final_state = bit_manp.IntToarr2d(final_state_int) 
        print(final_state)

        # the tree begins with the leaves from left to right showing the 7 states and the 8-th of each state represent the node that the heuristic has choosen
        for i in range(len(self.decision_tree)):
            for j in range(len(self.decision_tree[i])):
                te = bit_manp.IntToarr2d(self.decision_tree[i][j][0])
                print(f"{i} {te}")


        return final_state,self.decision_tree





state = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0],
        [1,0,0,1,0,0,0],
        [1,0,2,1,2,0,2]]

test = mimimax_bruning_algorithm()
test.solve(state,2)
# print()