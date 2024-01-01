class MyCar:
    def __init__(self, brand,year): # constructor
        self.brand = brand
        self.year = year
    def my_car(self):
        print(f"this is my car {self.brand} {self.year}")

    def go_speed(self, max_speed: int):
        print(f"up to speed {self.brand} {max_speed}")


syarte_tesla = MyCar("tesla",2023) #instance
syarte_tesla.my_car()
syarte_bmw = MyCar("BMW", 2024)
syarte_bmw.my_car()
syarte_tesla.go_speed(300)
syarte_bmw.go_speed(200)
# print(syarte_tesla.brand,syarte_tesla.year)
# print(syarte_bmw.brand,syarte_bmw.year)
# syarte_tesla.my_car()
# syarte_bmw.my_car()
# syarte_tesla.go_speed(100)
