class Bank:
    id=0
    name=""
    bal=0.0
    def addacu(self,i,n,b):
        self.id=i
        self.name=n
        self. bal=b
    def Depo(self,a):
        self. bal+=a
        print("Total balance :",self. bal)
    def withdr(self,a):
        self. bal-=a
        print("Total balance :",self. bal)
    def accshow(self):
        print("Acount ID :",self.id)
        print("Acount name :",self.name)
        print("Acount  bal :",self. bal)
o=Bank()
ch=0
while ch!=5:
    ch=int(input("\nEnter your choice :\n1.Acount created\t2.deposit\n3.Withdraw\t4.show Acount\n5.exits"))
    if ch==1:
        i=int(input("\nEnter your id :"))
        n=input("\nEnter your name :")
        b=int(input("\nEnter your  bal Amount :"))
        o.addacu(i,n,b)
        
    elif ch==2:
        a=float(input("\nEnter your Deposit Amount :"))
        o.Depo(a)
    elif ch==3:
        a=float(input("\nEnter your Withdraw Amount : "))
        if a>o.bal:
            print("Insufisunt Bal")
        else:
            o.withdr(a)
            print("Amount Withdraw")
    elif ch==4:
        o.accshow()
    elif ch==5:
        print("\nExitings")
    else:
        print("\nenter ypur choie")
            
    

       
    
        

    
