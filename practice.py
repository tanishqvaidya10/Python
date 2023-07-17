print("enter your fav cars: ")
cars = []

while True:
    c = input()
    if c == "q":
        break
    elif c == "r":
        cars.pop(0)
    else:
        cars.append()
    print(cars)

    for car in cars:
        print(car)