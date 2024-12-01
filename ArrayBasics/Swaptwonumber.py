class Solution:
    def Swap(self, a,b):
         #addtion subtraction
            # a=a+b
            # b=a-b
            # a=a-b
            # division multiplication
            # a=a*b
            # b=a//b
            # a=a//b
            #xor
            a=a^b
            b=a^b
            a=a^b

            return a,b
s=Solution()
print(s.Swap(4,5))