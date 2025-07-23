class car:
    pass
print(car)
class car:
    def about(self):
        return "this is a car"

rs=car()
print(rs.about())

class name:
    def funname():
        return "hello"
obj=name
print(obj.funname())
class laptop:
    def __init__(self,brand,ram,storage,cpu):
        self.name=brand
        self.ram=ram
        self.storage=storage
        self.processor=cpu

l1=laptop('hp','16gb',512,'i5')
print(l1.name)

class mobile:
    def __init__(self,display,ram,storage,battery,processor):
        self.display=display
        self.ram=ram
        self.storage=storage
        self.battery=battery
        self.proccessor=processor
    def update_battery(self,newbattery):
        self.battery=newbattery


obj=mobile('36mm','8gb','256gb','xHZ','vv')
print(obj.proccessor)
obj1=mobile("15mm",'8gb','64gb','yhz','aa')
print(obj1.storage)
obj2=mobile("10mm",'4gb','32gb','yhz','aa')
print(obj2.display)
mobile.update_battery('4000')
print(obj2.battery)
class Device:
    def __init__(self, ram, storage, battery, processor):
        self.ram = ram
        self.storage = storage
        self.battery = battery
        self.processor = processor

    def display_info(self):
        print("Device Specifications:")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print(f"Battery: {self.battery}")
        print(f"Processor: {self.processor}")

# Creating an object of the class
my_device = Device("8GB", "256GB SSD", "4500mAh", "Intel i5")
# Displaying the information
print(my_device.display_info())
