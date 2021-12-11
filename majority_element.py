
def majority_element(array):
    max_index=0
    count=0
    n=len(array)
    for i in range(0,n):
        if (array[i] == array[max_index]):
            count+=1
        else:
            count-=1
        if (count==0):
            max_index=i
            count=1
    count=0
    for i in range (0,n):
        if (array[i] == array[max_index]):
            count+=1
    if (count > (n/2)):
        return array[max_index]
    else:
        return -1
    

cases=int(input())
while cases>0:
    array= list(map(int,input().strip().split()))[:]
    majority= majority_element(array)
    print(majority)
    cases-=1