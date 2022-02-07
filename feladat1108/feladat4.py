import os

os.system("cls")

for i in range(0,5,1):
    for j in range(0,5,1):
        print("*", end="")
    print("")
input("")
os.system("cls")

for i in range (0,21,1):
    for j in range(0,21,1):
        print("{0:>4}".format(i*j), end=" ")
    print("")