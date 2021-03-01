class Animal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print(f"I am {self.name}")


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)


if __name__ == '__main__':
    robin = Bird("robin")
    robin.make_noise()
