# Health Roller

## Overview

A simple Python health roller for tabletop games. It uses regular expressions to interpret provided hit dice, then return the hit points for the creature based on the supplied hit dice and whichever common calculating scheme.

For the following, assume the input is 1d10+3d8+15 (one 10-sided die, three 8-sided dice, and a flat bonus of 15).

* Average health, or the exact middle value for each die. It would return 32 (5 + (3 x 4) + 15).
* Rolled health, or pseudo-random values between 1 and the die value for each die. It would return between 19 and 49.
* Suggested health. In Dungeons & Dragons 5e, players can choose to take this instead of rolling for their hit points after each level-up. It is 1 + the middle value for each die. It would return 36 (6 + (3 x 5) + 15).
* Player character versions of each of the above. This means that the first hit die is at its maximum value.
  * PC average health would return 37 (10 + (3 x 4) + 15).
  * PC rolled health would return between 28 and 49.
  * PC suggested health would return 40 (10 + (3 x (4 + 1)) + 15).
* Maximum health, or the maximum value for each die. It would return 49 (10 + (3 x 8) + 15).
* Minimum health, or the minimum value for each die. It would return 19 (1 + (3 x 1) + 15).
