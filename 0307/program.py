from os import system as k
from random import randrange as randi

k("cls")
berek=[[0]*3 for i in range(3)]
print("Minimál bérek: ")
for i in range(3):
        for j in range(3):
            berek[i][j]=randi(500,1201)
            print(f"{berek[i][j]}", end=" ")
        print("")