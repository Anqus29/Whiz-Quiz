from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# Print colored text
print(Fore.RED + "Red Text")
print("Regular Text")
print(Fore.GREEN + "Green Text")
print(Back.YELLOW + "Yellow Background")
print(Style.BRIGHT + "Bright Text" + Style.RESET_ALL)
print("Regular Text")
