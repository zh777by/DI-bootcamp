#ex3
# from ex_xp_1 import Dog

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



#ex5

                






