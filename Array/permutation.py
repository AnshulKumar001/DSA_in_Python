class Solution:
    def permutaton(self,s1:str,s2)->bool:
        s1_sorted=sorted(s1)
        s1_len=len(s1)
        s2_len=len(s2)
        for i in range (s2_len-s1_len+1):
            sub_string=s2[i:i+s1_len]
            if sorted(sub_string)==s1_sorted:
                return True
            else:
                return False
          



sol=Solution()
print(sol.permutaton("ab","abcdef"))  
print(sol.permutaton("ab","aebcdef"))        