import os
os.system("cls")
s=input("Adja meg a szöveget: \n")
karakter=input("keresendő karakter: ")
print("")
vane= False
print("A keresett karakkter pozíciói: ",end=" ")
for i in range(0,len(s),1):
    if s[i]==karakter:
        print("Pozíció: ",i+1)
        vane = True
if(not vane):
    print("nem jóu!")