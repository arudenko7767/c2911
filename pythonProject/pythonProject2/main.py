#class Human:
    #height=180

#class Student(Human):
    #satiety=0
#class Worker(Human):
    #satiety=100

#alex=Student()
#robert=Worker()
#print(alex.satiety)
#print(robert.satiety)


#class Grandparents:
    #height=170
    #age=60
    #satiety=100

#class Parents(Grandparents):
    #age=40

#class Child(Parents):
    #height=50
    #def __init__(self):
        #print(self.height)
        #print(self.satiety)
        #print(self.age)
#nick=Child()



#class Grandparents:
    #def __init__(self):
        #print("Hello")


#class Parents(Grandparents):
    #def __init__(self):
        #super().__init__()
        #print("World")
#hol=Parents()



class Computer:
    def calculator(self):
        print("Обчислення...")

class Display:
    def display(self):
        print("Я показую інформацію на дисплеї")

class Smartphone(Computer, Display):
    pass

iphone=Smartphone()
iphone.calculator()
iphone.display()