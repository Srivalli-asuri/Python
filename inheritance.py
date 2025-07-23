# Today's Task
# Create a parent class name Vehicle and create 3 child classes to inherit the properties of parent class.
class vehicle:
    def func(self):
        return "The vehicle is moving"
class car(vehicle):
    def hi(self):
        return "It is used for travelling"
class bike(car):
    def hello(self):
        return "Its a bike"
class bicycle(bike):
    def hello2(self):
        return "Its a bicycle"

obj1=bicycle()
print(obj1.hi())
print(obj1.hello())
print(obj1.hello2())
