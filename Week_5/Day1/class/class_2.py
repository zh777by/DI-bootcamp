#1. Write code that gets three words from a user and inputs them into a sentence using F-Strings.

# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")
# word3 = input("Enter the third word: ")

# print(f"The quick {word1} jumps over the lazy {word2} and {word3}")


#2. Write a list that contains 2 strings. Print the second string in uppercase and then the first string backwards.

# strings = ["hello", "class"]

# for string in strings:
#     if string == strings[1]:
#         print(string.upper())
#     else:
#         print(string[::-1])


#3. Write code for a list that contains four names and prints every other name.

# names = ["Anna", "Tim", "Mark", "Olga"]

# print(names)

# for i in range(0,4):
#     print(names[i])


#4. Write code for a list of numbers. Ask a user for a new number and insert it into the list,second from the end.

# numbers = [1, 2, 3, 4, 5]
# print("First list:", numbers)

# new_number = int(input("Enter a new number: "))
# numbers.insert(-1, new_number)

# print("Second list:", numbers)


#5 Create a dictionary containing the following information about you: your name, 
# your age, your gender, your favorite food. Be sure to use appropriate keys.

# my_dict = {
#     "name": "Evgenii",
#     "age": 40,
#     "gender": "male",
#     "favorite_food": "sushi"
# }
# print(my_dict)


#6. A user is allowed to drive home if their blood alcohol is less than 0.5 %. 
#Ask a user for their blood alcohol level and if they're not sober, tell them to take a cab.

# blood_alcohol_level = int(input('write your blood alcohol level: '))

# if blood_alcohol_level < 0.5:
#     print("You are sober. You can drive home.")
# else:
#     print("Your blood alcohol level is too high. Please take a cab.")


#7. If a user is male and over 65 or female and over 60, they may retire. Get a
# gender and age from the user and let them know if it's time to retire.

# gender = input("Enter your gender: ")
# age = int(input("Enter your age: "))

# if (gender == "male" and age > 65) or (gender == "female" and age > 60):
#     print("It is time to retire.")
# else:
#     print("It's not yet time to retire.")