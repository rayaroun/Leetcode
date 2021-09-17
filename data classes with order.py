from dataclasses import dataclass, field

# we can also order the dataclass 

@dataclass(order = True)
class Person:

	sort_index : int = field(init=False, repr=False) # defining this for sorting, would not be initialized, added the repr argument so that when we print the object the sort index does not show
	# since we added the data class we no longer need to have the self.__init__ fucntion

	name : str
	job : str
	age : int


	def __post_init__(self):
		self.sort_index = self.age

person1 = Person('Geralt' , 'Witcher' , 30)
person2 = Person('Aroun', 'jobless', 26)
person3 = Person('Aroun', 'jobless', 26)



print(person1) # prints the contents of the initialized variables in the data class

print(person2.age) # prints the age


# after adding order person2 > person3 is a valid operation. Ofcourse we would have to define what the order is 

print(person1 > person3) # now we can compare the contents of the data classes just by using the objects




