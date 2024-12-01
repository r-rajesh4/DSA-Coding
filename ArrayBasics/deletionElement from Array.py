class Solution:
    def DeletionInssertion(self,arr,p):
        # arr.append("None")
        print(arr)
        for i in range(p,len(arr)-1):
            arr[i]=arr[i+1]
        return arr

s=Solution()

print(s.DeletionInssertion([1,2,4,8,7,3,9,5,12],4))
