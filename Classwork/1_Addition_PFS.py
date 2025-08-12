a=10
b=20
print("Addition:",a+b) #Addition: 30
class Art:
    def __init__(self,n):
        self.n=n
    def __add__(self,other):
        return Art(self.n + other.n)
c=Art(5)
c1=Art(10)
c2=Art(20)
print(c + c1 + c2)
