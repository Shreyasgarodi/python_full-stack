class car:
    def __init__(self,suv,hatchback):
        self.suv=suv
        self.hatchback=hatchback
    def display(self):
     print(self.suv,self.hatchback)
bmw=car('x1','x3')
audi=car('q7','q9')
bmw.display()
audi.display()
