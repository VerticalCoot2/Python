import os

os.system("cls")
szamlalo=int(input("Számláló: "))
nevezo=int(input("Nevező:"))
if(nevezo==0):
    print("Nem lehet nullával osztani :) Butta vagy ;) ")
elif(szamlalo==nevezo):
    print("Hát az eredményed egy egész :O")
else:
    print("Az eredmény: ",szamlalo/nevezo)