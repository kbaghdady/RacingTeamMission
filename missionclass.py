class animal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def introduce(self):
        print('I am ',self.name,'my age is ',self.age,'my color is ',self.color)
    def changename(self,newname):
        self.name=newname
    def getname(self):
        return self.name

class dog(animal):
    def __init__(self,name,age,color):
        super().__init__(name,age,color)
        self.type='dog'
        self.breed=None
    def setbreed(self,breed):
        self.breed=breed
    def getbreed(self):
        return self.breed
    def setvaccinated(self,vaccinated):
        self.vaccinated=vaccinated
    def getvaccinated(self):
        return self.vaccinated


class cat(animal):
    def __init__(self,name,age,color):
        super().__init__(name,age,color)
        self.haircut=None
        self.caneatalone=None
    @property
    def haircut(self,YesOrNo):
        self.haircut=YesOrNo
    @property
    def caneatalone(self,YesOrNo):
        self.caneatalone=YesOrNo
    

