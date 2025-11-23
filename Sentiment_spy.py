import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init() #This function initializes Colorama so that ANSI escape sequences work on Windows. On other platforms (like macOS or Linux), this helps ensure compatibility.
print(f"{Fore.BLUE}😊 Welcome to sentiment spy😊{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Enter your name:{Style.RESET_ALL}").strip() #.strip(): Removes any leading or trailing whitespace from the input.


if not user_name:
    user_name = "Mystery Agent" ## Fallback if user doesn't provide a name

conversation_history = [] #An empty list that will store each sentence along with its computed sentiment data.
# Each item stored is a tuple: (text, polarity, sentiment_type).

print(f"{Fore.CYAN} Hello! {user_name}{Style.RESET_ALL}")
print(f"Write the sentences and I will analyze them and tell your sentiment.")
print(f"{Fore.YELLOW} 'reset',{Fore.CYAN} 'history',{Fore.RED} 'exit' to quit.{Style.RESET_ALL} ")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n {Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW} No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start = 1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "????"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "????"
                else:
                    color = Fore.YELLOW
                    emoji = "????"
                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
                continue
    # sentiment analysis
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "????"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "????"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "????"
    
    # Storing and Displaying the Result

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected!"f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
    