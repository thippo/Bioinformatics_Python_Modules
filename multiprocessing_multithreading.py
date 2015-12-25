python多进程：
from multiprocessing import Pool
if __name__=='__main__':
    p = Pool(processes=int)
    for xxxxxx in xxxxxx_list:
        p.apply_async(function, args=(xxxxxx,))
    p.close()
    p.join()

python多线程：
import threading
threads_list=[]
t1=threading.Thread(target=function,args=(xxx,))
threads_list.append(t1)
t2=threading.Thread(target=function,args=(xxx,))
threads_list.append(t2)
if __name__=='__main__':
    for t in threads_list:
        t.setDaemon(True)
        t.start()
    t.join()