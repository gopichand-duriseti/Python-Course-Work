class shopping:
    products=[]
    discount=10 #The attribute that is defined inside class is called class attribute

    @classmethod
    def update(cls,new_discount):
        cls.discount=new_discount
        print(f'{new_discount} is updated')
    @classmethod
    def prod(cls):
        return cls.products
    def __init__(self,name):
        self.name=name
        print(self.name)
class shops(shopping):
    @classmethod
    def shopsclass(cls):
        return super().prod()
    def __init__(self,name):
        super().__init__(name)

s=shopping("gopi")
c=shops("gopal")
print(c.shopsclass())