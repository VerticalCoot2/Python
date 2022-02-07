import os
import random

os.system("cls")
jegyek=random.randrange(200,501)
print("Az eladott jegyek száma: ", jegyek, "db/n")
bevetel=jegyek*320
print("A pénztár bevétele: ", bevetel, "Ft")
if(bevetel>112000 and bevetel<150000):
    ber=120000+(bevetel*0.01)
    print("Pénztáros fizetése: ", ber,"Ft")
else:
    ber=120000*0.99
    print("Pénztáros fizetése: ",ber,"Ft")