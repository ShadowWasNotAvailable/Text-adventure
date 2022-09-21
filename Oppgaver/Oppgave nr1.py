from random import randint


Liv = 100
Mandelvann = 0
Pistol = 0
Pistolskudd = 0

def inventory():

    print(f"Ditt inventory:")


    asking = True
    while asking:
        print("Hva vil du se?")
        print("Inventory eller Status")
        Inv = input("->")
        
        if Inv == ("Inventory"):
            print("Ditt inventory")
            if Mandelvann < 1:
                print(f"Du har {Mandelvann} mandelvann")
            if Pistol < 1:
                print(f"Du har en {Pistol} med {Pistolskudd} skudd")
        

        elif Inv == ("Status"):
            print ("Dette er din status")
            print (f"Du har {Liv} liv.")

def rom666 ():
    dør = randint (1,2)
    Chance = input ("->")
        
    if Chance == "Y" or "y":
        if dør == 1:
            print ("Du åpner døren og går inn, Du lukker døren bak deg og ser den forsvinne, et sterkt hvit lys skyter mot deg og du hører en stemme i hode som sier: Gratulerer du fikk deg ut.")
            exit
        else:
            print ("Du åpner døren og går inn, Du lukker døren bak deg og ser den forsvinne, Rommer er helt svart og helt stille, Du hører en stemme i hode som sier: Ser ut som det er enda en som kommer til å bli spist av mørket.")
            exit
    
    elif Chance == "N" or "n":
        print ("WIP To be continued")

def rom3 ():
    print("Du kommer in til rom 3 og ser rundt i rommet.")
    print("Du ser en boks i hjørnet men den er låst skal du prøve å ødelegge boxen for å få tak i det som er på insiden? Y/N")
    
    Start ()

    R3Choice1 = True
    while R3Choice1:
        global Liv

        Valg4 = input ("->")
        if Valg4 == "Y" or "y":
            Liv =- 10
            print(f"Du knuser boksen med hendene dine men du skader hendene dine, det tar 10 Liv, Du har nå {Liv} liv.")
            print("Du går tilbake til der du kom fra.")
            R3Choice1 = False
        
        elif Valg4 == "N" or "n":
            print("Du velger å ikke ødelegge boksen og lar den ligge og går tilbake til der du kom fra.")
            R3Choice1 = False
    
        else:
            print ("Ops du skrev noe feil prøv på nytt!")

    R3Choice2 = True
    while R3Choice2:
        print ("Skal du gå tilbake? Y/N")
        Choice = input ("->")
        
        if Choice == "Y" or "y":
            print ("Du går tilbake")
            R3Choice2 = False
            Start ()

        elif Choice == "N" or "n":
            print ("WIP du går tilbake")
            R3Choice2 = False
            Start ()

        else:
            print ("Ops du skrev noe feil prøv på nytt!")
        
def rom2 ():
    print("Du kommer in til rom 2 og ser rundt i rommet.")
    print("Du ser at det ligger noe i et mørkt hjørne skal du se hva det er? J/N.")

    R2Choice = True
    while R2Choice:
        global Liv
        global Pistol
        Valg3 = input ("->")
        
        if Valg3 == "J" or "j":
            print("Du går til hjørnet og prøver å ta det som ligger der.")
            Liv -= 5
            print(f"En rotte biter deg og tar 5 liv. Du har nå {Liv} liv.")
            print("Du tar pistolen etter rotten sprang vekk")
            Pistol += 1
            R2Choice = False
        
        elif Valg3 == "N" or "n":
            print(".")
            R2Choice = False
    
        else:
            print ("Ops du skrev noe feil prøv på nytt!")
                
def rom1 ():
    global Mandelvann
    print("Etter å ha gått in i rom 1 hører du et brøl.")
    print("I panikk tenker du: 1. Skal jeg springe 2. Skal jeg prøve å gjømme meg.")
    
    R1Choice1 = True
    while R1Choice1:
        Valg2 = input ("->")
        if Valg2 == "1":
            print("Du springer uten å tenke på hvor du springer etter å ha sprunget i rundt 5 minutter stopper du og ser bak deg, Du ser at tingen som løp etter deg er borte du prøver å finne ut av hvor du er, du finner en dør med røde prikker som sier denne døren har en 50/50 skjangse på å redde deg eller å drepe deg. skal du prøve å åpne denne døren med 50/50 skjangse till å få deg ut eller skal du ignorere den? Y/N")
            R1Choice1 = False
            rom666 ()


        elif Valg2 == "2":
            print("Du prøver å finne et sted å gjømte deg, Du ser i mot et hjørne og der ligger det en sekk du velger å gjømme deg i hjørnet bak sekken etter 1/2 minutt så går en lang mørk figur forbi og in i rommet påsiden av deg.")   
            print("Etter at figuren har blitt borte åpner du sekken og finner 3 mandelvann på box")
            Mandelvann += 3
            print(f"Du har nå {Mandelvann} Mandelvann")
            R1Choice1 = False
    
        else:
            print ("Ops du skrev noe feil prøv på nytt!")

def Start ():
    StartChoice = True
    while StartChoice:
        print("1. 2. 3.")
        Valg1 = input ("->")

        if Valg1 == "1":
            print("Du går mot rom 1.")
            StartChoice = False
            rom1 ()

        elif Valg1 == "2":
            print("Du går mot rom 2.")
            StartChoice = False
            rom2 ()

        elif Valg1 == "3":
            print("Du går mot rom 3.")
            StartChoice = False
            rom3 ()

        else:
            print ("Ops du skrev noe feil prøv på nytt!")

print("Du våkner opp i et rart rom. Det er gule vegger med blomster figurer på dem, hele gulvet er laget av teppe og det lukter våt katt, Du velger å røre teppt og kjenner at det er våt.")
print("Du tenker: Var ikke jeg ikke netopp i senga, dette må være en drømm. Du kliper deg selv og det gjør ondt, du får en dårlig følelse og er litt i panikk. Etter en liten stund tar du deg sammen og begynner å vandre rundt.")
print("Du går til rommet på siden av der du våknet der kan du gå 3 forskjellige veier hvilken skal du velge?")
Start ()