class Animal:
    def __init__(self) -> None:
        self.eyes = 2

    def breath(self):
        print("breath...")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print("swim swim!!")

    def breath(self):
        super().breath()
        print("in water")


nemo = Fish()
nemo.breath()
nemo.swim()
print(nemo.eyes)
