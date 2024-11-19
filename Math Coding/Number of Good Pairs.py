# Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums):
            temp=[0]*101
            sum=0
            for i in nums:
                temp[i] +=1
            for j in temp:
                sum +=(j*(j-1))//2
            return sum
                
sol=Solution()
print(sol.numIdenticalPairs([1,1,1,1]))