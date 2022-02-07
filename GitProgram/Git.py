from os import system
import sys
def Main():
    hdd=str(input("Please enter the Storage Drive's letter"))
    folder=str(input("Please enter the folder path"))
    userName=str(input("Please enter your GitHub username"))
    userEmail=str(input("Please enter your GitHub email"))
    system(f"{hdd}:")
    system(f"cd {folder}")
    system(f"git init")




if __name__=='__main__':
    Main()