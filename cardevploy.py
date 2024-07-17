class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.engine_status = 'off'

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        return f"Odometer reading: {self.odometer_reading} miles"

    def start_car(self):
        if self.engine_status == 'off':
            self.engine_status = 'on'
            print("Engine started.")
        else:
            print("Engine is already on.")

    def stop_car(self):
        if self.engine_status == 'on':
            self.engine_status = 'off'
            print("Engine stopped.")
        else:
            print("Engine is already off.")

    def drive(self, miles):
        if self.engine_status == 'on':
            self.odometer_reading += miles
            print(f"Driving {miles} miles.")
        else:
            print("Cannot drive, engine is off.")
if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2023)
    
    print("Car information:", my_car.get_car_info())
    my_car.start_car()
    my_car.drive(50)
    print(my_car.read_odometer())
    my_car.stop_car()
