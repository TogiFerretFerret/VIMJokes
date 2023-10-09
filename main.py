from colorama import Fore, Back, Style
from tqdm import tqdm
import os
import requests
import time
quote_list = []
idex = 0
lve = requests.get("https://raw.githubusercontent.com/TogiFerretFerret/test-e/main/jokes/vimjokes.txt").text.split("\n")
for i in tqdm(range(len(lve)),desc="Downloading Quotes"):
    mcv = requests.get("https://raw.githubusercontent.com/TogiFerretFerret/test-e/main/jokes/vimjokes.txt").text.split("\n")
    quote_list.append(mcv[idex])
    idex+=1
print(Fore.GREEN + "Done!")
print(Style.RESET_ALL)
quote_list.pop(len(quote_list)-1)
for i in quote_list:
    print(Fore.CYAN + i)
    print(Style.RESET_ALL)

