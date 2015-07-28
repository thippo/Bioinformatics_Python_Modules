#writen by thippo
#python version 3.4.3

def get_fasta_dict(filename):
	'''
	处理fasta格式文件
	
	输入：文件名称
	输出：以'>'行为键，其他行连接成一条去除换行符的字符串为值的一个字典
	'''
	seq_dict={}
	with open(filename,'r') as file:
		for i in file:
			if '>' in i:
				tmp_i=i.rstrip()
				seq_dict[tmp_i]=''
			else:
				seq_dict[tmp_i] += i.rstrip()
	return seq_dict
