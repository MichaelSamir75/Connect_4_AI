from bitManuplation import bit

class heuristic:
    solOfplayer = [0,0,0]

    def adding(self,c):
        if c == 2:
            self.solOfplayer[0] = self.solOfplayer[0] + 1
        elif c == 3:
            self.solOfplayer[1] = self.solOfplayer[1] + 1
        elif c == 4:
            self.solOfplayer[2] = self.solOfplayer[2] + 1
        elif c == 5:
            self.solOfplayer[2] = self.solOfplayer[2] + 2
        elif c == 6:
            self.solOfplayer[2] = self.solOfplayer[2] + 3
        elif c == 7:
            self.solOfplayer[2] = self.solOfplayer[2] + 4

    def adding2(self,c):
        s = 0
        if c == 4:
                    s = s + 1
        elif c == 5:
                    s = s + 2
        elif c == 6:
                    s = s + 3
        elif c == 7:
                    s = s + 4
        return s

    def get_heuristic_red(self,arr_state,x):
        count = 0
        j=0
        # horizontal
        for i in range (6):
            self.adding(count)
            count = 0
            for(j) in range (7):
                # print(f"row { i } col { j } value { arr_state[i][j] }")
                if arr_state[i][j] == x:
                    count += 1
                else:
                    self.adding(count)
                    count = 0
        self.adding(count)
        count = 0
        # vertical
        for j in range (7):
            self.adding(count)
            count = 0
            for i in range (6):
                if arr_state[i][j] == x:
                    count = count + 1
                else:
                    self.adding(count)
                    count = 0
        
        self.adding(count)
        count = 0
        for i in range(3,6):
                count = 0
                temp = 0
                for j in range(0,i+1):
                    if arr_state[i-temp][j] == x :
                        count +=1
                    else:
                        self.adding(count)
                        count = 0
                    temp += 1
                self.adding(count)
        
        for i in range(1,4):
                count = 0
                temp = 0
                for j in range(5,i-2,-1):
                    if arr_state[j][i+temp] == x :
                        count +=1
                    else:
                        self.adding(count)
                        count = 0
                    temp += 1
                self.adding(count)

        for i in range(3,6):
                count = 0
                temp = 0
                for j in range(6,6-i-1,-1):
                    if arr_state[i-temp][j] == x :
                        count +=1
                    else:
                        self.adding(count)
                        count = 0
                    temp += 1
                self.adding(count)
            
      
        for j in range(3,6):
                count = 0
                temp = 0
                for i in range(5,5-j-1,-1):
                    if arr_state[i][j-temp] == x :
                        count +=1
                    else:
                        self.adding(count)
                        count = 0
                    temp += 1
                self.adding(count)

        return self.solOfplayer
    
    def getScore(self,array,x):
        score = 0
        count = 0
        for i in range(6):
            score = score + self.adding2(count)
            count = 0
            for j in range (7):
                if array[i][j] == x:
                    count = count + 1
                else:
                    score = score + self.adding2(count)
                    count = 0
        score = score + self.adding2(count)
        count = 0           

        for j in range(7):
            score = score + self.adding2(count)
            count = 0
            for i in range (6):
                if array[i][j] == x:
                    count = count + 1
                else:
                    score = score + self.adding2(count)
                    count = 0
        score = score + self.adding2(count)
        count = 0

        for i in range(3,6):
                count = 0
                temp = 0
                for j in range(0,i+1):                
                    if array[i-temp][j] == x :
                        count +=1
                    else:
                        score = score + self.adding2(count)
                        count = 0
                    temp += 1
                score = score + self.adding2(count)
                
        for i in range(1,4):
                count = 0
                temp = 0
                for j in range(5,i-2,-1):
                    if array[j][i+temp] == x :
                        count +=1
                    else:
                        score = score + self.adding2(count)
                        count = 0
                    temp += 1
                score = score + self.adding2(count)

        for i in range(3,6):
                count = 0
                temp = 0
                for j in range(6,6-i-1,-1):
                    if array[i-temp][j] == x :
                        count +=1
                    else:
                        score = score + self.adding2(count)
                        count = 0
                    temp += 1
                score = score + self.adding2(count)
            
      
        for j in range(3,6):
                count = 0
                temp = 0
                for i in range(5,5-j-1,-1):
                    if array[i][j-temp] == x :
                        count +=1
                    else:
                        score = score + self.adding2(count)
                        count = 0
                    temp += 1
                score = score + self.adding2(count)
        return score

    def get_heuristic(self,state,x):
        bit_manp = bit()
        arr_state = bit_manp.IntToarr2d(state)
        # print("arr_state: " , end="")
        # print(arr_state)
        self.solOfplayer = [0,0,0]
        res1 = self.get_heuristic_red(arr_state,1)
        self.solOfplayer = [0,0,0]
        # print("res1:", end="")
        # print(res1)
        res2 = self.get_heuristic_red(arr_state,2)
        # print(f"res1 {res1}")
        # print(f"res2 {res2}")
        # print("res2:", end="")
        # print(res2)
        temp1 = (10*res1[2] + 3*res1[1] + res1[0]) - (8*res2[2] + 3*res2[1] +  res2[0])
        res1= [0,0,0]
        res2 = [0,0,0]
        return temp1




# state = [[1,2,0,0,1,1,2],
#         [1,1,1,2,2,1,2],
#         [2,2,1,2,1,2,1],
#         [1,1,2,2,2,2,1],
#         [1,2,1,1,1,2,1],
#         [1,2,2,1,2,1,2]]

# arr = [[1,0,0,0,0,0,0],
#        [2,1,0,0,0,0,0],
#        [2,2,1,0,0,0,0],
#        [1,1,2,1,0,0,0],
#        [2,1,2,2,1,0,0],
#        [1,2,2,1,2,0,0]]
# test = heuristic()
# test.get_heuristic(arr,True)
# print(test.getScore(arr,1))
# print(test.getScore(arr,2))