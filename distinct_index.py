def distinct_index(array, start, end):
    if start > end:
        return [False, -1]

    middle_index = end if (end == start) else int((end + start) / (2))

    a = distinct_index(array, start, middle_index - 1)

    if a[0] == 1:
        return list(a)
    elif array[middle_index] == middle_index:
        return [True, middle_index] if (a[0] == 0) else a
    else:
        b = distinct_index(array, middle_index + 1, end)
        if b[0] == 1:
            return list(b)
        else:
            return [False, -1]

cases=int(input())
while cases>0:
    array= list(map(int,input().split()))
    distinct,index= distinct_index(array,0,len(array)-1)
    print(str(distinct)+", "+str(index))
    cases-=1