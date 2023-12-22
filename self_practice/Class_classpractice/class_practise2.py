class MyCar:
    def __init__(self, brand,year):
        self.brand = brand
        self.year = year
    def __init__(self, brand,year):
        self.brand = brand
        self.year = year

    # year = 2023
    # brand = "Tesla"

    def my_drive(self):
        print("Tesla - 2023 this is my driving")
    def my_drive2(self):
        print("BMW - 2024 this is my driving")
    def go_speed(self, max_speed: int):
        print("up to speed", max_speed)


syarte_tesla = MyCar("tesla",2023)
syarte_bmw = MyCar("BMW", 2024)
print(syarte_tesla.brand,syarte_tesla.year)
print(syarte_bmw.brand,syarte_bmw.year)
# print(type(syarte))
# print(syarte.year)
# print(syarte.brand)
syarte_tesla.my_drive()
syarte_bmw.my_drive2()
syarte_tesla.go_speed(100)
