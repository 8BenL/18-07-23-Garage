class Car:
    def __init__(self, name:str="name", year:str="year", color:str="color", number:str="number", owner:str="owner", last_visit:str="last_visit", last_fixup:str="last_fixup"):
        self.name=name
        self.year=year
        self.color=color
        self.number=number
        self.owner=owner
        self.last_visit=last_visit
        self.last_fixup=last_fixup


    def __str__(self):
        return f"{self.name},{self.number},{self.owner}"        

    def __repr__(self):
        return f"{self.name}:{self.number}:{self.owner}"        

    

