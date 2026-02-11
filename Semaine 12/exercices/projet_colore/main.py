from colorama import Fore, Style
import emoji
import pyfiglet

print(Fore.BLUE + emoji.emojize("Bonjour :smile:", language='alias') + Style.RESET_ALL)
print(pyfiglet.figlet_format("Python"))
