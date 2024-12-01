class Solution:
    def reverseArray(self, arr):
            i=0
            j=len(arr)-1
            print(arr)
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i +=1
                j -=1

            return arr
s=Solution()
print(s.reverseArray([2,5,8,9,6,4]))