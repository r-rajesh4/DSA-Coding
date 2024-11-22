class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum= n*(n+1)//2
        print("sum is ",sum)
        sumArr=0
        for i in range(0,n):
                sumArr +=i
                print("i",i)
        print("sumArray",sumArr)
        return sum-sumArr
s=Solution()
print(s.missingNumber([3,0,1]))
