class Solution:
	def removeDuplicates(self, nums):
		# Your code goes here
            tnum=[]
            for i in nums:
                if i not in tnum:
                    tnum.append(i)
            return tnum
s=Solution()
print(s.removeDuplicates([3,3,4,]))
