
    
class note():
    def __init__(self,work=[],life=[]):
        self.work = work
        self.life = life

class user():
    def __init__(self,name,notes=note()):
        self.name = name
        self.notes = notes


test = user('A')
