#ex1

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat_1 = Cat("Lisy", 3)
# cat_2 = Cat("Dina", 5)
# cat_3 = Cat("Rita", 2)

# cats = [cat_1, cat_2, cat_3]

# def oldest_cat():
#     for cat in cats:
#         print(max(cat.age))
    
#     return oldest_cat

# print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")



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
#     def __init__(self, zoo_name):
#         self. animals = []
#         self.name = zoo_name        

#     def add_animal(self,new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)

#     def get_animals(self):
#         for animal in self.animals:
#             print(animal)

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)

#     def sort_animals(self):
#         sorted_animals = sorted(self.animals)

# #next not defined

# ramat_gan_safari = Zoo("Ramat Gan Safari")

# ramat_gan_safari.add_animal("lion")
# ramat_gan_safari.add_animal("elephant")
# ramat_gan_safari.add_animal("giraffe")
# ramat_gan_safari.add_animal("zebra")
# ramat_gan_safari.add_animal("kangaroo")

# ramat_gan_safari.get_animals()
# ramat_gan_safari.sell_animal("elephant")
# ramat_gan_safari.get_animals()

# ramat_gan_safari.sort_animals()








