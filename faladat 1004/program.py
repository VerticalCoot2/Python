import os
os.system("cls")


szam=int(input("Számot!: "))
"""if(szam>10):
    print(szam*2)
elif(szam==10):
    print("Nyertél, grat")
else:
    print(szam+5)
if(szam!=10):
    print(szam*2)
else:
    print(szam+5)"""
if(szam<10 and szam%2==0):
    print("Páros")
else:
    print("Páratlan")