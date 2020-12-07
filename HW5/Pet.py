class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    def set_name(self, owner, name):
        self.name
    def set_animal_type(self,animal_type):
        self.animal_type
    def set_age(self):
        self.age
    def get_name(self):
        return self.name
    def get_animal_type(self):
        return self.get_animal_type
    def get_age(self):
        return self.age
    def display_pet(self):
        print(self.name, self.animal_type, self.age)
if __name__=="__main__":
    P = Pet("buddy","friend",99)
    P.display_pet()
