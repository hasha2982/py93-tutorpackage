class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self, personName):
        print("{0}: Hello, {1}!".format(self.name, personName))

    def whoami(self):
        print("{0}: Hi everyone, I am {0} and my age is {1}".format(self.name, self.age))