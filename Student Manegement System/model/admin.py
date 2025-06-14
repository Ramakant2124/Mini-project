from .teacher import Teacher

class Admin(Teacher):
    def __init__(self,n,a,i,sub,sal,d):
        self.aid=i
        self.dept=d
        super().__init__(n,a,i,sub,sal)
    def showadmin(self):
        super().showteacher()
        print(f"Admin Department : {self.dept}")
