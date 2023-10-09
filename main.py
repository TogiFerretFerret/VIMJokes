from colorama import Fore, Style
from tqdm import tqdm
import time
import requests

quote_list = []
idex = 0
lve = requests.get("https://raw.githubusercontent.com/TogiFerretFerret/test-e/main/jokes/vimjokes.txt").text.split("\n")
for i in tqdm(range(len(lve)),desc="Downloading Quotes"):
    mcv = requests.get("https://raw.githubusercontent.com/TogiFerretFerret/test-e/main/jokes/vimjokes.txt").text.split("\n")
    quote_list.append(mcv[idex])
    idex+=1
print(Fore.GREEN + "Done!")
print(Style.RESET_ALL)
# Create a function to print a string with a typewriter effect
def typewriter(string,speed=0.1):
    for char in string:
        print(Fore.CYAN + char, end='')
        time.sleep(speed)
    print()
quote_list.pop(len(quote_list)-1)
for i in quote_list:
    typewriter(i)
    print(Style.RESET_ALL)
    input("Press Enter to continue...")
