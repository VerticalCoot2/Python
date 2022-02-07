import os

os.system("cls")
print("STRING MŰVELETEK")
s1="Csokonai Vitéz Mihály"
print("A költő neve: ", s1)

#Harmadik karakter kiírása
print ("A harmadik karakter:", s1[2])

#A középső név kiírása
print ("A középső név kiírása", s1[9:14])

#Hol kezdődok a középső név
print ("A középső név kezdete: ", s1.find("Vitéz")+1)

#költő nevének hossza
print ("A költő mevének hossza: ", len(s1))

#hozzáfűzés:
s1 = s1+" költő"
print(s1)

# o beszúrása
s1 = s1.split()[0]+"o"+ s1[8:27]
print (s1)

# o törlése
s1=s1[0:8]+s1[9:28]
print("az o törlése után",s1)

#A "V" t cserélkük ki "v" re
print("Csere után: ", s1.replace("V","v"))