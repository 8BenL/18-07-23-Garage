from classes import Car
import pickle

def load():
    try:
        with open("cars.pickle", "rb") as f:
            cars=pickle.load(f)
            return cars
    except:
        return []

def add(name:str="name", year:str="year", color:str="color", number:str="number", owner:str="owner", last_visit:str="last_visit", last_fixup:str="last_fixup"):
    cars=load()
    cars.append(Car(name=name, year=year, color=color, number=number, owner=owner, last_visit=last_visit, last_fixup=last_fixup))
    with open("cars.pickle", "wb") as f:
        pickle.dump(cars, f)       

def save(cars:list):
    with open("cars.pickle", "wb") as f:
        pickle.dump(cars, f)

def delete(name,number):
    cars=load()
    for car in cars.copy():
        if car.name==name and car.number==number:
            cars.remove(car)
    save(cars)

def update(name:str="name", year:str="year", color:str="color", number:str="number", owner:str="owner", last_visit:str="last_visit", last_fixup:str="last_fixup"):
    cars=load()
    for car in cars.copy():
        if car.owner==owner:
            cars.remove(car)
    save(cars)
    add(name, year, color, number, owner, last_visit, last_fixup)

def search(query:str):
    results = []
    cars=load()
    for car in cars.copy():
        """if query in car.name or query in car.number:"""
        for value in car.__dict__.values():
            if query in value:
                results.append(car)
                break
    return results
        