class Solution:
	def countDigits(self, num):
            count = 0
            temp=num
            while temp!=0:
                a=temp%10
                if a==0:
                    pass
                else:
                    if num%a==0:
                        count +=1
                temp=temp//10
            return count 
        

solution = Solution()
num = 1012  
result = solution.countDigits(num)
print(f"Number of digits in {num} that divide {num} evenly: {result}")