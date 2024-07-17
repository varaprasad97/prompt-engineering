class Bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer = 0
        self.is_running = False

    def get_bike_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def read_odometer(self):
        return f"Odometer reading: {self.odometer} miles"

    def start_bike(self):
        if not self.is_running:
            self.is_running = True
            print("Bike started.")
        else:
            print("Bike is already running.")

    def stop_bike(self):
        if self.is_running:
            self.is_running = False
            print("Bike stopped.")
        else:
            print("Bike is already stopped.")

    def ride(self, miles):
        if self.is_running:
            self.odometer += miles
            print(f"Riding {miles} miles.")
        else:
            print("Cannot ride, bike is not running.")


# Example usage:
if __name__ == "__main__":
    my_bike = Bike("Honda", "CBR500R", 2022)
    
    print("Bike information:", my_bike.get_bike_info())
    my_bike.start_bike()
    my_bike.ride(20)
    print(my_bike.read_odometer())
    my_bike.stop_bike()
