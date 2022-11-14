import math
from bitManuplation import bit
from heuristic import heuristic

class mimimax_bruning_algorithm:
    # initialize the global variables
    def __init__(self):
        self.decision_tree = []
        self.values_heuristic = []
        self.final_result = 0
    
    def get_child(self,rank,state):
        startDigitOfCol = 9*rank
        x = 7
        x = x << startDigitOfCol
        first_empty = x & state
        first_empty = first_empty >> startDigitOfCol
        if(first_empty == 6): return -math.inf  #the column is full
        next_state = state | (1 << (startDigitOfCol + first_empty + 3))     # 1 indicate the player color
        first_empty += 1
        first_empty = first_empty << startDigitOfCol
        next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
        next_state = next_state | first_empty   # set the first empty in the next state
        
        return next_state

    def minimax(self,state,max_height,cur_depth,isMax,alpha,beta):
        if(cur_depth == max_height): 
            heur = heuristic()
            return heur.get_heuristic(state,isMax)

        final_state = 0
        col = []
        values = []

        # max is the yellow player (bit 1)
        if isMax:
            value = -math.inf  #negative infinity
            #get the max value of the 7 states
            for i in range (7):
                next_state = self.get_child(i,state)
                #add to the tree
                col.append(next_state)

                temp = self.minimax(next_state,max_height,cur_depth+1,False,alpha,beta)
                values.append(temp)
                if(temp > value): 
                    value = temp
                    final_state = next_state
                
                alpha = max(alpha,temp)
                if beta <= alpha:
                    break

            col.append(final_state)
            values.append(value)
            values.append(isMax)
            
            self.decision_tree.append(col)
            self.values_heuristic.append(values)
            self.final_result = final_state
            return value
        # min is the red player (bit 0)
        else:
            value = math.inf   #positive infinity     
            #get the min value of the 7 states
            for i in range (7):
                next_state = self.get_child(i,state)
                #add to the tree
                col.append(next_state)

                temp = self.minimax(next_state,max_height,cur_depth+1,True,alpha,beta)
                values.append(temp)
                if(temp < value): 
                    value = temp
                    final_state = next_state
                    
                beta = min(beta,temp)
                if beta <= alpha:
                    break

            col.append(final_state)
            values.append(value)
            values.append(isMax)
            
            self.decision_tree.append(col)
            self.values_heuristic.append(values)
            self.final_result = final_state
            return value



    def solve(self,state,max_height):

        # convert the current state to int
        bit_manp = bit()
        cur_state = int(bit_manp.arr2dToInt(state))
        
        self.minimax(cur_state,max_height,0,True,-math.inf,math.inf) #assume that the agent is the yellow player
        final_state_int = self.final_result
        final_state = bit_manp.IntToarr2d(final_state_int) 
        print(f"final {final_state}")

        # the tree begins with the leaves from left to right showing the 7 states and the 8-th of each state represent the node that the heuristic has choosen
        for i in range(len(self.decision_tree)):
            for j in range(len(self.decision_tree[i])):
                print(bit_manp.IntToarr2d(self.decision_tree[i][j]), end=" ")
                print(self.values_heuristic[i][j], end = " ")
                if(j==len(self.decision_tree[i]) -1): print(self.values_heuristic[i][j+1], end = " ")    
                print()
            print()


        return final_state





state = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0],
        [1,0,0,1,0,0,0],
        [1,0,2,1,2,0,2]]

# test = mimimax_bruning_algorithm()
# test.solve(state,2)
# print()