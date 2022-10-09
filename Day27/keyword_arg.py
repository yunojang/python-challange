def calc(n=1, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiple"]
    return n


print(calc(2, add=5, multiple=10))


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(model="k5")
print(my_car.model)
print(my_car.make)
