class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		# Your code goes here
            sum=0
            product=1
            while n!=0:
                a=n%10
                sum +=a
                product *=a
                n=n//10
            return product-sum
