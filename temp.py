from bitManuplation import bit

class heuristic:
    
    def __init__(self):
        self.n1_4_conn = 0
        self.n1_3_conn = 0
        self.n1_2_conn = 0
        self.n2_4_conn = 0
        self.n2_3_conn = 0
        self.n2_2_conn = 0
        
    def cont(self,value,person):
        if person == 1:
            if value == 4:
                self.n1_4_conn += 1
            elif value == 3:
                self.n1_3_conn += 1
            elif value == 2:
                self.n1_2_conn += 1
        elif person == 2:
            if value == 4:
                self.n2_4_conn += 1
            elif value == 3:
                self.n2_3_conn += 1
            elif value == 2:
                self.n2_2_conn += 1

    def get_heuristic_red(self,arr_state,case):
        # r = random.randint(-100,100)
        for i in range(len(arr_state)):
            for j in range(len(arr_state[i])):
                row = i
                column = j
                if arr_state[i][j] == 0 or arr_state[i][j] == (3-case): continue
                print(f"row = {row} col = {column}")
                counter = 0
                for q in range(4):
                    # print(f"{row}  q = {q}")
                    if (row+q) <= 5:
                        res = arr_state[row+q][column]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"1 {counter}")
                counter = 0
                for q in range(4):
                    if (row-q) >= 0:
                        res = arr_state[row-q][column]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"2 {counter}")
                counter = 0
                for q in range(4):
                    if (column+q) <= 6:
                        res = arr_state[row][column+q]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"3 {counter}")
                counter = 0
                for q in range(4):
                    if (column-q) >= 0:
                        res = arr_state[row][column-q]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"4 {counter}")
                counter = 0
                for q in range(4):
                    if ((row+q) <= 5) and ((column+q) <= 6):
                        res = arr_state[row+q][column+q]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"5 {counter}")
                counter = 0
                for q in range(4):
                    if ((row-q) >= 0) and ((column+q) <= 6):
                        res = arr_state[row-q][column+q]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"6 {counter}")
                counter = 0
                for q in range(4):
                    if ((row+q) <= 5) and ((column-q) >= 0):
                        res = arr_state[row+q][column-q]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"7 {counter}")
                counter = 0
                for q in range(4):
                    if ((row-q) >= 0) and ((column-q) >= 0):
                        res = arr_state[row-q][column-q]
                        if res == case:
                            counter += 1
                        elif res == 0 or res == (3-case): break
                self.cont(counter,1)
                print(f"8 {counter}")
                counter = 0
                
    def get_heuristic(self,state):
        bit_manp = bit()
        arr_state = bit_manp.IntToarr2d(state)
        self.get_heuristic_red(arr_state,1)
        self.get_heuristic_red(arr_state,2)
        return 0

state = [[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0],
        [1,0,2,1,0,0,0],
        [1,1,1,1,2,0,2]]

temp = heuristic()
temp.get_heuristic_red(state,1)
print(temp.n1_4_conn)
print(temp.n1_3_conn)
print(temp.n1_2_conn)