def partition(copied_array,start,end):
    pivot_index = start 
    pivot= copied_array[start]
    for i in range(start+1,end+1):
        if(copied_array[i] <= pivot):
            copied_array[pivot_index]=copied_array[i]
            copied_array[i]=copied_array[pivot_index+1]
            copied_array[pivot_index+1]=pivot
            pivot_index+=1
    return pivot_index

    
def kthsmallest(copied_array, start, end, k):
    if(start>=end):
        return copied_array[start]
        
    root= partition(copied_array,start,end)
    
    number_of_right_elements=root-start+1
    
    if (number_of_right_elements==k):
        return copied_array[root]
    elif (number_of_right_elements>k):
        return kthsmallest(copied_array, start, root-1, k)
    else:
        return kthsmallest(copied_array, root+1, end, k-number_of_right_elements) 
    

cases=int(input())
while cases>0:
    array= list(map(int,input().split()))
    k=int(input())
    copied_array=array.copy()
    element= kthsmallest(copied_array, 0, len(copied_array)-1, k)
    index= array.index(element)
    print(str(element)+", "+str(index))
    cases-=1