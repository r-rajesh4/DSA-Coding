class Solution:
	def findSmallest(self, nums):
		# Your code goes here
            min=nums[0]
            for i in nums:
                if i<=min:
                    min=i
            return min
s=Solution()
print(s.findSmallest([-10,1,5,6,-11]))