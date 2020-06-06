#! python3
import re

hitDiceRegex = re.compile(r'([+/-]*[\d]*d[\d]{1,2}|[+/-]*\d+)')

def getHealth(hitDice, f):
    hd = hitDiceRegex.findall(hitDice)
    print(hd)
    print(str(f))

#TODO: Write a parser for the regular expression.

def calcAvg():
    pass # 1/2 die value rounded down for every roll.

def calcMax():
    pass # Max die value for every roll.

def calcMin():
    pass # Min die value for every roll (1).

def calcPCA():
    pass # Max die value for first HD, 1/2 die value rounded down for every other roll.

def calcPCR():
    pass # Max die value for first HD, randomly rolled for every other roll.

def calcPCS():
    pass # Max die value for first HD, (1/2)+1 die value rounded down for every other roll.

def calcRol():
    pass # Random rolls.

def calcSug():
    pass # (1/2)+1 die value rounded down for every roll.

print("Enter the monster's hit dice.")
hitDice = str(input())

calcMsg = """Enter how you would like health calculated:
    - avg for the average health.
    - max for the maximum health.
    - min for the minimum health.
    - pca for PC-styled average health.
    - pcr for PC-styled randomly rolled health.
    - pcs for PC-styled suggested health.
    - rol for randomly rolled health.
    - sug for the suggested health.
    """

while True:
    calcMethod = input(calcMsg)
    calcMethods = {
        'avg': calcAvg,
        'max': calcMax,
        'min': calcMin,
        'pca': calcPCA,
        'pcr': calcPCR,
        'pcs': calcPCS,
        'rol': calcRol,
        'sug': calcSug
    }
    if calcMethod in calcMethods:
        getHealth(hitDice, calcMethods[calcMethod])
        break
    else:
        print('That is not a valid option.')