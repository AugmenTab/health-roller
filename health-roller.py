#! python3
import re

hitDiceRegex = re.compile(r'([+/-]*[\d]*d[\d]{1,2}|[+/-]*\d+)')

def getHealth(hitDice, method):
    hd = hitDiceRegex.findall(hitDice)
    print(hd)

#TODO: Write a parser for the regular expression.

def calcAvg():
    pass # 1/2 die value rounded down for every roll.

def calcMax():
    pass # Max die value for every roll.

def calcMin():
    pass # Min die value for every roll (1).

def rollHealth():
    pass # Random rolls.

def calcSug():
    pass # (1/2)+1 die value rounded down for every roll.

print("Enter the monster's hit dice.")
hitDice = str(input())

print("""Enter how you would like health calculated:
    - avg for the average health.
    - max for the maximum health.
    - min for the minimum health.
    - rol for randomly rolled health.
    - sug for the suggested health.""")
calcMethod = input()
if calcMethod == 'avg' or 'max' or 'min' or 'rol' or 'sug':
    getHealth(hitDice, calcMethod)
else:
    print('That is not a valid option.')
    calcMethod = input