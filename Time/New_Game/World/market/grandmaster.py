'''Grandmaster

He looks just like your great-grandfather!

'''

from Util import *
import os, importlib
import State


isPerson = True
CurrentLocation = os.path.dirname(__file__)

def talk():
    #checkState
    if(not State.quest3complete) or (not State.quest3given):
        quest3()
    elif (not State.quest2complete) or (not State.quest2given):
        quest2()
    else:
        Say("Developer","Game's over dude.")


def quest3():

    #Everyone knows this is the correct way to count eggs.
    eggCounting = [1,2,3,5,4,6,9,11,7,13,12,8,10,14,15,16,18,19,17]
    basket = os.path.join(CurrentLocation,"basket")

    if (not State.quest3given):
        Say(__name__,"Ahh...")
        Wait(2)
        Say(__name__,"...")
        Wait(2)
        Say(__name__,"You must be the Explorer...")
        Wait(2)
        Say(__name__,"...")
        Wait(2)
        Say(__name__,"... but right now I need my proteins and fibres...")
        Wait(2)
        Say(__name__,"...")
        Wait(2)
        Say(__name__,"Please take this basket and bring me 10 eggs and 5 bell peppers!")
        Update(State.__file__, "quest3given","True")

    else:
        if(os.path.exists(basket)):
            eggsInBasket = Search("egg", basket)
            count = 0
            numEggs = 0
            verbalCount =""
            for egg in eggsInBasket:
                if (count>=len(eggCounting)):
                    verbalCount+="... That's too many to count!"
                    break
                else:
                    numEggs = eggCounting[count]
                    count +=1
                    verbalCount += str(numEggs)
                    if (count<len(eggsInBasket)):
                        verbalCount +=', '
                    else:
                        verbalCount +='.'

            Say(__name__,"Hmm...")
            Wait(count * 0.2)
            Say(__name__,verbalCount)

            if(numEggs==10):
                Say(__name__,"Ahh...")
                Wait(1)
                Say(__name__,"10 eggs...")
                Wait(1)
                Say(__name__,"Perfect...")
                Wait(1)
                Say(__name__,"Now for the bell peppers... ")
                Update(State.__file__,"quest3complete","True")
                quest4()
            elif(eggCounting.index(numEggs)>eggCounting.index(10)):
                Say(__name__,"Ahh...")
                Wait(1)
                Say(__name__,"There are too many eggs...")
                Wait(1)
                Say(__name__,"Please remove the extras from the basket.")
            else:
                Say(__name__,"Ahh...")
                Wait(1)
                Say(__name__,"There are not enough eggs...")
                Wait(1)
                Say(__name__,"Please go get some more.")

        else:
            Say("Hmm...")
            Wait(2)
            Say("Where's my basket?")

    importlib.reload(State)

def quest2():

    #get the apples in the location
    applesInLocation = Search("Apple", CurrentLocation)
    if (applesInLocation):
        for apple in applesInLocation:
            globals()[apple] = importlib.import_module(apple)
            if (globals()[apple].Colour != "Red"):
                Say(__name__, "This "+apple+" is not Red, it is "+ globals()[apple].Colour)
            else:
                Update(State.__file__, "quest2complete", "True")
    else:
        Say(__name__,"Where did the apple go!? Please Explorer, let me have my apple. Do not torture me so! ")
        return

    importlib.reload(State)

    if (not State.quest2complete):
        if (not State.quest2given):
            Say(__name__,"Alas, woe is me! Are there no apples I can eat?")
            Wait(2)
            Say(__name__,"Explorer, if you really are who you are, you must be able to change the *FUNDAMENTAL* properties of this apple. This PNG will show you how.")
            Show("How_To_Change_Fundamental_Things.png")
            Update(State.__file__, "quest2given","True")

        else:
            Say(__name__,"Do you want to see the PNG again?")

            options = ["Yes, please.",
            "No thank you."]
            if (Ask(options)==1):
                Say(__name__,"Here you go.")
                Show("How_To_Change_Fundamental_Things.png")

            Say(__name__,"Please Explorer, make this apple Red!")
    else:
        Say(__name__,"You have my utmost gratitude, O Explorer. Please, talk to me whenever you need to see the Prophetic Neo Graphics (PNG) again.")
        Say("Developer","You have come to the end of the tutorial/Demo! Thanks for playing!")
