
# def add(*args):
#     sum_numb = sum([n for n in args])
#     return sum_numb
#
#
# print(add(5,5,8))


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=5, multiply=10)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="White")
print(my_car.make)

