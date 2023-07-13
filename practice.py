import copy

cars = ["tesla","bmw","audi"]

c = copy.deepcopy(cars)
c[0] = "ford"

print(c,cars)