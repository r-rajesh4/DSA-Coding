class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=max(nums)
        a=min(nums)
        while b!=0:
            a,b=b,a%b
        return a        
s=Solution()
print(s.findGCD([2,5,3,4,10]))