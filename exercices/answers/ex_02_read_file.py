from os import listdir, chdir
from pathlib import Path

p = Path("exercices/answers/nameslist.txt")
count = []

f = open(p, "r")

temp = f.read().splitlines()

for x in temp:
    if x not in count :
        count.append(x)
    
print(f'There is {len(count)} different names in the file "{p}" which are the following :\n {count}')