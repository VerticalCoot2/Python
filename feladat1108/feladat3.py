import os

os.system("cls")
var = int(input("hányszor írjuk ki? "))
sztring = input("Mit?")

for i in range(1,var+1,1):
    print(sztring)
input("")
os.system("cls")

for i in range(10,210,10):
    print(i,end=" ")
for i in range(1,21,1):
    print(i,end=" ")
input("")
os.system("cls")

for i in range(0,10,1):
    print("{0:>10}".format("*"))
input("")
os.system("cls")

for i in range(0,10,1):
    print(" "*i, "*", sep="")
input("")
os.system("cls")

for i in range(0,10,1):
    print(" "*(9-i), "*", sep="")
input("")
os.system("cls")