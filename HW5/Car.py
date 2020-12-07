class Car:
    def __init__(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed
    def set_year_model(self):
        self.year_model
    def set_make(self):
        self.make
    def set_speed(self):
        self.speed
    def get_year_model(self):
        return self.year_model
    def get_speed(self):
        return self.speed
    def get_make(self):
        return self.make
    def accelerate(self):
         self.speed =(self.speed)+5
    def brake(self):
         self.speed =(self.speed)-5
    def displayCar(self):
        print(" Year: ", self.year_model,"model: ", self.make, "s pit:",  self.speed)
if __name__=="__main__":
    C= Car(1991,"cào cào",5)
    C.accelerate()
    C.accelerate()
    C.displayCar()
    C.brake()
    C.displayCar()