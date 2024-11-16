#Prime number check

class Solution:
    def prime(self,num):
        count=0
        i=1
        for i in range(1,num,i*i):
            if num%i==0:
                count +=2
            if i*i == num:
                count -=1
        if count == 2:
            return str(num)+" " +"is a Prime Number"
        else:
            return str(num) +"is Not a prime Number"
        
        
s=Solution()
print(s.prime(2))
            