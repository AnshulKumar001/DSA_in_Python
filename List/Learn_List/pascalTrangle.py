class Solution:
    def Pascaltrangle(self,numRow):
       # trangle=[]
        for i in range (numRow):
            row=[1]*[i+1]
            print(row)  


sol=Solution() 
print(sol.Pascaltrangle(5))             