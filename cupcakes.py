from abc import ABC, abstractmethod
import csv
from pprint import pprint

class Cupcake(ABC):

    size = 'regular'
    def __init__(self, image, name, flavor, price, gluten, limited, calories):
        self.image = image
        self.name = name
        self.flavor = flavor
        self.price = price
        self.gluten = gluten
        self.limited = limited
        self.calories = calories
        self.frosting = []

    def add_frosting(self, *args):
        for frost in args:
            self.frosting.append(frost)

    @abstractmethod
    def calculate_price(self, quantity):
        if quantity >= 8:
            return (self.price * quantity) *0.75
        elif quantity >=4:
            return (self.price * quantity) *0.85
        else:
            return self.price * quantity

class Mini(Cupcake):
    size = "mini"
    def calculate_price(self, quantity):
        if quantity >=12:
            return (self.price * quantity) *0.75
        elif quantity >=6:
            return (self.price * quantity) *0.85
        else:
            return self.price * quantity

class Regular(Cupcake):
    size = "Regular"
    def calculate_price(self, quantity):
        if quantity >= 8:
            return (self.price * quantity) *0.75
        elif quantity >=4:
            return (self.price * quantity) *0.85
        else:
            return self.price * quantity

class Large(Cupcake):
    size = "Large"

    def calculate_price(self, quantity):
        if quantity >= 4:
            return (self.price * quantity) *0.75
        elif quantity >=2:
            return (self.price * quantity) *0.85
        else:
            return self.price * quantity


#_________CUPCAKE____________
cupcake_1 = Mini("cherry.jpg", "Cherry Almond Euphoria", "Almond Cake", 1.68, False, False, 130)
cupcake_2 = Mini("caramel-swirl.jpg", "Caramel Swirl Delight", "Chocolate", 1.98, False, False, 185)
cupcake_2.add_frosting("Caramel", "Cream")
cupcake_3 = Regular("lemon.jpg", "Zesty Lemon Meringue Burst", "Yellow Cake", 2.48, True, False, 260)
cupcake_3.add_frosting("Lemon Meringue")
cupcake_4 = Regular("mint.PNG", "Midnight Mint Madness", "Chocolate/Mint", 2.88, False, True, 320)
cupcake_4.add_frosting("Peppermint")
cupcake_5 = Regular("coconut.jpg", "Tropical Coconut Dream", "White Cake", 2.48, True, True, 220)
cupcake_5.add_frosting("Coconut")
cupcake_6 = Regular("hazel.jpg", "Hazelnut Heaven Surprise", "Hazelnut Cake", 2.48, False, False, 200)
cupcake_7 = Large("berry.jpg", "Velvet Raspberry Bliss", "Velvet Cake", 3.28, True, True, 300)
cupcake_7.add_frosting("Raspberry")
cupcake_8 = Large("crunch.jpg", "Salted Caramel Crunch Delight", "Almond Cake", 3.28, False, False, 300)
cupcake_8.add_frosting("Caramel")

cupcake_stock = [
    cupcake_1, cupcake_2, cupcake_3, cupcake_4, cupcake_5, cupcake_6, cupcake_7, cupcake_8
]


# ________________ CSV file management ________________
def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

def append_csv(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "flavor", "price", "gluten", "limited", "calories", "frosting"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "price": cupcake.price, "gluten": cupcake.gluten, "limited": cupcake.limited, "calories": cupcake.calories, "frosting": cupcake.frosting})

def write_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["image", "size", "name", "flavor", "price", "gluten", "limited", "calories", "frosting"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()


        for cupcake in cupcakes:
            writer.writerow({"image": cupcake.image, "size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "price": cupcake.price, "gluten": cupcake.gluten, "limited": cupcake.limited, "calories": cupcake.calories, "frosting": cupcake.frosting})


# _____________ Cupcake __________________
def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["image", "size", "name", "flavor", "price", "gluten", "limited", "calories", "frosting"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)
