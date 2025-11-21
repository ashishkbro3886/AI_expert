import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches" : ["Bali","Maldives","Phuket"],
    "mountains": ["Swiss Alps","Rocky mountains","Himalayas"],
    "cities": ["Tokyo","Paris","New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Beacuse of all their hot spots!"
]

# Normalizing User Input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower()) # Uses a regular expression to replace any occurrence of one or more whitespace characters (\s+) with a single space.

# Travel Recommendations
def recommend():
    print(f"{Fore.CYAN} TravelBot: Beaches, Mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot : How about {suggestion}")
        print(f"{Fore.CYAN}TravelBot: Do you like it? (Yes/No)")
        answer = input(Fore.YELLOW + "You :").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(f"{Fore.RED}TravelBot: Let's try another.")
            recommend() #Recursive call if the user rejects the suggestion
        else:
            print(f"{Fore.RED}TravelBot: I'll suggest again.")
            recommend() # Recursive call on unrecognized answer
    else:
        print(f"{Fore.RED}TravelBot: Sorry, I don't have that type of destinations.")
    
    show_help()

# Packing Tips
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")


# Tell a Random Joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Show Help Menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "-Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "-Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main Chat Loop Function
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(f"{Fore.GREEN}Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
    
# Running the Chatbot

if __name__ == "__main__":
    chat()