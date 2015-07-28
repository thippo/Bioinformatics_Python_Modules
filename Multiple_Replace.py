#writen by thippo
#python version 3.4.3

def multiple_replace(original,substitution,seq):
	'''
	对一个字符串的多个字符同时做替换
	
	输入：原始替换字符，要替换成的字符，目标对象
	输出：多重替换后的字符串
	
	注：
	1，此函数不能将字符替换为空，如需请先处理字符串后再用此函数
	2，original，substitution两个参数如果不一样长，将取最短的一个长度建字典
	3，如果多次调用此函数，不建议使用此函数
	'''
	return ''.join([dict(zip(original,substitution)).get(x,x) for x in seq])
	