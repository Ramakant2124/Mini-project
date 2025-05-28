class Clac:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)
        


o=Clac()
ch=0
while ch!=5:
    ch=int(input("\nEnter your Chose :\n1.Add\t2.sub\t3.mul\t4.div\t5.exit\n"))
    a=int(input("\nEnter the frist number :"))
    b=int(input("\nEnter the second number :"))
    if ch==1:
        o.add(a,b)
    elif ch==2:
        o.sub(a,b)
    elif ch==3:
        o.mul(a,b)
    elif ch==4:
        o.div(a,b)
    elif ch==5:
        print("exit")
    
     

 
    
    
