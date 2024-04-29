
class User:

    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def say_first_name(self):
        print(self.name)

    def say_last_name(self):
        print(self.surname)

    def say_full_name(self):
        print(f"{self.name} {self.surname}")