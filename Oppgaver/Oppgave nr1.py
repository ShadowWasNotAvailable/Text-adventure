from random import randint
from tkinter import END, Y

def rom666 ():
    dør = randint (1,2)
    Chance = input ("->")
        
    if Chance == "Y":
    
    if dør == 1:
        print ("Du åpner døren og går inn, Du lukker døren bak deg og ser den forsvinne, et sterkt hvit lys skyter mot deg og du hører en stemme i hode som sier: Gratulerer du fikk deg ut.")
        exit
    else:
        print ("Du åpner døren og går inn, Du lukker døren bak deg og ser den forsvinne, Rommer er helt svart og helt stille, Du hører en stemme i hode som sier: Ser ut som det er ende en som kommer til å bli spist av mørket.")
        exit

def rom3 ():
    print(".")
    print(".")
    
    Choice4 = True
    while Choice4:
        Valg4 = input ("->")
        if Valg4 == "1":
            print("")
            Choice4 = False
        elif Valg4 == "2":
            print(".")
            Choice4 = False
    
        else:
            print ("Ops du skrev noe feil prøv på nytt!")

def rom2 ():
    print(".")
    print(".")
    
    Choice3 = True
    while Choice3:
        Valg3 = input ("->")
        if Valg3 == "1":
            print("")
            Choice3 = False
        elif Valg3 == "2":
            print(".")
            Choice3 = False
    
        else:
            print ("Ops du skrev noe feil prøv på nytt!")

def rom1 ():
    print("Etter å ha gått in i rom 1 hører du et brøl.")
    print("I panikk tenker du: 1. Skal jeg springe 2. Skal jeg prøve å gjømme meg.")
    
    Choice2 = True
    while Choice2:
        Valg2 = input ("->")
        if Valg2 == "1":
            print("Du springer uten å tenke på hvor du springer etter å ha sprunget i 5 minutter stopper du og ser bak deg, Du ser at tingen som løp etter deg er borte du prøver å finne ut av hvor du er, du finner en dør med røde prikker som sier denne døren har en 50/50 skjangse på å redde deg eller å drepe deg. skal du prøve å åpne denne døren med 50/50 skjangse till å få deg ut eller skal du ignorere den? Y/N")
            Choice2 = False
            rom666 ()


        elif Valg2 == "2":
            print("Du gjømte deg i et hjørne og så en lang mørk figur passere forbi rommet påsiden av deg.")
            Choice2 = False
    
        else:
            print ("Ops du skrev noe feil prøv på nytt!")



print("Du våkner opp i et rart rom. Det er gule vegger med blomster figurer på dem, hele gulvet er laget av teppe og det lukter våt katt, Du velger å røre teppt og kjenner at det er våt.")
print("Du tenker: Var ikke jeg ikke netopp i senga, dette må være en drømm. Du kliper deg selv og det gjør ondt, du får en dårlig følelse og er litt i panikk. Etter en liten stund tar du deg sammen og begynner å vandre rundt.")
print("Du går til rommet på siden av der du våknet der kan du gå 3 forskjellige veier hvilken skal du velge?")
print("1. 2. 3.")

Choice = True
while Choice:
 Valg1 = input ("->")

 if Valg1 == "1":
    print("Du går mot rom 1.")
    Choice = False
    rom1 ()

 elif Valg1 == "2":
    print("Du går mot rom 2.")
    Choice = False
    rom2 ()

 elif Valg1 == "3":
    print("Du går mot rom 3.")
    Choice = False
    rom3 ()

 else:
    print ("Ops du skrev noe feil prøv på nytt!")
        



