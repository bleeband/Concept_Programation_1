from colorama import Fore, Back, Style

print(Fore.RED + 'Ce texte est rouge')
print(Back.GREEN + 'Ce texte a un fond vert')
print(Style.BRIGHT + 'Ce texte est lumineux')
print(Fore.BLUE + Back.YELLOW + 'Ce texte est bleu avec un fond jaune')
print()
# Reset to default
print(Style.RESET_ALL + 'Ce texte est revenu à la normale')
