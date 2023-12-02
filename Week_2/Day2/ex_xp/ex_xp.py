# ex_1
# my_fav_numbers = set([3, 4, 5, 6])
# my_fav_numbers.add(2)
# my_fav_numbers.add(7)
# my_fav_numbers.remove(7)

# friend_fav_numbers = set([8, 5, 3, 1])

# print(my_fav_numbers.union(friend_fav_numbers))

#ex2
#no

#ex3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0,'Apples')
# apple_count = basket.count('Apples')
# basket.clear()
# print(basket)

#ex4
#An integer is a whole number without any decimal point.
#A float is a number that has both an integer part and a fractional part, separated by a decimal point.

# count = 1
# while count <= 4.5: 
#     my_list = count + 0.5 
#     print(my_list)
#     count += 0.5

#ex5
# for numbers in range(1,21):
#     if numbers % 2 == 0:   
#         print(numbers)

#ex6
# my_name = 'Evgenii'
# while True:
#     user_name = input("Please enter your name: ")
#     print(user_name)
#     if user_name == my_name:
#         break

#ex7
# user_input = input("Please enter your favorite fruits, separated with a single space: ")
# favorite_fruits = user_input.split()
# print("Your favorite fruits:", favorite_fruits)
# user_favorite_fruit = input("Now, enter the name of any fruit: ")
# if user_favorite_fruit in user_input:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#ex8
# toppings = []
# base_price = 10
# topping_price = 2.5
# while True:
#     topping = input("Enter a pizza topping: ")
#     toppings.append(topping)
#     print(f"Adding {topping} to your pizza.")
#     if topping.lower() == 'quit':
#         break
# total_price = base_price + len(toppings) * topping_price

# Sorry I don't have more time 


#ex9
# family_size = int(input('How many people in a family? '))
# ages = []

# for i in range(family_size):
#     age = int(input(f'Enter the age of family member {i+1}: '))
#     ages.append(age)

# print('Ages of family members:', ages)

# if age < 3:
#   age_price = 0
# elif 3< age < 12:
#   age_price = 10
# else:
#   age_price = 15

# total_price = age * age_price
# print(f"Total price is: ${total_price}")


# goup_size = int(input('How many people? '))
# list_of_teenagers = []

# for i in range(goup_size):
#   age = int(input(f'Enter the age of each member {i+1}: '))
#   list_of_teenagers.append(age)


# if 16 < age < 21 in list_of_teenagers: 
#   list_of_teenagers.remove(age)
  
# print(list_of_teenagers)


#ex10

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# while "Pastrami sandwich" in sandwich_orders:
#     sandwich_orders.remove("Pastrami sandwich")
# # print(sandwich_orders)

# finished_sandwiches = []

# sandwich_orders.remove("Tuna sandwich")
# finished_sandwiches.append("Tuna sandwich")
# sandwich_orders.remove("Avocado sandwich")
# finished_sandwiches.append("Avocado sandwich")
# sandwich_orders.remove("Egg sandwich")
# finished_sandwiches.append("Egg sandwich")
# sandwich_orders.remove('Chicken sandwich')
# finished_sandwiches.append('Chicken sandwich')

# print("I made your tuna sandwich")
# print("I made your avocado sandwich")
# print("I made your egg sandwich")
# print("I made your chicken sandwich")










    











