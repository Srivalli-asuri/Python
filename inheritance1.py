class vehicle:
    def v1(self):
        return "this is first class"
class vehicle1(vehicle):
    def v2():
        return "this is second class"
class vehicle2(vehicle1):
    def v3():
        return "this is third class"
class vehicle3(vehicle2):
    def v4():
        return "this is fourth class"
obj1=vehicle3
print(obj1.v3())
