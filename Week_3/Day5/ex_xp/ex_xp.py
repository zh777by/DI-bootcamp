#Quizz
#part_1

#What is a class?
#A Class it is an object constructor, or a "blueprint" for creating objects, but it doesn’t offer any actual content itself. It is an idea for how something should be defined.

#What is an instance?
#An instance is a copy of the class with actual values, literally an object belonging to a specific class. 

#What is encapsulation?
#Encapsulation describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

#What is abstraction?
#Abstraction is defined as a process of handling complexity by hiding unnecessary information from the user.

#What is inheritance?
#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#What is multiple inheritance?
#A class can be derived from more than one superclass.

#What is polymorphism?
#Polymorphism means different or related classes that use the same names for their functions.

#What is method resolution order or MRO?
#It is the order in which a method is searched for in a classes hierarchy 



#part_2

# import random

# class Card:
#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value

#     def __str__(self):
#         return f"{self.value} of {self.suit}"

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#         self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#         self.initialize_deck()

#     def initialize_deck(self):
#         self.cards = []
#         for suit in self.suits:
#             for value in self.values:
#                 card = Card(suit, value)
#                 self.cards.append(card)

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def deal(self):
#         if not self.cards:
#             print("No cards left in the deck.")
#             return None
#         return self.cards.pop()


# deck = Deck()
# deck.shuffle()


# for _ in range(5):
#     card = deck.deal()
#     if card:
#         print(f"Dealt: {card}")

