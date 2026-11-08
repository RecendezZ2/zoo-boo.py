# Zanetta Recendez, IS31
# Zoo Boo admission prices and costume rules

# Store information about one guest in a dictionary.
# The name is a string, and the age is an integer.
# The member and costume values are Booleans: True or False
person = {
    "name": "Zz",
    "age": 38,
    "member": True,
    "costume": True
}

# Welcome the guest and display the Zoo Boo event dates and times.
# Access the name key to include the guest's name in the message.
print("Welcome to Zoo Boo at Fresno Chaffee Zoo!")
print("Event dates: October 22, 23, and 24, 2026")
print("Event time: 5:00 PM to 8:00 PM")
print(f"Guest name: {person['name']}")

# Checks for children under 2 first because their admission is free,
# whethar or not they are zoo members.
if person["age"] < 2:
    print("Admission: Free for children under 2.")

# Check both age and membership using the
# Members age 12 or older pay the member adult price.
elif person["age"] >= 12 and person["member"] == True:
    print("Admission: $18.00 for a member adult.")

# Children under 2 were already handled by the first condition.
# This condition covers member children ages 2 through 11.
elif person["age"] < 12 and person["member"] == True:
    print("Admission: $16.00 for a member child.")

# Guests age 12 or older who are not members pay
# the non-member adult price.
elif person["age"] >= 12 and person["member"] == False:
    print("Admission: $22.00 for a non-member adult.")

# The remaining category is non-member children ages 2 threw 11
# Print the price directly without storing or calculating it
else:
    print("Admission: $20.00 for a non-member child.")

# Check for a costume separately from the ticket pricing conditions
# Display the costume rules only when costume is True
if person["costume"] == True:
    print("\nZoo Boo Costume Rules:")
    print("Wear a family-friendly costume.")
    print("No weapons are allowed.")
    print("No extremely scary or gory costumes are allowed.")
    print("No balloons are allowed.")
    print("Inflatable costumes are allowed, except at the")
    print("giraffe feeding station at Twiga Terrace.")
    print("The Zoo's regular dress code also applies.")