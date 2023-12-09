#ex1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# bengal_cat = Bengal(name = "Ben", age = 3)
# chartreux_cat = Chartreux(name = "Chart", age = 2)
# siamese_cat = Siamese(name = "Siame", age = 4)

# all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# sara_pets = Pets(animals = all_cats)

# sara_pets.walk()



#ex2

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def barks(self):
#         print(f"{self.name} barks ! WAF")

#     def run_speed(self, run_speed):
#         run_speed = self.weight / self.age * 10
#         print(f"{self.name} running speed is {self.run_speed}")

#     def fight(self, other_dog):
#         self_score = self.run_speed * self.weight
#         other_score = other_dog.speed * other_dog.weight
#         if self_score > other_score:
#             print(f"{self.name} has won {other_dog.name}")
#         else:
#             print(f"{other_dog.name} has won {self_score}") 

# if __name__ == '__main__':

# dog1 = Dog(name = "Fenix", age = 5, weight = 19) 
# dog2 = Dog(name = "Felix", age = 3, weight = 20)
# dog3 = Dog(name = "Max", age = 4, weight = 21)

# print(dog1.barks())
# print(dog2.run_speed())
# print(dog3.fight())

# class PetDog(Dog):
#     def __init__(self, name, age, weight, trained = False):
#         super().__init__(name, age, weight)
#         self.trained = trained

#     def train(self):
#         bark = self.bark()
#         self.trained = True

#     def play(self, *args):
#         for i in args:
            
#         all_dogs = [self.name, args.name]
#         dog_str = ", ".join(all_dogs)
#         print(f"{dog_str} all play together")

# dog1 = Dog(name = "Fenix", age = 5, weight = 19) 
# dog2 = Dog(name = "Felix", age = 3, weight = 20)
# dog3 = Dog(name = "Max", age = 4, weight = 21)



#ex4
# class Family:
#     def __init__(self, last_name):
#         self.members = []
#         self.last_name = last_name

#     def add_member(self, first_name, age, relationship):
#         member = {
#             'first_name': first_name,
#             'age': age,
#             'relationship': relationship
#         }
#         self.members.append(member)

#     def born(self, **kwargs):
#         child_first_name = kwargs.get('first_name', 'Unknown')
#         child_gender = kwargs.get('gender', 'Unknown')

#         self.add_member(child_first_name, 0, f"Newborn {child_gender}")
#         print(f"Congratulations! A new member, {child_first_name}, has been born to the {self.last_name} family.")

#     def is_18(self, name):
#         for member in self.members:
#             if member['first_name'] == name:
#                 return member['age'] > 18
#         return False

#     def display_family_members(self):
#         print(f"Family Members of {self.last_name}:")
#         for member in self.members:
#             print(f"Name: {member['first_name']}, Age: {member['age']}, Relationship: {member['relationship']}")


# # Creating an instance of the Family class with the last name "Johnson"
# johnson_family = Family(last_name="Johnson")

# # Adding members to the family
# johnson_family.add_member("Michael", 35, "Father")
# johnson_family.add_member("Sarah", 32, "Mother")

# # Displaying family members
# johnson_family.display_family_members()

# # Checking if a family member is over 18
# print(johnson_family.is_18("Michael"))  # True
# print(johnson_family.is_18("Sarah"))    # True (assuming parents are considered adults)

# # Adding a newborn to the family
# johnson_family.born(first_name="Alex", gender="Male")

# # Displaying family members after the newborn is added
# johnson_family.display_family_members()



# # #ex5
# class TheIncredibles(Family):
#     def incredible_presentation(self):
#         super().family_presentation

# incredible_mambers =  [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]

# incredible_fam = TheIncredibles("Incredible", data2)








