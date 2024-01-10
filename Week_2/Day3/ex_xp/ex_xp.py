# # ex1

# class Currency:
#     def __init__(self, label, amount):
#         self.label = label
#         self.amount = amount

#     def __str__(self):
#         return f'{self.amount} {self.label}'

#     def __int__(self):
#         return int(self.amount)

#     def __repr__(self):
#         return f'{self.amount} {self.label}'

#     def __add__(self, other):       
#         if type(other) == int:
#             return self.amount + other
        
#         elif self.label == other.label: 
#             self.amount += other.amount
#             return self.amount + other.amount
        
#         else:
#             raise TypeError ('different label')
    

#     def __iadd__(self, other):
#         if type(other) == int:
#             return self.amount + other      


# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))   
# print(int(c1))    
# print(repr(c1)) 
# print(c1 + 5)    
# print(c1 + c2)   
# print(c1)      
# c1 += 5
# print(c1)   
# c1 += c2
# print(c1)       


#ex3

# import string
# import random

# length = 5
# characters = string.ascii_letters 
# random_string = ''.join(random.choice(characters) for i in range(length))

# print(random_string)



#ex4

# from datetime import datetime

# def display_current_date():
#     current_date = datetime.now()
#     formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
#     print("current date and time:", formatted_date)

# display_current_date()


#ex5

# from datetime import datetime, timedelta

# def time_until_january_1():
#     current_datetime = datetime.now()
#     target_date = datetime(current_datetime.year)
#     time_difference = target_date - current_datetime


#ex6

# from datetime import datetime

# def minutes_lived(birthdate):
#     birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d')
#     time_lived = datetime.now() - birthdate_obj
#     minutes_lived = time_lived.total_seconds() / 60   
#     return f"You lived {int(minutes_lived):,} minutes."

# birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
# print(minutes_lived(birthdate_input))


#ex7

# from faker import Faker

# users = []
# def generate_fake_user():
#     fake = Faker()
#     user = {
#         'name': fake.name(),
#         'address': fake.address(),
#         'language_code': fake.language_code(),
#     }
#     users.append(user)


class MyClass:
  __counter = 0

  @classmethod
  def add(cls,a): 
    return cls.__counter + a

my_class_add = MyClass.add(3)
print(my_class_add)
# >> 3

new_class = MyClass()
new_class.__counter = 1

print(new_class.add(3))
# >> 3


