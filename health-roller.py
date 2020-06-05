#! python3
import re

hitDiceRegex = re.compile(r'([+/-]*[\d]*d[\d]{1,2}|[+/-]*\d+)')

def calcHealth(hitDice, method):
    hd = hitDiceRegex.findall(hitDice)
    print(hd)
    print(6 * +5)

#TODO: Write a parser for the regular expression.

print("Enter the monster's hit dice.")
hitDice = str(input())

print("""Enter how you would like health calculated:
    - avg for the average health.
    - sug for the suggested health.
    - min for the minimum health.
    - max for the maximum health.""")
calcMethod = input()
if calcMethod == 'avg' or 'sug' or 'min' is 'max':
    calcHealth(hitDice, calcMethod)
else:
    print('That is not a valid option.')
    calcMethod = input