class dog:
    species='firstdog'

    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def info(self):
        return '{} is {} years old'.format(self.name,self.age)
    
    def speak(self,sound):
        return "{}says{}!".format(self.name,sound)

#instance 생성
c=dog('july',4)
d=dog('marry',10)

print(c.info())
print(c.speak('walwal'))
print(d.speak('mungmung'))