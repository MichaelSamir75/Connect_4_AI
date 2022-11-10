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
        for i in range (6):
            self.adding(count)
            count = 0
            for(j) in range (7):
                if arr_state[i][j] == x:
                    count += 1
                else:
                    self.adding(count)
                    count = 0
        count = 0
        for j in range (7):
            self.adding(count)
            count = 0
            for i in range (6):
                if arr_state[i][j] == x:
                    count = count + 1
                else:
                    self.adding(count)
                    count = 0
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
        return score

    def get_heuristic(self,state,x):
        bit_manp = bit()
        arr_state = bit_manp.IntToarr2d(state)
        res1 = self.get_heuristic_red(arr_state,1)
        self.solOfplayer = [0,0,0]
        print(res1)
        res2 = self.get_heuristic_red(arr_state,2)
        print(res2)
        if x == 1:
            temp1 = (5*res1[2] + 4*res1[1] + 3 * res1[0]) - (5*res2[2] + 4*res2[1] + 3 * res2[0])
            return temp1
        elif x == 0:
            temp1 = (5*res2[2] + 4*res2[1] + 3 * res2[0]) - (5*res1[2] + 4*res1[1] + 3 * res1[0])
            return temp1