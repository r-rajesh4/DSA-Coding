class Solution:
    def largestandsecondlargest(self,arr):
        max=0
        second_max=0
        for i in arr:
            if i=>max:
                second_max=max
                max=i
        return max,second_max
    
s=Solution()
print(s.largestandsecondlargest([2,1,4,2,6,3,7,9,15,21]))
