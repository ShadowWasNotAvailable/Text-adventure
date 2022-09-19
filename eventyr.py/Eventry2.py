from random import randint

penger = randint (100 , 6000)

def inventory():
    inven = input ("Bank or Inventory. -> ")
    if inven == ("Bank" or "bank"):
        print (f"Du har" , {penger} , "Kroner")
    
    if inven == ("Inventory" or "inventory"):
        print (f"Dette har du i inventory")

Asking = input ("Vil du se din inventory? Y/N -> ")

if Asking == ("Y" or "y"):
    inventory()
