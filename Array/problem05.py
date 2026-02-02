#(504). Base 7

'''

Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"
 '''






class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        sign = "-" if num < 0 else ""
        num = abs(num)
        res = ""
        
        while num > 0:
            res = str(num % 7) + res
            num //= 7
        
        return sign + res
