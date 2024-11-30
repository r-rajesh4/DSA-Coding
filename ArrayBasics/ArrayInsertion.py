class Solution:
    def ArrInssertion(self,arr,p,num):
        arr.append("None")
        for i in range(len(arr)-1,p-1,-1):
            arr[i]=arr[i-1]
            if i ==p:
                arr[i]=num
                break;
        return arr

s=Solution()
print(s.ArrInssertion([1,2,4,8,7,3,9,5,12],3,56))
