class person():
    def __init__(self,name):
        self.name = name
    def reveal(self):
        print('My name is {}.'.format(self.name))
        
test = person('Jack')

class hero(person):
    pass

test2 = hero('Deadpool')