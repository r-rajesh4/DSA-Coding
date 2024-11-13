class Solution:
	def minimumSum(self, num: int) -> int:
            l = []
            while num !=0:
                g=num%10
                l.append(g)
                num=num//10

            l.sort()
            a=l[0]
            b=l[1]
            c=l[2]
            d=l[3]
            num1=a*10+d
            num2=b*10+c
            return num1+num2