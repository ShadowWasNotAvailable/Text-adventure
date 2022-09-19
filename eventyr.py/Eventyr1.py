from random import randint

lommelykt = randint (0 , 1)
tau = randint (0 , 1)
penger = randint (0 , 500)
energibar = randint (2 , 4)
kniv = randint (0 , 1)



Name = input ("Enter name here. -> ")

print (f"{Name} Våkner opp midt i en skog og husker ingen ting, {Name} legger merke til at han har en ryggsekk som er litt tung, {Name} velger å sjekke hva han har i sekken.")

if lommelykt == 1:
    print (f"{Name} fant en lommelykt i sekken!")
if tau == 1:
    print (f"{Name} fant et tau i sekken!")
if penger > 1:
    print (f"{Name} fant {penger} kroner i sekken!")
if energibar == 1:
    print (f"{Name} fant en energibar i sekken!")
if energibar > 2:
    print (f"{Name} fant {energibar} energibarer i sekken!")
if kniv == 1:
    print (f"{Name} fant en kniv i sekken!")




