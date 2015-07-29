#writen by thippo
#python version 3.4.3

class Find_Gene_Position():
'''
position_tuple=('+/-',position_min,position_max)
'''
	import re

	def __init__(self,gff_file):
		self.element_list=[]
		with open(gff_file) as file:
			for i in file:
				if 'RefSeq	gene' in i:
					r1=self.re.findall('(Scaffold[0-9]*?)	glimmer',i)
					r2=self.re.findall('glimmer	gene	([0-9]*?)	',i)
					r3=self.re.findall('	([0-9]*?)	\.	',i)
					r4=self.re.findall('	ID=(Bacillus.sp.T61GL[0-9]{6});Name',i)
					self.element_list.append([r1[0],r4[0],r2[0],r3[0]])
				elif 'RefSeq	exon' in i:
					r1=self.re.findall('(Scaffold[0-9]*?)	glimmer',i)
					r2=self.re.findall('RefSeq	exon	([0-9]*?)	',i)
					r3=self.re.findall('	([0-9]*?)	\.	',i)
					r4=self.re.findall('	ID=(Bacillus.sp.T61GL[0-9]{6});Name',i)
					self.element_list.append([r1[0],r4[0],r2[0],r3[0]])

	def find_gene_downstream(self,position_tuple):
		if '-' in position_tuple:
			n='inside'
			for i in self.element_list:
				if ((int(i[1].strip())-int(position_tuple[1])<0 and int(i[2].strip())-int(position_tuple[1])>0) or (int(i[1].strip())-int(position_tuple[2])<0 and int(i[2].strip())-int(position_tuple[2])>0)):
					return 'inside'
				else:
					if (int(i[2].strip())-int(position_tuple[1]))>0:
						return n
					else:
						n=i[0]
		else:
			for i in self.element_list:
				if ((int(i[1].strip())-int(position_tuple[1])<0 and int(i[2].strip())-int(position_tuple[1])>0) or (int(i[1].strip())-int(position_tuple[2])<0 and int(i[2].strip())-int(position_tuple[2])>0)):
					return 'inside'
				else:
					if (int(i[1].strip())-int(position_tuple[2]))>0:
						return i[0]

	def find_gene_upstream(self,position_tuple):
		if '-' in position_tuple:
			n='inside'
			for i in self.element_list:
				if ((int(i[1].strip())-int(position_tuple[1])<0 and int(i[2].strip())-int(position_tuple[1])>0) or (int(i[1].strip())-int(position_tuple[2])<0 and int(i[2].strip())-int(position_tuple[2])>0)):
					return 'inside'
				else:
					if (int(i[1].strip())-int(position_tuple[2]))>0:
						return i[0]
		else:
				for i in self.element_list:
					if ((int(i[1].strip())-int(position_tuple[1])<0 and int(i[2].strip())-int(position_tuple[1])>0) or (int(i[1].strip())-int(position_tuple[2])<0 and int(i[2].strip())-int(position_tuple[2])>0)):
						return 'inside'
					else:
						if (int(i[2].strip())-int(position_tuple[1]))>0:
							return n
						else:
							n=i[0]
					
if 'Minus' in i:
    gene_name_down=find_gene_downstream(('-',position_min_list[0],position_max_list[0]))
    gene_name_up=find_gene_upstream(('-',position_min_list[0],position_max_list[0]))
else:
    gene_name_down=find_gene_downstream(('+',position_min_list[0],position_max_list[0]))
    gene_name_up=find_gene_upstream(('+',position_min_list[0],position_max_list[0]))