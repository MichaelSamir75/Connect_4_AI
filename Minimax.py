from audioop import minmax
from itertools import tee
import math
from pickle import FALSE, TRUE
from bitManuplation import bit

class mimimax_algorithm:
    def minimax(self,state,max_height,cur_depth,isMax):
        if(cur_depth == max_height): return # heuristic(state in 2d)


        final_state = 0

        # max is the yellow player (bit 1)
        if(isMax):
            value = -math.inf  #negative infinity

            #get the max value of the 7 states
            for i in range (7):
                
                # get the first empty place in the col and add to it 
                startDigitOfCol = 9*i
                x = 7 # 0000 0111
                x = x << startDigitOfCol # shift left to the col i
                first_empty =  x | state
                first_empty = first_empty >> startDigitOfCol # shift right to know the number in decimal
                if(first_empty == 6): return -math.inf  #the column is full
                next_state = state | (1 << (startDigitOfCol + first_empty + 3))     # 1 indicate the player color
                first_empty+=1
                first_empty = first_empty << startDigitOfCol
                next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
                next_state = next_state | first_empty   # set the first empty in the next state


                temp = minmax(next_state,max_height,cur_depth+1,False)
                if(temp > value): 
                    value = temp
                    final_state = next_state

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
                first_empty =  x | state
                first_empty = first_empty >> startDigitOfCol # shift right to know the number in decimal
                if(first_empty == 6): return math.inf  #the column is full
                next_state = state | (0 << (startDigitOfCol + first_empty + 3))  # 0 indicate the player color(redundant step because it's actually equal 0)
                first_empty+=1
                first_empty = first_empty << startDigitOfCol
                next_state = next_state & ~(7 << startDigitOfCol)  # clear the 3 bit that representing the first empty
                next_state = next_state | first_empty   # set the first empty in the next state



                temp = minmax(next,max_height,cur_depth+1,TRUE)
                if(temp < value): 
                    value = temp
                    final_state = next_state

            return final_state


    def array_to_long(self,arr):
        return


    def solve(self,state,max_height):
        bit_manp = bit()
        cur_state = bit_manp.arr2dToInt(state,6,7)
        final_state = self.minimax(cur_state,max_height,0,True) #assume that the agent is the yellow player
        # return to 2d
        return final_state






t = mimimax_algorithm()
t.test()