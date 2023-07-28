from functions import load, add
from datetime import date, timedelta
import random

def generate_random_cars(count):
    car_models = [
        "Toyota",
        "Honda",
        "Ford",
        "Chevrolet",
        "BMW",
        "Nissan",
        "Kia",
        "Ferrari",
        "Volvo",
        "Jeep",
        "Mazda",
        "Subaru",
        "Audi",
        "Hyundai",
        "Lamborghini",
        "Porsche"
    ] 
    car_colors = [
        "Red",
        "Blue",
        "Green",
        "Yellow",
        "Black",
        "White",
        "Gray",
        "Silver",
        "Orange",
        "Purple",
        "Brown",
        "Pink",
        "Gold",
        "Beige"
    ]
    car_owners = [
        "Noam Levi",
        "Maya Cohen",
        "Yair Mizrahi",
        "Tamar Biton",
        "Eitan Dayan",
        "Shira Azulay",
        "Itai Katz",
        "Noya Ben David",
        "Adi Avrahami",
        "Yael Vashitz",
        "Omer Ben-Zvi",
        "Or Tal",
        "Nir Kagan",
        "Talia Leshem",
        "Nadav Harel",
        "Guy Gidron",
        "Avishy Grundman",
        "Liora Bin"
    ]

    current_year = date.today().year

    for i in range(count):
        name = random.choice(car_models)
        year = random.randint(1985, current_year)
        color = random.choice(car_colors)
        number = ''.join(random.choices('0123456789', k=6))
        owner = random.choice(car_owners)
        last_visit = date.today() - timedelta(days=random.randint(1, 3650))
        last_fixup = (last_visit - timedelta(days=random.randint(1, 3650))).strftime("%d-%m-%Y")
        last_visit = last_visit.strftime("%d-%m-%Y")

        add(name, year, color, number, owner, last_visit, last_fixup)

#generate_random_cars(40)

def no_fixup_ten_last_years():
    no_fixuped_cars = []
    cars = load()
    for car in cars:
        if int(car.last_fixup[-4:]) < 2013:
            no_fixuped_cars.append(car)
            print(car.name, car.last_fixup)

no_fixup_ten_last_years()


