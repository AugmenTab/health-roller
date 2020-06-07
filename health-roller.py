#! python3

import re

hitDiceRegex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')

def getHealth(hitDice, f):
    hd = hitDiceRegex.findall(hitDice.lower())
    nums = []
    for i in hd:
        if 'd' in i:
            die = i.split('d')
            if die[0] == '' or die[0] == '+' or die[0] == '-':
                die[0] = die[0] + '1'
            nums.append(f(die))
        else:
            nums.append(int(i))
    print('The monster has ' + str(sum(nums)) + ' hit points.')

def calcAverageHealth(die): # 1/2 die value rounded down for every roll
    avgHealth = (int(die[1]) / 2) * int(die[0])
    return int(avgHealth)

def calcMax(die): # Max die value for every roll.
    maxHealth = int(die[0]) * int(die[1])
    return maxHealth

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

hitDice = input("Enter the monster's hit dice.\n")
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
        'avg': calcAverageHealth,
        'max': calcMax,
        'min': calcMin,
        'pca': calcPCAverage,
        'pcr': calcPCRollHealth,
        'pcs': calcPCSuggestedHealth,
        'rol': calcPCRollHealth,
        'sug': calcSuggestedHealth
    }
    if calcMethod in calcMethods:
        getHealth(hitDice, calcMethods[calcMethod])
        break
    else:
        print('That is not a valid option.')