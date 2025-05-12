
class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            print("Age cannot be negative!")
        else:
            self._age = new_age

    
    def display_name(self):
        print("Your name is:",self.name)
        print(f"You age is {self.age} years old.")
    

p1 = Person("Mary", 36)
p1.age = 49
print(f"Updated age for {p1.name} to {p1.age} years old.")
p1.display_name()

p2 = Person("Jane", 17)
p2.display_name()

p3 = Person("Olivia", 28)
p3.display_name()


