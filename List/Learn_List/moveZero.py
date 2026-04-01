class Solution:
    def moveZero(self,nums):
        j=0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[j] ,nums[i] =nums[i],nums[j]
                j+=1
        return nums
sol=Solution()
print(sol.moveZero([1,0,3,7,0,0,9]))            
            