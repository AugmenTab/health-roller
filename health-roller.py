#! python3

import math
import random
import re

hit_dice_regex = re.compile(r'([+/-]*[\d]*[d,D][\d]{1,2}|[+/-]*\d+)')


def get_health(_hit_dice, f):
    hd = hit_dice_regex.findall(_hit_dice.lower())
    dice = []
    nums = []
    for i in hd:
        if 'd' in i:
            die = i.split('d')
            if die[0] in ('', '+', '-'):
                die[0] = die[0] + '1'
            dice.append(list(map(int, die)))
        else:
            nums.append(int(i))
    nums.extend(f(dice))
    print('The monster has ' + str(sum(nums)) + ' hit points.')


def calc_average_health(dice):  # 1/2 die value rounded down for every roll
    return list(map(__calc_average_health, dice))


def __calc_average_health(die):
    avg_health = math.floor((die[1] / 2) * die[0])
    return avg_health


def calc_max(dice):  # Max die value for every roll.
    return list(map(__calc_max, dice))


def __calc_max(die):
    max_health = die[0] * die[1]
    return max_health


def calc_min(dice):  # Min die value for every roll.
    return list(map(__calc_min, dice))


def __calc_min(die):
    min_health = die[0]
    return min_health


def calc_pc_average(dice):  # Max die value for first HD, 1/2 die value rounded down for every other roll.
    return __calc_pc_rules(dice, calc_average_health)


def __calc_pc_rules(dice, f):
    avg_pc = [dice[0][1]]
    dice[0][0] -= 1
    avg_pc.append(sum(f(dice)))
    return avg_pc


def calc_pc_roll_health(dice):  # Max die value for first HD, randomly rolled for every other roll.
    return __calc_pc_rules(dice, calc_random_health)


def calc_pc_suggested_health(dice):  # Max die value for first HD, (1/2)+1 die value rounded down for every other roll.
    return __calc_pc_rules(dice, calc_suggested_health)


def calc_random_health(dice):  # Random rolls.
    return list(map(__calc_random_health, dice))


def __calc_random_health(die):
    rand = random.randint(1, die[1])
    return rand


def calc_suggested_health(dice):  # (1/2)+1 die value rounded down for every roll.
    return list(map(__calc_suggested_health, dice))


def __calc_suggested_health(die):
    suggested_health = math.floor((((die[1]) / 2) + 1) * die[0])
    return suggested_health


hit_dice = input("Enter the monster's hit dice.\n")
calc_msg = """Enter how you would like health calculated:
    - avg for the average health.
    - max for the maximum health.
    - min for the minimum health.
    - pca for PC-styled average health.
    - pcr for PC-styled randomly rolled health.
    - pcs for PC-styled suggested health.
    - rol for randomly rolled health.
    - sug for the suggested health.\n"""

while True:
    calc_method = input(calc_msg)
    calc_methods = {
        'avg': calc_average_health,
        'max': calc_max,
        'min': calc_min,
        'pca': calc_pc_average,
        'pcr': calc_pc_roll_health,
        'pcs': calc_pc_suggested_health,
        'rol': calc_random_health,
        'sug': calc_suggested_health
    }
    if calc_method in calc_methods:
        get_health(hit_dice, calc_methods[calc_method])
        break
    else:
        print('That is not a valid option.')
