countries = ["India", "United States", "Australia", "Ireland", "Sri Lanka", "Iceland", "Cuba", "Iran", "Poland"]
"""
 Problem => Count all the countries which are starting with "I"
            Also print all these countries with starts with "I"
            ['India', 'Ireland', 'Iceland', 'Iran']
"""
# Standard way to solve it
print(f"Using Standard way to solve it")
count = 0
countriesStartsWithI = []
for country in countries:
    if country[0] == "I":
        count = count + 1
        print(f"The country name {country} where the name starts with I.")
        countriesStartsWithI.append(country)
print("The total count of all the countries with starts with I =>", count)
print("List of all the countries with starts with I =>", countriesStartsWithI)

# Another way - Using the built-in function - startswith() -> it works with strings
print(f"\nUsing Built-In Function - StartsWith()")
count = 0
countriesStartsWithIAgain = []
for country in countries:
    if country.startswith("I"):
        count = count + 1
        print(f"The country name {country} where the name starts with I.")
        countriesStartsWithIAgain.append(country)
print("The total count of all the countries with starts with I.", count)
print("List of all the countries with starts with I =>", countriesStartsWithIAgain)
