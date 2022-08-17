import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"text will be in blue and background in yellow"+
Fore.YELLOW+Back.BLUE+"text will be in yellow and back will be in blue")
print(Fore.CYAN+"Hi there from colorama")
print(Back.GREEN+"Go Greeen")