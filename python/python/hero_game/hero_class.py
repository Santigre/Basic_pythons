class hero:
    name = ""
    health = 10
    attack = 3

    def __init__(self,myname):
        self.name = myname

    def get_name(self):
        print self.name
        
