class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

#  someone = Person()
hunter = Person('Elmer Fudd')
print(hunter.name)

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")

    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

person = Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")
print(person.name)
print(doctor.name)
print(lawyer.name)

give_me_a_yugo.need_a_push()

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)

car = Car()
car.exclaim()
Car.exclaim(car)
