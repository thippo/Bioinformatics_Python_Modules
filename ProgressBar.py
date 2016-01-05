class ProgressBar():
    def __init__(self,count=0,total=0,width=50):
        self.count=count
        self.total=total
        self.width=width
    def __call__(self,message=''):
        import sys
        if message:
            self.count+=1
            position=round(self.width*self.count/self.total)
            sys.stdout.write(message+' '*(self.width+15)+'\n')
            sys.stdout.flush()
            if position==self.width:
                sys.stdout.write('Done!    '+'|'+'#'*position+' '*(self.width-position)+'|  '+str(self.count)+'/'+str(self.total)+'\n')
                sys.stdout.flush()
            else:
                sys.stdout.write('Progress '+'|'+'#'*position+' '*(self.width-position)+'|  '+str(self.count)+'/'+str(self.total)+'\r')
                sys.stdout.flush()
        else:
            self.count+=1
            position=round(self.width*self.count/self.total)
            if position==self.width:
                sys.stdout.write('Done!    '+'|'+'#'*position+' '*(self.width-position)+'|  '+str(self.count)+'/'+str(self.total)+'\n')
                sys.stdout.flush()
            else:
                sys.stdout.write('Progress '+'|'+'#'*position+' '*(self.width-position)+'|  '+str(self.count)+'/'+str(self.total)+'\r')
                sys.stdout.flush()

				
if __name__=='__main__':
    import time
    bar=ProgressBar(total=5)
    for i in range(bar.total):
        bar(str(i+1))
        time.sleep(1)