"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int2str = str(x)
        if x < 0: 
            rev = "-" + int2str[len(int2str):0:-1]
        elif x >= 0:
            rev = int2str[::-1]
            
        if int(rev) > 2**31 - 1 or int(rev) < -2**31:
            return 0
        
        return int(rev)
    
solution = Solution()
x = 120

print(solution.reverse(x))