import threading
import time

class Mythread(threading.Thread):
    def __init__(self,number,func,args):
        threading.Thread.__init__(self)
        self.number=number
        self.func=func
        self.args=args

    def run(self):
#        print('{} has started'.format(self.getName()))
        print('{} has started'.format(self.number))
        self.func(*self.args)
#        try:
#            if self._target:
#                self._target(*self._args,**self._kwargs)
#        finally:
#            del self._target,self._args,self._kwargs
#        print('{} has complited'.format(self.getName()))
        print('{} has complited'.format(self.number))


def double(number, cycles):
    for i in range(cycles):
        number+=number
    print(number)

#def sleeper(n,name):
#    print('{} решил поспать'.format(name))
#    time.sleep(n)
#    print('{} проснулся'.format(name))

#for i in range(4):
#    t=Mythread(target=sleeper,name='Thread{}'.format(i+1),args=(3,'Thread{}'.format(i+1)))
#    t.start()

threds_list=[]

for i in range(50):
    t=Mythread(number=i+1,func=double,args=[i,3])
    threds_list.append(t)
    t.start()

for t in threds_list:
    t.join()