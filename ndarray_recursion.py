def ndarray_recursion(a_array,shape_array,n=0):
    if len(shape_array)>=2:
        if(n==len(shape_array)-2):
            return '['+(',').join([ str(x) for x in a_array])+']'
        return '['+','.join([ndarray_recursion(a_array[x],shape_array,n+1) for x in range(shape_array[n])])+']'
    else:
        return '['+(',').join([ str(x) for x in a_array])+']'

if __name__ == '__main__':
    a=[[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]],[[5,5,5],[6,6,6]]]
    b=[1,2,3]
    print(ndarray_recursion(a,[3,2,3]))
    print(ndarray_recursion(b,[3,]))
