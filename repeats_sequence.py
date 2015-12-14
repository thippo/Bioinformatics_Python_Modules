def repeats_sequence(seq_list,length):
    '''
    parameters:
    seq_list: must be list or tuple with string
    length: the length of sequence you want

    return:
    repeats_dict
    '''
    repeats_dict={}
    for i in seq_list:
        for j in range(0,len(i)-length+1):
            if i[j:j+length] not in repeats_dict.keys():
                repeats_dict[i[j:j+length]]=1
            else:
                repeats_dict[i[j:j+length]]+=1
    return repeats_dict