# Napište skript, který přečte obsah souboru alice.txt a pomocí slovníku v něm spočítá četnost jednotlivých
# znaků. Tento slovník poté uloží do JSON souboru hw01_output.json.
# Při zpracování považujte velká písmena za malá a ignorujte mezery (' ') a znaky nového řádku ('\n').
# Volitelně můžete slovník na závěr seřadit podle klíčů.

import json
with open('alice.txt', encoding='utf-8') as file:
    alice = file.read()


alice = alice.lower()
alice = alice.replace(" ", "")
alice = alice.replace("\n", "")


pocet_znaku = {}

for z in alice:
    if z in pocet_znaku:
        pocet_znaku[z] += 1
    else:
        pocet_znaku[z] = 1


hw_01_output_file = {key: pocet_znaku[key] for key in sorted(pocet_znaku)}
print(hw_01_output_file)


with open("hw_01_output_file.json", mode="w", encoding="utf-8") as output_file:
    json.dump(hw_01_output_file, output_file, ensure_ascii=False, indent=4)
