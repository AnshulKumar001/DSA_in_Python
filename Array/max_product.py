class Solution(object):
    def MaxProduct(self,nums):
        nums.sort()
        return nums[-1]*nums[-2]

nums = [3,4,5,2]

obj = Solution()
print(obj.MaxProduct(nums))        