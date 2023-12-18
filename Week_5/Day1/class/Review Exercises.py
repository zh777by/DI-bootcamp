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


# Conditions
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


#Loops
#8. Write a loop to print every number between 10 and 20.

# for number in range(10, 21):
#     print(number)


#9. Write a loop to print every odd number between 1 and 20.

# for number in range(21):
#     if number % 2 != 0:
#         print(number)


#10. Write code with a list of five names. Print the names one by one using a loop.

# names = ["Anna", "Tim", "Mark", "Olga", "Boris"]

# for name in names:
#     print(name)


#11. Write a loop that takes numbers from the user until it receives the number 0 and prints the sum of the numbers received.

# sum_of_numbers = 0

# while True:
#     user_input = int(input("Enter a number: "))
#     if user_input == 0:
#         break  
#     sum_of_numbers = sum_of_numbers = user_input # sum_of_numbers += user_input

# print("Sum of the numbers:", sum_of_numbers)


#12. Write a loop that takes words from the user until it receives the word 'done' and prints the longest word received.

# words = []

# while True:
#     word = input("Enter a word (type 'done' to finish): ")

#     if word == 'done':
#         break
#     words.append(word)

# if words:
#     longest_word = max(words, key=len)
#     print("The longest word is:", longest_word)
# else:
#     print("No words were entered.")


#Functions
#13. Write a function that takes a string as input and prints its length:

# def string_length(input_string):
#     length = len(input_string)
#     print(f"The length of string is: {length}")

# user_input = input("Enter a string: ")
# string_length(user_input)


#14. Define a function that takes three numbers and prints their average.

# def average(num1: float, num2: float, num3: float):
#     total = num1 + num2 + num3
#     average = total / 3
#     print("The average is:", average)

# num1 = 10
# num2 = 10
# num3 = 10

# average(num1, num2, num3)


#15. Define a function that takes two arguments, a string and a number and checks
# if the string has more characters than the number. 

# def string_length(input_string, number):
#     return len(input_string) > number

# result = string_length('string', 3)
# print(result)


#16. Write a function that copies a string a certain number of times, based on the
# input. Set the default amount of copies to be 1.

# def copy_string(input_string, num_copies=1):
#     return input_string * num_copies

# original_string = "Hello, class!"
# result = copy_string(original_string)  
# print(result)

# result_3_copies = copy_string(original_string, 3)  
# print(result_3_copies)

