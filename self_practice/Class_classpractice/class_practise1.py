class MyCar:
    year = 2023
    brand = "Tesla"

    def my_drive(self):
        print("this is my driving")
    def go_speed(self, max_speed: int):
        print("up to speed", max_speed)


syarte = MyCar()
print(type(syarte))
print(syarte.year)
print(syarte.brand)
syarte.my_drive()
syarte.go_speed()
