def stack_count(arr):
    position_array=[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]!=0:
                position_array.append((i,j))
    all_matrix=[[position_array.pop(0)]]
    remove_list=[]
    while position_array:
        for i in position_array:
            for j in all_matrix:
                if (i[0]-1,i[1]) in j or (i[0],i[1]-1) in j or (i[0]+1,i[1]) in j or (i[0],i[1]+1) in j:
                    j.append(i)
                    remove_list.append(i)
                    break
        if remove_list:
            position_array=list(set(position_array)-set(remove_list))
            remove_list=[]
        else:
            all_matrix.append([position_array.pop(0)])
    return len(all_matrix)