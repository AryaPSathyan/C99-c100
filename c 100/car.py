class Car():
    def __init__(self,model,color,company,speed_limit):
        self.model = model
        self.color = color 
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("the car has started")

    def stop(self):
        print("the car has stopped")    

    def change_gear(self,gear_type):
        print("gear has changed to " ,gear_type)

audi = Car("A6","red","audi","80")
audi.change_gear(2)
audi.color 