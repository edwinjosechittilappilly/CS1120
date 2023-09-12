# # creating a dictionary
# country_capitals = {
#   "United States": "Washington D.C.", 
#   "Italy": "Rome", 
#   "England": "London"
# }

# # printing the dictionary
# print(country_capitals)

# print(country_capitals["United States"])  # Washington D.C.

# print(country_capitals["England"]) # London


country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples", 
  "England": "London"
}


# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)