import os
os.system("cls")
# írjon programot , mely egy bekért szövegben megszámolja, hogy hány karakter
sztring=input("Kérek egy szép szöveget")
#szokozdb=sztring.find(" "+1)
szokozdb=0
for i in range(0,len(sztring),1):
    if(sztring[i]==" "):
        szokozdb = szokozdb+1
print("A szövegben", len(sztring)-szokozdb,"szóköz nélküli karakter található")
print("A szövegben ", szokozdb+1,"szó található")