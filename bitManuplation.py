class bit:
    
    def arr2dToInt(self,arr,row,col):
        x=""
        for  i in range(row):
            for j in range(col):
                if arr[i][j] == 2:
                    x = x + str(self.DecimalToBinary(arr[i][j]))
                else:
                    x = x + "0"+str(self.DecimalToBinary(arr[i][j]))

        x = int(x)
        x = self.binaryToDecimal(x)
        return x

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

    def IntToarr2d(self,long , row,col):
        long = self.DecimalToBinary(long)
        zeros = [[0 for i in range(col)] for j in range(row)]
        print(zeros)
        long = str(long)
        r=row-1
        c=col-1
        print(long[len(long)-2])
        for i in range(len(long)-1,0,-2):
            if True:
                if long[i-1]=="0" and long[i]=="0":
                    zeros[r][c] = 0      
                elif long[i-1]=="1" and long[i]=="0":
                    zeros[r][c] = 2
                else:
                    zeros[r][c] = 1 

            if c == 0:
                r = r -1
                c = col-1
            else:
                c =c - 1
        return zeros



# arr = [[2,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,0,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,2,1,2,0,2]]
# obj = bit()
# x=obj.arr2dToInt(arr,6,7)
# final = obj.IntToarr2d(x,6,7)
# print(final)