class Human:
    def __init__(self,name="Human"):
        self.name=name

class Animal:
    def __init__(self, animal):
        self.animal=animal
        self.friend=[]

    def add_friend(self, human):
        self.friend.append(human)
    def print_friend_names(self):
        if self.friend!=[]:
            print(f" Names of {self.animal} friends ")
            for friend in self.friend:
                print(friend.name)
        else:
            print(f" There are no friend in {self.animal} ")

alex=Human("Alex")
anna=Human("Anna")
dog=Animal("Jack")
dog.add_friend(alex)
dog.add_friend(anna)
dog.print_friend_names()