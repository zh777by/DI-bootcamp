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
#     def __init__(self, members, last_name: str):
#         self.members = []
#         self.last_name = last_name

#     def born(self, **kwargs):
#         self.add_member(**kwargs)
#         print(f"Congratulations! Child is born into the {self.last_name} family.")

#     def is_18(self, name, member_age):
#         for member in self.members:
#             if member_age > 18:
#                 return True
#             else:
#                 return False
            
#     def family_presentation(self):
#         for member in self.members:
#             print(f"Name: {member['first_name']}, Age: {member['age']}, Relationship: {member['relationship']}")


# # #ex5
# class TheIncredibles(Family):
#     def incredible_presentation(self):
#         super().family_presentation

# incredible_mambers =  [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]

# incredible_fam = TheIncredibles("Incredible", data2)








