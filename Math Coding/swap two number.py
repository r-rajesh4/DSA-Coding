class Solution:
    def swapNumbers(self, a, b):
        a=a+b
        b=a-b
        a=a-b
        return a,b
s=Solution()
print(s.swapNumbers(34,45))