class Car:
    color = None

class Motorcycle:
    color = None

def change_color(car,color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

m1 = Motorcycle()
m2 = Motorcycle()
m3 = Motorcycle()

change_color(car_1,"white")
change_color(car_2, "yellow")
change_color(car_3,"green")


change_color(m1, "m_white")
change_color(m2, "m_green")
change_color(m3, "m_yellow")

print(car_1.color)
print(car_2.color)
print(car_3.color)

print(m1.color)
print(m2.color)
print(m3.color)