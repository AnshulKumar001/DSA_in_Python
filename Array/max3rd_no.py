class Solution(object):
    def MaxProduct(self,nums):
        duplicate=list(set(nums)) #upicate number remove only save alternate number 
        duplicate .sort()
        return duplicate[-3] if len(duplicate) >=3 else 0

nums = [3,4,5,9,9,7,2]

obj = Solution()
print(obj.MaxProduct(nums))