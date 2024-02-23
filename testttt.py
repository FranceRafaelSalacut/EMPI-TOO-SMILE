import re

patern = r'(ab)*(aa|bb)'
test = [
    "aa",
    "e",
    "abababbb",
    "abababaaaa",
    "aaaaaabbbbbb",
    "bbbbbbababab"
]

for txt in test:
    if re.fullmatch(patern, txt):
        print("match!")
    else: 
        print("fuku")

