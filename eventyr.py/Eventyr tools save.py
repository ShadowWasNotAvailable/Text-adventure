from random import randint


global Mandelvann
Mandelvann = 0

def inventory():

    print(f"Ditt inventory:")


asking = True
while asking:
    print("dine valg a, b ,c")
    valg = input("-> ")

    if valg == "inventory":
        inventory()

    elif valg == "a":
        print("blabla")
        asking = False


Asking = input ("Will du se ditt inventory?")

if Asking == ("Y"):
    inventory()

print (f"{Mandelvann}")

 
