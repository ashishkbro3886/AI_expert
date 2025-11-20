import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init() #This function initializes Colorama so that ANSI escape sequences work on Windows. On other platforms (like macOS or Linux), this helps ensure compatibility.
print(f"{Fore.BLUE}😊 Welcome to sentiment spy😊{Style.RESET_ALL}")