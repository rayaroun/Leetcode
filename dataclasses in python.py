from dataclasses import dataclass

@dataclass
class Person:
	name : str
	job : str
	age : int


person1 = Person('Geralt' , 'Witcher' , 30)
person2 = Person('Aroun', 'jobless', 26)
person3 = Person('Aroun', 'jobless', 26)



print(person1) # prints the contents of the initialized variables in the data class

print(person2.age) # prints the age

print(person2 == person3) # now we can compare the contents of the data classes just by using the objects




