def add(*args):
    return sum(args)


sum = add(2, 4, 6, 14, 87)
# print(sum)

def calculate(n, **kwargs):
    print(kwargs) # => {'add':3, 'multiply':5}
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    print(kwargs["add"]) # => 3
    n += kwargs["add"] # => 5
    n *= kwargs["multiply"] # => 5(result above) * 5

calculate(2, add=3, multiply=5)

#How is the Label class created in Tkinter (look at main.py)?
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # works as square brackets, but if there's no value it won't give an error, but just return None
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.make) # => Nissan
print(my_car.color) # => None



