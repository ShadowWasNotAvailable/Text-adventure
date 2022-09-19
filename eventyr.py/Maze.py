def room1 ():
    print ("Du er i et mørkt og stille rom med rød maling på veggene (Rom 1)")
    print ("Du ser 2 dører og må ta et valg 1/2")
    Room1Q = input ("-> ")
    if Room1Q == 1:
        room2 ()
    if Room1Q == 2:
        room3 ()
    
        

def room2 ():
    pass

def room3 ():
    pass

room1 ()