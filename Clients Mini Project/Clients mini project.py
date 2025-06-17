class Clients:
    def __init__(self,i,n,cn,s,b):
        self.cid=i
        self.name=n
        self.company_name=cn
        self.services=s
        self.budget=b

    def __str__(self):
        return f"\nCID : {self.cid}\nNAME : {self.name},\n COMPANY :{ self.company_name},\nSERVICES :{self.services},\nBUGET :{self.budget}"
c1=Clients(101,"Client1","Company1","FB Marketing",10200)
c2=Clients(102,"Client2","Company2","Web devlopment",45000)
c3=Clients(103,"Client3","Company3","Instagram marketin",25000)
c4=Clients(104,"Client4","Company4","Softawer devloper",452000)

clients_list=[c1,c2,c3,c4]

def show_clients():
    print("\nSHOWING CLIENTS -:")
    print("---------------------------")
    for cli in clients_list:
        print(cli)
    print("---------------------------")    
def add_client():
    i=int(input("Enter your Client ID :"))
    n=input("Enter Client Name :")
    cn=input("Enter Client Comapany Name :")
    s=input("Enter Services :")
    b=float(input("Enter your Budget :"))
    c5=Clients(i,n,cn,s,b)
    clients_list.append(c5)
    print("CLIENT ADDED SUCCESFULLY!")

def find_client(i):
    for cli in clients_list:
        if i==cli.cid:
            return cli
    return False
def delete_client():
    i=int(input("Enter Client ID TO Delets:"))
    cli = find_client(i)
    if cli:
        clients_list.remove(cli)
        print("CLIENT REMOVED SUCCESFULLY!")
    else:
        print("NO SUCH CLIENTS TO REMOVE")

while True:
    ch= int(input("\nENTER YOUR CHOUCE :\n1.ADD CLIENT,\n2.DELETE CLIENT,\n3.SHOW CLIENT,\n4.EXITING......"))
    if ch ==1:
        add_client()
    elif ch ==2:
        delete_client()
    elif ch ==3:
        show_clients()    
    elif ch ==4:
        print("EXITING......")
        break
    else:
        print("INVALID CHOICE")
        
    
