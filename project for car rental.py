class Car:
    def __init__(self, cname, cmodel, cnum, ccolor, crent_per_day):
        self.car_name = cname
        self.car_model = cmodel
        self.car_num = cnum
        self.car_color = ccolor
        self.car_rent = crent_per_day
        self.available = True

    def display(self):
        print("Car Name:", self.car_name)
        print("Car Model:", self.car_model)
        print("Car Number:", self.car_num)
        print("Car Color:", self.car_color)
        print("Car Rent Per Day:", self.car_rent)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Rented")


class Customer:
    def __init__(self, cid, cname, cphone):
        self.customer_id = cid
        self.customer_name = cname
        self.customer_phone = cphone


class Rental:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_car(self):
        print("\nAvailable Cars")
        for car in self.cars:
            car.display()
            print("----------------------")

    def rent_car(self, car_num):
        for car in self.cars:
            if car.car_num == car_num:
                if car.available:
                    car.available = False
                    print(car.car_name, "rented successfully.")
                else:
                    print("Car is already rented.")
                return
        print("Car not found.")

    def return_car(self, car_num):
        for car in self.cars:
            if car.car_num == car_num:
                if not car.available:
                    car.available = True
                    print(car.car_name, "returned successfully.")
                else:
                    print("Car is already available.")
                return
        print("Car not found.")


# Create Rental object
rental = Rental()

# Add Cars
rental.add_car(Car("BMW", "X5", 101, "Black", 5000))
rental.add_car(Car("AUDI", "A6", 102, "Light Blue", 4500))
rental.add_car(Car("TOYOTA", "INNOVA", 103, "Silver", 3000))


while True:
    print("\n======= CAR RENTAL SYSTEM =======")
    print("1. Show Cars")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rental.show_car()

    elif choice == 2:
        car_num = int(input("Enter Car Number to Rent: "))
        rental.rent_car(car_num)

    elif choice == 3:
        car_num = int(input("Enter Car Number to Return: "))
        rental.return_car(car_num)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
