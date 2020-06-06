#! python3
import re

hitDiceRegex = re.compile(r'([+/-]*[\d]*d[\d]{1,2}|[+/-]*\d+)')

def getHealth(hitDice, f):
    hd = hitDiceRegex.findall(hitDice)
    print(hd)
    print(str(f))

#TODO: Write a parser for the regular expression.

def calcAverageHealth():
    pass # 1/2 die value rounded down for every roll.

def calcMax():
    pass # Max die value for every roll.

def calcMin():
    pass # Min die value for every roll (1).

def calcPCAverage():
    pass # Max die value for first HD, 1/2 die value rounded down for every other roll.

def calcPCRollHealth():
    pass # Max die value for first HD, randomly rolled for every other roll.

def calcPCSuggestedHealth():
    pass # Max die value for first HD, (1/2)+1 die value rounded down for every other roll.

def calcRandomHealth():
    pass # Random rolls.

def calcSuggestedHealth():
    pass # (1/2)+1 die value rounded down for every roll.

hitDice = input("Enter the monster's hit dice.")

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