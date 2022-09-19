from random import randint


Eple = 0
Penger = 100


print ("Du gikk in på buttiken og så et eple.")
print (f"Du har {Penger} kroner og du har lyst på 1 eple som er 15 kroner.")
epler = input("Skal du kjøpe eple? J/N.")

if epler == "J" or "j":
    print ("Du kjøpte eple for 15 kroner.")
    Penger -= 15
    Eple += 1

if epler == "n" or "n":
    print ("Du kjøpte ikke eple.")


print ("Du gikk ut av butikken og ble litt sulten.")
if Eple < 1:
    print ("Du kjøpte ikke eple så du må finne noe annet")
else:
    QSpise = input ("Spis eple? J/N.")

    if QSpise == ("J" or "j"):
        print ("Du spiste eple og følte ikke like sulten lengre.")
        Eple -= 1

    if QSpise == ("N" or "n"):
        print ("Du hadde lyst til å spare eple til noe godt senere.")
        print ("Du er fortsatt sulten og har lyst på noe å spise.")

Qvalg = input ("Skal du se etter noe å spise? J/N.")

if Qvalg == ("J" or "j"):
    print ("Du gikk litt rundt for å se etter noe å spise.")
    print ("Du fant en resturang.")

Qresturang = input ("Skal du gå inn i resturangen? J/N.")

if Qresturang == ("J" or "j"):
    print ("Du gikk inn i resturangen.")
    print ("Du satt deg ned å ventet på en meny.")
    print ("Det kom en ung gutt å ga deg en meny.")
    print ("Du så på det som var i menyen.")
    print ("Du så at de hadde kebab for 55 kroner.")


Qkebab = input ("Skal du kjøpe kebab for 55 kroner? J/N.")

if Qkebab == ("J" or "j"):
    print ("Du kjøpte og spiste kebab.")
    Penger -= 55
    print (f"Du har nå {Penger} kroner.")












if Penger < 1:
    print ("Du har ikke noe mer penger og må dra hjem.")
    print ("End.")

    exit