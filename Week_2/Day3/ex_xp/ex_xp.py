#ex1

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# my_dict = dict(zip(keys, values))

# print(my_dict)


#ex2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# for person, age in family.items():
#     if age < 3:
#         print(f"{person}'s ticket is free")
#     elif 3< age < 12:
#         print(f"{person}'s ticket is $10")
#     else:
#         print(f"{person}'s ticket is $15")

# total_cost = 0
# for person, age in family.items():
#     if age < 3:
#         price = 0
#     elif 3< age < 12:
#         price = 10
#     else:
#         price = 15
#     total_cost += price

# print(f"total cost for family: ${total_cost}")


#ex3
# brand = {"name": "Zara", 
# "creation_date": 1975, 
# "creator_name": "Amancio Ortega Gaona", 
# "type_of_clothes": ["men", "women", "children", "home"], 
# "international_competitors": ["Gap", "H&M", "Benetton"], 
# "number_stores": 7000, 
# "major_color":{ 
#     "France": "blue", 
#     "Spain": "red", 
#     "US": ["pink", "green"]}
# }
# print(brand)

# brand ["number_stores"] = 2

# iternational_competitors = ["Gap", "H&M", "Benetton"]
# print(f"Zara's clients are {iternational_competitors} clients")

# brand["country_creation"] = "Spain"
# print(brand)

# if brand["international_competitors"]:
#     brand["international_competitors"] = ["Gap", "H&M", "Benetton", "Desigual"]
# print(brand)

# del brand["creation_date"]
# print(brand)

# last_international_competitor = brand["international_competitors"][-1]
# print(last_international_competitor)

# us_colors = brand["major_color"]["US"]
# print("US colors:", us_colors)

# key_value_pairs = len(brand)
# print("number of pairs:", key_value_pairs)

# print('keys() : ', brand.keys())

# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000,
# }
# print(more_on_zara)

# brand.update(more_on_zara)
# print(brand)

# number_of_stores = brand["number_stores"]
# print("number of stores:", number_of_stores)
#the key is already present in "brand", the corresponding value in "brand" for that key is updated to the value from "more_on_zara".


#ex4

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# disney_users_A = {}
# for index, name in enumerate(users):
#     disney_users_A[name] = index
# print(disney_users_A)

# disney_users_B = {}
# for index, name in enumerate(users):
#     disney_users_B[index] = name
# print(disney_users_B)



        

    




        










