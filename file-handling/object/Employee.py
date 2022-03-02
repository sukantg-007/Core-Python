class Employee:
    def __init__(self,eid,ename,esal,eaddr):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("EID : {} ENAME : {} ESAL : {} EADDR : {}".format(self.eid,self.ename,self.esal,self.eaddr))