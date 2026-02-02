class Vehicle:

    def _init_(self, seating, fare):
        self.seating = seating
        self.fare = fare

        # the original fare
    def fare1(self):
       self.fare = 10/100 * self.fare + self.fare
       print("Total fare costs: ", self.fare)

class Bus(Vehicle):
        def _init_(self,seating,fare):
            super()._init_(seating,fare)
            self.total_fare =  self.seating *  self.fare

school_bus = Bus(50,100)
school_bus.fare1()
school_bus = Bus(school_bus.seating,school_bus.fare)
print("Total fare costs: ", school_bus.total_fare)