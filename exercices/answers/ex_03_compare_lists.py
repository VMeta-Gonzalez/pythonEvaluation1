from os import listdir, chdir
from pathlib import Path

pathHappy = Path("exercices/answers/happynumbers.txt")
pathPrime = Path("exercices/answers/primenumbers.txt")

fHappy = open(pathHappy, "r")
fPrime = open(pathPrime, "r")

tempHappy = fHappy.read().splitlines()
tempPrime = fPrime.read().splitlines()

common = []

for i in tempHappy:
    if i in tempPrime:
        common.append(i)

print("The numbers present in both lists are the following :")
for x in common:
    print(x)