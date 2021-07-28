class Car:
    def __init__(self,model,colour,company , speed_limit):
        self.model = model
        self.colour = colour
        self.speed_limit = speed_limit
        self.company = company

    def start(self):
        print('started')
        
    def stop(self):
        print('stopped')
        
    def accelerate(self):
        print('accelerating')
        "accelerating functionality here"
        
    def change_gear(self):
        print('gear changed')
        "gear related functionality here"
        
audi = Car("a6","black","audi",80)
print(audi.colour)