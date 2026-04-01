class Solution:
    def disappeard (self ,nums ):
        for num in nums:
          index=abs(num)-1
          if nums[index]>0:
            nums[index] = -nums[index]
        return [i+1 for i in range(len(nums)) if nums[i]>0]   


sol=Solution()
print(sol.disappeard([4,3,2,7,8,2,3,1]))

