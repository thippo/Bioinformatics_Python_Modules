def denoise(arr,n=3):
    import numpy as np
    noise_list=[]
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr[0])-1):
            if sum([arr[i+k][j+l] for k in (-1,0,1) for l in (-1,0,1)]) < n:
                noise_list.append((i,j))
    for i in range(1,len(arr)-1):
        if sum([arr[i+k][0+l] for k in (-1,0,1) for l in (0,1)]) < n-1:
            noise_list.append((i,0))
    for i in range(1,len(arr)-1):
        if sum([arr[i+k][len(arr[0])-1+l] for k in (-1,0,1) for l in (-1,0)]) < n-1:
            noise_list.append((i,len(arr[0])-1))
    for i in range(1,len(arr[0])-1):
        if sum([arr[0+k][i+l] for k in (0,1) for l in (-1,0,1)]) < n-1:
            noise_list.append((0,j))
    for i in range(1,len(arr[0])-1):
        if sum([arr[len(arr)-1+k][i+l] for k in (-1,0) for l in (-1,0,1)]) < n-1:
            noise_list.append((len(arr)-1,j))
    if sum([arr[0+k][0+l] for k in (0,1) for l in (0,1)]) < n-1:
        noise_list.append((0,0))
    if sum([arr[0+k][len(arr[0])-1+l] for k in (0,1) for l in (-1,0)]) < n-1:
        noise_list.append((0,len(arr[0])-1))
    if sum([arr[len(arr)-1+k][0+l] for k in (-1,0) for l in (0,1)]) < n-1:
        noise_list.append((len(arr)-1,0))
    if sum([arr[len(arr)-1+k][len(arr[0])-1+l] for k in (-1,0) for l in (-1,0)]) < n-1:
        noise_list.append((len(arr)-1,len(arr[0])-1))
    for i in noise_list:
        arr[i[0]][i[1]]=0
    return arr