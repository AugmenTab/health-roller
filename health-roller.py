#! python3

import re, math

hitDiceRegex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')

def getHealth(hitDice, f):
    hd = hitDiceRegex.findall(hitDice.lower())
    dice = []
    nums = []
    for i in hd:
        if 'd' in i:
            die = i.split('d')
            if die[0] == '' or die[0] == '+' or die[0] == '-':
                die[0] = die[0] + '1'
            dice.append(list(map(int, die)))
        else:
            nums.append(int(i))
    nums.extend(f(dice))
    print('The monster has ' + str(sum(nums)) + ' hit points.')

def calcAverageHealth(dice): #1/2 die value rounded down for every roll
    return list(map(__calcAverageHealth, dice))

def __calcAverageHealth(die):
    avgHealth = math.floor((die[1] / 2) * die[0])
    return avgHealth

def calcMax(dice): #Max die value for every roll.
    return list(map(__calcMax, dice))

def __calcMax(die):
    maxHealth = die[0] * die[1]
    return maxHealth

def calcMin(dice): #Min die value for every roll.
    return list(map(__calcMin, dice))

def __calcMin(die):
    minHealth = die[0]
    return minHealth

def calcPCAverage(die): #Max die value for first HD, 1/2 die value rounded down for every other roll.
    lvlMax = False
    avgPC = math.floor((int(die[1]) / 2) * int(die[0]) + int(die[1]))
    if not lvlMax:
        lvlMax = True
    return avgPC

def calcPCRollHealth():
    pass # Max die value for first HD, randomly rolled for every other roll.

def calcPCSuggestedHealth():
    pass # Max die value for first HD, (1/2)+1 die value rounded down for every other roll.

def calcRandomHealth():
    pass # Random rolls.

def calcSuggestedHealth(dice): #(1/2)+1 die value rounded down for every roll.
    return list(map(__calcSuggestedHealth, dice))

def __calcSuggestedHealth(die):
    sugHealth = math.floor((((die[1]) / 2) + 1) * die[0])
    return sugHealth

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