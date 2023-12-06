# ex1

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f'{self.amount} {self.currency}'

#     def __int__(self):
#         return self.amount

#     def __repr__(self):
#         return f'{self.amount} {self.currency}'

#     def __int__(self):
#         return self.amount

#     def __add__(self, other):       
#         if isinstance(other, (int, float)):
#             return Currency(self.currency, self.amount + other) 

#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             return Currency(self.currency, self.amount + other.amount)

#     def __iadd__(self, other):
#         if isinstance(other, (int, float)):
#             self.amount += other
#         elif isinstance(other, Currency):
#             if self.currency != other.currency:
#                 raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
#             self.amount += other.amount
#         else:
#             raise TypeError(f"Unsupported operand type: {type(other)}")
#         return self

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





