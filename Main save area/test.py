
Question = input ("Hva er 2+4? ")
Question = int(Question)

if Question > 6:
    print (Question , "var feil svar.")

if Question < 6:
    print (Question , "var feil svar.")

if Question == 6:
    print ("Bra 6 var rett svar!")



QuestionP = input ("Hva er 600+44? ")
QuestionP = int(QuestionP)

if QuestionP > 644:
    print (QuestionP , "var Feil svar.")

if QuestionP < 644:
    print (QuestionP , "var Feil svar.")

if QuestionP == 644:
    print ("Bra" , QuestionP , "var rett svar!")




print ("Hva er 4*6")
print ("A. 24")
print ("B. 22")
print ("C. 20")
ABC = input ("->")


if ABC == "A" or "a":
    print ("Rett")

if ABC == "B" or "b":
    print ("Feil")

if ABC == "C" or "c":
    print ("Feil")



print ("Hva er 200 + 111")
print ("A. 312")
print ("B. 222")
print ("C. 311")
ABC = input ("->")


if ABC == "A" or "a":
    print ("Feil")

if ABC == "B" or "b":
    print ("Feil")

if ABC == "C" or "c":
    print ("Rett")



Eple = 0
Penger = 100
print ("Du gikk in på buttiken og så et eple")
print (f"Du har {Penger} kroner og du har lyst på 1 eple som er 15 kr")
epler = input("Skal du kjøpe eple? J/N.")

if epler == "J" or "j":
    print ("Du kjøpte eple for 15 kroner")
    Penger = 85
    Eple = 1

if epler == "N" or "n":
    print ("Du kjøpte ikke eple")

print ("Du gikk ut av butikken og ble litt sulten")
Spise = input ("Spis eple? J/N")

if Spise == ("J" or "j"):
    print ("Du spiste eple og følte ikke like sulten lengre")
    Eple = 0

if Spise == ("N" or "n"):
    print ("Du hadde lyst til å spare eple til noe godt senere")

