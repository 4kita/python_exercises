from random import random


a1wins=0
a2wins=0
a3wins=0
avictories = 0

for _ in range (1, 10000):
    if random() >= .87:
        a1wins = 1
    if random() >= .65:
        a2wins = 1
    if random() >= .17:
        a3wins = 1
    if a1wins + a2wins + a3wins >= 2:
        avictories = avictories + 1
    a1wins = 0
    a2wins = 0
    a3wins - 0

print (f"The number of times candidate A won was: {avictories}")
    



