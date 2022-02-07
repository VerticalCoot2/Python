import os
import random
import math
os.system("cls")

cukor=float(input("Kérem a sugár értékét: "))
#cukor=random.randrange(20,51)
#cukor=1
#cukor=int(input("kérem a kör sugarát: "))
#cukor=random.randrange(20, 51)
#cukor=random.randrange(int(input("Kérem a lehető legkisebb számot: ")), int(input("kérem a legnagyobb számot: ")))

print("A sugár mérete: ", cukor)
kalkulating=((cukor*cukor)*(math.pi))
print("a kör területe:", round(kalkulating))
