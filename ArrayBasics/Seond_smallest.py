class Solution:
	def secondSmallest(self, nums) :
		# Your code goes here
            
            min=nums[0]
            second_min=nums[1]

            for i in range(2,len(nums)):
                if nums[i]<min:
                    second_min=min
                    min=nums[i]
                elif nums[i]<second_min and nums[i]!=min:
                    second_min=nums[i]
            return second_min
                


s=Solution()
print(s.secondSmallest( [1,2,1,4,6]))