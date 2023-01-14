class Man:
    height=187
    age=21
    satiety=100

class Auto(Man):
    Height=2.1
    weight=2200
    width=2

class Lamborghini(Auto):
    speed=305

    def __init__(self):
        print(self.height)
        print(self.weight)
        print(self.width)
        print(self.speed)
nick=Lamborghini()


class Man:
    def __init__(self):
        print("My car is beautiful")

class Auto(Man):
    def __init__(self):
        super().__init__()
        print("Yeah, it`s True!")
hol=Auto()