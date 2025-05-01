class Vehicle:
    licenseNumber = ""
    serialCode = ""
    
    def turnonairconditioner(self):
        print("Turn On:Air")
class Car(Vehicle):
    def sayhello(self):
        print("Hello world")
        
class PickUp(Vehicle):
    pass
        
class Van(Vehicle):
    pass
        
pickup1 = PickUp()
pickup1.turnonairconditioner()

car1 = Car()
car1.turnonairconditioner()
car1.sayhello()

van1 = PickUp()
van1.turnonairconditioner()