class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        trip_cost = (distance / self.efficiency) * food_price
        return trip_cost
        
    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(self, max_speed, efficiency, load_weight, bed_area):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        trip_cost = Siege.get_trip_cost(distance, food_price) + (self.load_weight * 0.01)
        return trip_cost

    def get_cargo_volume(self):
        self.load
        self.cargo_volume = self.bed_area * 2
        return self.cargo_volume


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume
        

    def get_cargo_volume(self):
        return  self.cargo_volume
       
        
