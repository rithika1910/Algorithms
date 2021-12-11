#@start-editable@

def  merge(arr, low, mid, high):
    #counting reverse pair
    count=0
    j = mid+1
    for i in range(low, mid+1):
        while(j<=high and arr[i] > (2*arr[j])):
            j+=1
        count = count + j-(mid+1)
        
    #merging    
    lt=[]
    l,r = low,mid+1
    while(l<=mid and r<=high):
        if (arr[l]<=arr[r]):
            lt.append(arr[l])
            l+=1
        else:
            lt.append(arr[r])
            r+=1
            
    while (l<=mid):
        lt.append(arr[l])
        l+=1
    while (r<=high):
        lt.append(arr[r])
        r+=1
        
    for i in range (low,high+1):
        arr[i] = lt[i-low]
    return count
            
def solution(arr, low, high):
    if (low>=high):
        return 0
    mid = (low + high) // 2
    #left tree
    inv = solution(arr, low, mid)
    #right tree
    inv = inv + solution(arr, mid+1, high)
    inv = inv + merge(arr, low, mid, high)
    return inv
    
    
#@end-editable@


def main():
    N=int(input())    
    arr = list(map(int, input().split(" "))) 
    #sol = Solution()
    count = solution(arr, 0, N-1)
    print(count)
    
    

if __name__ == '__main__':
    main()