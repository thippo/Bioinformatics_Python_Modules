def getORF(sequence,frame):
    '''
    parameters:
    sequence: must be 'ATCG'
    frame: must be list or tuple with 0,1,2

    return:
    max_index,max_le,max_seq
    '''
    orfs = {}
    max_le=0;max_index=0

    for j in frame:
        start_codon_index = 0
        end_codon_index = 0
        start_codon_found = False
        for indx in range(j, len(sequence), 3):
            current_codon = sequence[indx:indx+3]
            if current_codon == 'ATG' and not start_codon_found:
                start_codon_found = True
                start_codon_index = indx
            if current_codon in ['TAA','TAG','TGA'] and start_codon_found:
                end_codon_index = indx
                le = end_codon_index - start_codon_index + 3
                if le >= max_le:
                    max_le=le
                    max_index=start_codon_index
                start_codon_found = False
    max_seq=sequence[max_index:max_index+max_le]
    return max_index,max_le,max_seq