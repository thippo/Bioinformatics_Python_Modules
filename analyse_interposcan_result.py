#writen by thippo
#python version 3.4.3

def analyse_interposcan_result(file_in,remove_repeat='T'):
    pfam_description={}
    protein_pfam={}
    pfam_protein={}
	with open(file_in) as filein:
		for line in filein:
			line_list=line.split('	')
			pfam_description[line_list[4]]=line_list[5]
			protein_pfam[line_list[0]]=[]
			pfam_protein[line_list[4]]=[]
		for line in filein:
			line_list=line.split('	')
			protein_pfam[line_list[0]].append(line_list[4])
			pfam_protein[line_list[4]].append(line_list[0])
    outfile_protein_pfams=open('Protein_pfams_'+file_in+".th",'w')
    outfile_pfam_proteins=open('Pfam_proteins_'+file_in+".th",'w')
    if 'T' in remove_repeat:
        for (protein,pfam) in protein_pfam.items():
            for pf in list(set(pfam)):
                outfile_protein_pfams.write(protein+'	'+pf+"	"+pfam_description[pf]+"\n")
            outfile_protein_pfams.write("\n")
        outfile_protein_pfams.close	
        for (pfam,protein) in pfam_protein.items():
            for name in list(set(protein)):
                outfile_pfam_proteins.write(pfam+'	'+name+"	"+pfam_description[pfam]+"\n")
            outfile_pfam_proteins.write("\n")			
        outfile_pfam_proteins.close
    else:
        for (protein,pfam) in protein_pfam.items():
            for pf in pfam:
                outfile_protein_pfams.write(protein+'	'+pf+"	"+pfam_description[pf]+"\n")
            outfile_protein_pfams.write("\n")
        outfile_protein_pfams.close	
        for (pfam,protein) in pfam_protein.items():
            for name in protein:
                outfile_pfam_proteins.write(pfam+'	'+name+"	"+pfam_description[pfam]+"\n")
            outfile_pfam_proteins.write("\n")			
        outfile_pfam_proteins.close