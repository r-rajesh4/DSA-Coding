# Count Operations to Obtain Zero
class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        step=0
        while num1 and num2:
            if num2 >num1 :
                num2 = num2-num1
            else:
                num1= num1-num2
            step +=1
        return step
        
s=Solution()
print(s.countOperations(2,3))