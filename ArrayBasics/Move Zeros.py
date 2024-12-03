class Solution:
	def moveZeros(self, nums):
		# Your code goes here
            i=0
            j=0
            for i in range(0,len(nums)):
                if nums[i]!=0 :
                    nums[i],nums[j]=nums[j],nums[i]
                    j=j+1
            return nums
s=Solution()
print(s.moveZeros([0,1,0,0,2,0,3,0,0,0,0,12]))
