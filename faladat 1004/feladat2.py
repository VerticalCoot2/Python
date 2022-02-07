import os
os.system("cls")

hom=int(input("A hőmérséklet: "))
if(hom<0):
    print("A halmazaállapot: szilárd")
elif(hom<=100):
    print("A halmazálalpot: folyadék")
else:
    print("a halmazállapot: légnemű")