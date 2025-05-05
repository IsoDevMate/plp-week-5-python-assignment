class Vehicle:
    """Base class for all types of vehicles"""

    def __init__(self, name, max_speed, color):
        self.name = name
        self.max_speed = max_speed
        self.color = color
        self.current_speed = 0

    def move(self):
        """Base move method - will be overridden by child classes"""
        print(f"{self.name} is moving.")

    def stop(self):
        """Stop the vehicle"""
        self.current_speed = 0
        print(f"{self.name} has stopped.")

    def describe(self):
        """Print vehicle description"""
        print(f"This is a {self.color} {self.__class__.__name__} named '{self.name}' with a maximum speed of {self.max_speed} km/h.")


class Car(Vehicle):
    """Car class for road vehicles"""

    def __init__(self, name, max_speed, color, fuel_type):
        super().__init__(name, max_speed, color)
        self.fuel_type = fuel_type
        self.wheels = 4

    def move(self):
        """Override the move method (polymorphism)"""
        self.current_speed = min(self.max_speed, 60)
        print(f"🚗 {self.name} is driving on the road at {self.current_speed} km/h.")

    def honk(self):
        """Car-specific method"""
        print(f"🔊 {self.name} honks: BEEP BEEP!")


class Boat(Vehicle):
    """Boat class for water vehicles"""

    def __init__(self, name, max_speed, color, boat_type):
        super().__init__(name, max_speed, color)
        self.boat_type = boat_type

    def move(self):
        """Override the move method (polymorphism)"""
        self.current_speed = min(self.max_speed, 30)
        print(f"🚢 {self.name} is sailing across the water at {self.current_speed} km/h.")

    def anchor(self):
        """Boat-specific method"""
        print(f"⚓ {self.name} drops anchor and stabilizes.")


class Plane(Vehicle):
    """Plane class for air vehicles"""

    def __init__(self, name, max_speed, color, airline):
        super().__init__(name, max_speed, color)
        self.airline = airline
        self.altitude = 0

    def move(self):
        """Override the move method (polymorphism)"""
        self.current_speed = self.max_speed
        self.altitude = 10000
        print(f"✈️ {self.name} is flying through the sky at {self.current_speed} km/h at altitude {self.altitude} meters.")

    def land(self):
        """Plane-specific method"""
        print(f"🛬 {self.name} is landing at the airport.")
        self.altitude = 0
        self.stop()


class Bicycle(Vehicle):
    """Bicycle class for human-powered vehicles"""

    def __init__(self, name, max_speed, color, type_of_bike):
        super().__init__(name, max_speed, color)
        self.type = type_of_bike
        self.wheels = 2

    def move(self):
        """Override the move method (polymorphism)"""
        self.current_speed = min(self.max_speed, 25)
        print(f"🚲 {self.name} is being pedaled along the path at {self.current_speed} km/h.")

    def ring_bell(self):
        """Bicycle-specific method"""
        print(f"🔔 {self.name}'s bell rings: RING RING!")


# Demo of vehicle polymorphism
def main():
    # Create instances of different vehicles
    sedan = Car("Family Sedan", 180, "blue", "gasoline")
    yacht = Boat("Luxury Yacht", 70, "white", "motorboat")
    jet = Plane("Commercial Jet", 900, "silver", "Delta Airlines")
    mountain_bike = Bicycle("Trail Explorer", 50, "green", "mountain bike")

    # Store all vehicles in a list
    vehicles = [sedan, yacht, jet, mountain_bike]

    print("===== VEHICLE DESCRIPTIONS =====")
    for vehicle in vehicles:
        vehicle.describe()

    print("\n===== VEHICLE MOVEMENT (POLYMORPHISM DEMO) =====")
    for vehicle in vehicles:
        vehicle.move()  # Each vehicle moves differently (polymorphism)

    print("\n===== SPECIAL VEHICLE ACTIONS =====")
    sedan.honk()
    yacht.anchor()
    jet.land()
    mountain_bike.ring_bell()

    print("\n===== STOPPING ALL VEHICLES =====")
    for vehicle in vehicles:
        vehicle.stop()  # All vehicles use the same stop method (inheritance)

if __name__ == "__main__":
    main()
