# class Solution(object):
#     def isThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         count=0
#         for i in range (1,n+1):
#             if n%i==0:
#                 count +=1
#         if count ==3:
#             return True
#         else:
#             return False
        
# s=Solution()
# r=s.isThree(23)
# print(r)        



class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=0
        i=1
        for i in range (1,n,i*i):
            if n%i==0:
                count +=2
            if i*i==n:
                count -=1
        if count ==3:
            return True
        else:
            return False
        
s=Solution()
r=s.isThree(4)
print(r)        
