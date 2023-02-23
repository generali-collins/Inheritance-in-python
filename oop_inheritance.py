# Collins Wanga

# A Python program to demonstrate inheritance

class Team():
    

    def __init__(self, name, jersey_num):
        
        self.name = name
        self.jersey_num = jersey_num

# To check if this person is a player
    def Display(self):
        print(self.name, self.jersey_num)


# Player Number
player = Team("Generali",10)
player.Display()
