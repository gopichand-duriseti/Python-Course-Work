class number:
    def __init__(self,n):
        self.n=n
    def __sub__(self,other):
        return number(self.n-other.n)
    def __str__(self):
        return f"{self.n}"
n=number(5)
n1=number(10)
n2=number(15)
n3=number(20)
print(n-n1-n2-n3)
