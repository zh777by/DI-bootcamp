#1
# def display_message():
#     print("I am learning Python in this course.")

# display_message()

#2
# def favorite_book(title):
#     print(f"One of my favorite books is {title}: ")

# favorite_book("Alice in Wonderland")

#3
# def describe_city(name, country):
#     if name == "Tel-Aviv":
#         print(f"{name} is in Israel")
#     else:
#         print(f"{name} is not in Israel")

# describe_city("Tel-Aviv", ',')
# describe_city("Moscow", ',')

#4
# import random

# def compare_number(user_number):
#     random_number = random.randint(1,100)

#     if user_number == random_number:
#         print("Success, numbers are the same! ")
#     else:
#         print("Fail, numbers are not the same! ")
#     print("Random number is: ", random_number)

# user_input = int(input("Enter the number: "))
# compare_number(user_input)
# print("User number is: ", user_input)


#5
# def make_shirt(size="large", text="I love Python"):
#     if size == "large":
#         print(f"The size of the shirt is {size} and the text is {text}")
#     elif size == "medium":
#         print(f"The size of the shirt is {size} and the text is {text}")
#     else: 
#         size == "any"
#         print(f"The size of the shirt is {size} and the text is 'No size shift'")

# make_shirt(size="any", text="No size shift")


#6
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magician_names): 
#     print(f"Magican names: {magician_names}")

# # show_magicians(magician_names)

# def add_make_great(magician_names):
#     for n in range(len(magician_names)):
#         magician_names[n] = "The Great " + magician_names[n]

# add_make_great(magician_names)
# show_magicians(magician_names)


#7
# import random

# def get_random_temp(season):
#     if season == "winter":
#         return random.randint(-30, 5)
#     elif season == "spring":
#         return random.randint(-5, 15)
#     elif season == "summer":
#         return random.randint(5, 40)
#     elif season == "fall":
#         return random.randint(-10, 16)
#     else:
#         return random.randint(-30, 40)

# winter = get_random_temp("winter")
# spring = get_random_temp("spring")
# summer = get_random_temp("summer")
# fall = get_random_temp("fall")

# print(winter, spring, summer, fall)
    
# # random_temp = get_random_temp(season)
# # print(random_temp)

# user_input = input("enter a season: ")

# def main():
#     random_temp = get_random_temp(user_input)
#     print(f"The temperature right now is {random_temp} degrees Celsius")
#     if random_temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= random_temp < 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 16 <= random_temp < 23:
#         print("Weather is ok")
#     elif 24 < random_temp < 32:
#         print("Weather is good")
#     elif 32 <= random_temp < 40:
#         print("Heating like in hell")
# main()

#Sorry, I don't have more time











