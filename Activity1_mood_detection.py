# Greet the user 
print("Hello, I am AI bot. What is your name?")

# Asking the name of user 
name = input("Name: ")

# Responding to the user 
print(f"Welcome to the platform, nice to meet you {name}")

# asking the question 
print(f"How is your mood today {name} (good/bad)?")
mood = input().lower()

# Compairing the input by conditional outputs
if mood == "good":
    print(f"{name}'s mood is good.")
elif mood == "bad":
    print(f"{name}'s mood is bad.")
else:
    print(f"No worries {name}, sometimes it is hard to express your mood with words.")
