class Solution:
    def maxelement(self,arr):
        max=0
        for i in arr:
            if i>max:
                max=i
        return max

s=Solution()
print(s.maxelement([2,3,14,4,2,1,9,6,0]))