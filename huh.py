from os import system
from random import randrange
+9

def main():

	system("cls")
	tantargy=input("Melyik tantárgyból?\n")
	jegyekszama=int(input("Hány jegye van?\n"))
	jegyz = 0
	felev = 0

	for i in range(jegyekszama):			
		osztalyzat = randrange(1,6)

		if (i+1) == fl(jegyekszama/2):
			felev=fl(jegyz/(jegyekszama/2))

		print(osztalyzat, end=" ")
		jegyz+=osztalyzat

	jegyz=round(jegyz/jegyekszama)

	if jegyz<2:
		print(f"\nFélév: {felev}\nMivel a tanuló {jegyz}. ra/re áll, ezért {tantargy} tantárgyból megbukott")

	elif 2<=jegyz and jegyz<2.5:
		print(f"\nFélév: {felev}\nMivell a tanuló {jegyz}. ra/re áll, ezért {tantargy} tantárgyból elégségesre lett le zárva")

	elif 2.5<=jegyz and jegyz<3.5:
		print(f"\nFélév: {felev}\nMivell a tanuló {jegyz}. ra/re áll, ezért {tantargy} tantárgyból közepesre lett le zárva")

	elif 3.5<=jegyz and jegyz<4.5:
		print(f"\nFélév: {felev}\nMivell a tanuló {jegyz}. ra/re áll, ezért {tantargy} tantárgyból jó lett le zárva")

	else:
		print(f"\nFélév: {felev}\nMivell a tanuló {jegyz}. ra/re áll, ezért {tantargy} tantárgyból jelesre lett le zárva")

if __name__ =='__main__':
	main()