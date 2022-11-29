import math
from bitManuplation import bit
from heuristic import heuristic
from fileinput import close
class mimimax_algorithm:

    # initialize the global variables
    def __init__(self):
        self.decision_tree = []
        self.values_heuristic = []

    # get the best move to agent 1 by minimax algorithm
    def minimax(self,state,max_height,cur_depth,isMax):
        if(cur_depth == max_height): 
            heur = heuristic()
            x = heur.get_heuristic(state,isMax)
            return x

        final_state = -1
        col = []
        values = []

        # max is the yellow player (bit 1)
        if(isMax):
            value = -math.inf  #negative infinity

            #get the max value of the 7 states
            for i in range (7):
                
                # get the first empty place in the col and add to it 
                startDigitOfCol = 9*i
                x = 7 # 0000 0111
                x = x << startDigitOfCol # shift left to the col i
                first_empty =  x & state
                first_empty = first_empty >> startDigitOfCol # shift right to know the number in decimal
                if(first_empty == 6): continue  #the column is full
                next_state = state | (1 << (startDigitOfCol + first_empty + 3))     # 1 indicate the player color
                first_empty+=1
                first_empty = first_empty << startDigitOfCol
                next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
                next_state = next_state | first_empty   # set the first empty in the next state

                temp = self.minimax(next_state,max_height,cur_depth+1,False)

                #add to the tree
                col.append(next_state)
                #add to the values of heuristic
                values.append(temp)

                if(temp > value): 
                    value = temp
                    final_state = next_state 

            if(final_state != -1):
                col.append(final_state)
                values.append(value)
                values.append(isMax)

                # append to the global arrays
                self.decision_tree.append(col)
                self.values_heuristic.append(values)

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
                if(first_empty == 6): continue  #the column is full
                next_state = state | (0 << (startDigitOfCol + first_empty + 3))  # 0 indicate the player color(redundant step because it's actually equal 0)
                first_empty+=1
                first_empty = first_empty << startDigitOfCol
                next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
                next_state = next_state | first_empty   # set the first empty in the next state

                
                temp = self.minimax(next_state,max_height,cur_depth+1,True)

                #add to the tree
                col.append(next_state)
                #add to the values of heuristic
                values.append(temp)

                if(temp < value): 
                    value = temp
                    final_state = next_state

            if(final_state != -1):
                col.append(final_state)
                values.append(value)
                values.append(isMax)

                #append to the global arrays 
                self.decision_tree.append(col)
                self.values_heuristic.append(values)

            return value

    def write_file(self):
        #number of nodes expanede
        num_of_nodes_expanded = 0
        bit_manp = bit()
        worker_file = open("assets/node_expansion_minimax.txt","w")
        for i in range(len(self.decision_tree)):
            for j in range(len(self.decision_tree[i])):
                num_of_nodes_expanded+=1
                worker_file.write(f'{bit_manp.IntToarr2d(self.decision_tree[i][j])} {self.values_heuristic[i][j]}  ')
                if(j==len(self.decision_tree[i]) -1):
                    worker_file.write(f'{self.values_heuristic[i][j+1]} ')
                worker_file.write(f'\n')
            worker_file.write(f'\n')
        worker_file.close()
        return num_of_nodes_expanded


    def solve(self,state,max_height):
        #clear the decision tree and the values in every call
        self.decision_tree.clear()
        self.values_heuristic.clear()

        # convert the current state to int
        bit_manp = bit()
        cur_state = int(bit_manp.arr2dToInt(state))
        
        self.minimax(cur_state,max_height,0,True) #assume that the agent is the yellow player(bit 1)
        
        # the final state is the last element in the decision tree (every state contains 8 states)
        decision_tree_size = len(self.decision_tree)
        last_col_decision_tree_size = len(self.decision_tree[decision_tree_size -1])
        final_state_int = self.decision_tree[decision_tree_size-1][last_col_decision_tree_size-1]
        final_state = bit_manp.IntToarr2d(final_state_int) 

        # number of nodes expanede
        # num_of_nodes_expanded = 0

        # the tree begins with the leaves from left to right showing the 7 states and the 8-th of each state represent the node that the heuristic has choosen
        # for i in range(len(self.decision_tree)):
        #     for j in range(len(self.decision_tree[i])):
        #         num_of_nodes_expanded+=1
        #         print(bit_manp.IntToarr2d(self.decision_tree[i][j]), end=" ")
        #         print(self.values_heuristic[i][j], end = " ")
        #         if(j==len(self.decision_tree[i]) -1): print(self.values_heuristic[i][j+1], end = " ")    
        #         print() 
        #     print()               
        num_of_nodes_expanded = self.write_file()
        print("fianl state : ", final_state)
        print("Number of nodes expanded = ", num_of_nodes_expanded)
        

        return final_state


# state = [[0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0], 
#         [1, 0, 0, 0, 0, 0, 0], 
#         [2, 0, 0, 2, 0, 0, 0]]        
# test = mimimax_algorithm()
# res = test.solve(state,3)
# print(res)