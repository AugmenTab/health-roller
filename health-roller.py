#! python3
import re

hitDiceRegex = re.compile(r'([+/-]*[\d]*d[\d]{1,2}|[+/-]*\d+)')

def getHealth(hitDice, method):
    hd = hitDiceRegex.findall(hitDice)
    print(hd)

#TODO: Write a parser for the regular expression.

print("Enter the monster's hit dice.")
hitDice = str(input())

print("""Enter how you would like health calculated:
    - avg for the average health.
    - sug for the suggested health.
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