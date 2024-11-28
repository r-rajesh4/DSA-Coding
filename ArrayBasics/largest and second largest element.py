class Solution:
	def secondLargest(self, nums) -> int:
		# Your code goes here
            max=float('-inf')
            sec=float('-inf')
            for i in range (0,len(nums)):
                if nums[i]>max:
                    sec=max
                    max=nums[i]
                elif nums[i]>sec and nums[i]!=max:
                    sec=nums[i]

            return sec
            

    
s=Solution()
print(s.secondLargest([2,1,4,2,6,3,7,9,15,21,20]))