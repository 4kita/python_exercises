class Car():
        def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage

        def drive(self, miles):
            self.mileage += miles


his_car = Car("blue", 20000)
her_car = Car("red", 30000)

print(f"The {his_car.color} car has {his_car.mileage} miles.")
print(f"The {her_car.color} car has {her_car.mileage} miles.")

his_car.drive(500)

print(f"The {his_car.color} car has {his_car.mileage} miles.")