def reverse_strand(seq):
    return ''.join([dict(zip(('A','T','C','G'),('T','A','G','C'))).get(x,x) for x in seq])[::-1]
