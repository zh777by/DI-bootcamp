#ex1

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat_1 = Cat("Lisy", 3)
# cat_2 = Cat("Dina", 5)
# cat_3 = Cat("Rita", 2)

# cats = [cat_1, cat_2, cat_3]

# oldest_cat = cats[0]

# for cat in cats[1:]:
#     if cat.age > oldest_cat.age:
#         oldest_cat = cat

# print(f"The oldest cat is {oldest_cat.name} with age {oldest_cat.age} years.")



#ex2

# class Dog:
#     def __init__(self, name, height):
#         self.name  = name
#         self.height = height
    
#     def bark(self):
#         print(f"{self.name} barks WAF")

#     def jump(self):
#         distance = self.height * 2
#         print(f'{self.name} jumps {distance} sm!')

# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print("davids dog is bigger then sarahs dog")
# else:
#     print("sarahs dog is bigger then davids dog")



#ex3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway = ["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"]

# stairway_lyrics = Song(lyrics = stairway)

# stairway_lyrics.sing_me_a_song()


#ex4

# class Zoo:
#     def __init__(self, zoo_name) -> None:
#         self.zoo_name = zoo_name
#         self.animals = []

#     def add_animal(self, *new_animal):
#         for animal in new_animal:
#             if animal in self.animals:
#                 print('Animal already in the list')
#             else:
#                 self.animals.append(animal)

#     def get_animals(self):
#         print(self.animals)

#     def sort_animals(self):
#         sorted_animals = sorted(self.animals)
#         groups = {}   
#         for animal in sorted_animals:
#             first_letter = animal[0]
#             if first_letter not in groups:
#                 groups.update({first_letter:[animal]})
#             else:
#                  groups[first_letter].append(animal)

#         return groups
                
#     def get_groups(self):
#         groups_dict = self.sort_animals()
#         new_dict = {}
#         for i, group in enumerate(groups_dict):
#             new_dict.update({i+1 : groups_dict[group]})
#         return new_dict
            

# safari_rg = Zoo('Safari Ramat Gan')
# safari_rg.add_animal('Giraffe', 'Monkey', 'Lion', 'Arara', 'Bear', 'Baboon', 'Ape')
# safari_rg.get_animals()
# print(safari_rg.sort_animals())
# print(safari_rg.get_groups())




        










