class A:
    def fun(self):
        print("This is fun1 in class A")
        
    def fun2(self):
        print("This is fun2 in class A")
        
class B:
    def fun(self):
        print("This is fun3 in class B")
        
    def fun4(self):
        print("This is fun4 in class B")

class C(A,B):
    def fun5(self):
        print("This is fun5 in class C")
        
    def fun6(self):
        print("This is fun6 in class C")

a = A()
b = B()
c = C()
c.fun()