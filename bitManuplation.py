class bit:
    def arr2dToInt(self,array):
        x=""
        flag = False
        for i in range (7):
            count = 7
        # x=x+"     "
            for j in range(6):
                count = count -1
                if array[j][i] != 0:
                    flag = True
                    if(count == 1):
                        x = x +"100"
                    elif(count == 2):
                        x= x +"010"
                    elif(count == 3):
                        x= x +"110"
                    elif(count == 4):
                        x= x +"001"
                    elif(count == 5):
                        x= x +"101"
                    elif(count == 6):
                        x= x +"011"
                    break
            if(not(flag)):
                x= x +"000"
            flag = False
            for k in range (5,0,-1):
                if array[k][i] == 2:
                    x = x +"0"
                elif array[k][i] == 1:
                    x = x+ "1"
                else:
                    x = x + "0"
            x = x+ "0"
        y = x[::-1]
        print(y)
        return self.binaryToDecimal(int(y))
    
    def DecimalToBinary(self,num):
        return bin(num).replace("0b", "")

    def binaryToDecimal(self,binary):
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return decimal   

    def IntToarr2d(self,long):
        long = self.DecimalToBinary(long)
        zeros = [[0 for i in range(7)] for j in range(6)]
        c = 0
        long = str(long)
        flag = False
        for h in range(len(long),63,1):
            long = "0" + long
        for i in range (len(long)-1,0,-9):
            temp = long[i-2] + long[i-1]+ long[i]
            temp = self.binaryToDecimal(int(temp))
            if temp == 0:
                c = c+1
                continue
            if(temp == 1): t = 4;
            elif(temp == 2): t = 3;
            elif(temp == 3): t = 2;
            elif(temp == 4): t = 1;
            elif(temp == 5): t = 0;
            elif(temp == 6): t = -1;
            counter = 0
            for j in range(5,t,-1):
                    if int(long[i-counter-3]) == 1:
                        zeros[j][c] = 1
                    elif int(long[i-counter-3]) == 0:
                        zeros[j][c] = 2
                    counter = counter + 1
            c = c+1
            
        return zeros

# arr = [[0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,1,0,0,0],
#        [1,0,2,1,2,0,2]]
# obj = bit()
# x=obj.arr2dToInt(arr)
# print(x)
# final = obj.IntToarr2d(x)
# print(final)
# print(arr)