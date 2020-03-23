'''Grandmaster

He looks just like your great-grandfather!

'''

from Util import *
import os, importlib
import State


isPerson = True
CurrentLocation = os.path.dirname(__file__)
basket = os.path.join(CurrentLocation,"basket")

def talk():

    #checkState
    importlib.reload(State)
    
    if(not State.quest3complete) or (not State.quest3given):
        quest3()
    elif (not State.quest4complete):
        quest4()
    else:
        Say("Developer","Game's over dude.")

def Count(items, countingMethod):
    count = 0
    numItems = 0
    verbalCount =""
    for item in items:
        if (count>=len(countingMethod)):
            verbalCount+="... That's too many to count!"
            break
        else:
            numItems = countingMethod[count]
            count +=1
            verbalCount += str(numItems)
            if (count<len(items)):
                verbalCount +=', '
            else:
                verbalCount +='.'
    Wait(count * 0.2)
    Say(__name__, verbalCount)
    return numItems

def quest3():

    #Everyone knows this is the correct way to count eggs.
    eggCounting = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]

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
        Update(State.__file__, "quest4given","True")

    else:

        Say(__name__,"...")
        Wait(3)
        Say(__name__,"Ahh! You scared me. Do you have my eggs and peppers?")
        Pause()

        if(os.path.exists(basket)):
            eggsInBasket = Search("egg", basket)
            count = 0
            numEggs = 0
            verbalCount =""
            for egg in eggsInBasket:
                globals()[egg] = importlib.import_module("basket."+egg)
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

            Say(__name__,"Let’s see how many we have here...")
            Wait(count * 0.2)
            Say(__name__,verbalCount)

            if(numEggs==10):
                Say(__name__,"Ahh...")
                Wait(1)
                Say(__name__,"10 eggs...")
                Wait(1)
                Say(__name__,"Perfect...")
                Wait(1)
                Say(__name__,"*Munch*")
                Wait(2)
                Say(__name__,"*Crunch*")
                for egg in eggsInBasket:
                    Consume(globals()[egg].__file__)
                Wait(2)
                Say(__name__,"That was tastey. Now for the bell peppers... ")

                Update(State.__file__,"quest3complete","True")
                quest4()
            else:
                if(numEggs == 0 or eggCounting.index(numEggs)<eggCounting.index(10)):
                    Say(__name__,str(numEggs)+"? There are not enough eggs...")
                else:
                    Say(__name__,str(numEggs)+"? There are too many eggs...")
                Wait(1)
                Say(__name__,"I thought I said 10! Do you not know how to count eggs? Counting is *FUNDAMENTAL* for the chosen one...")

        else:
            Say(__name__,"Hmm...")
            Wait(2)
            Say(__name__,"Where's my basket?")



def quest4():

    #Everyone knows you don't count bellpeppers the same way you count eggs.
    bellpepperCounting= [1,2,3,4,6,9,11,7,13,12,8,10, 5,14,15,16,18,19,17]
    Say(__name__,"...")
    Wait(3)
    Say(__name__,"Ahh! You scared me. Do you have my peppers?")
    Pause()

    if(os.path.exists(basket)):
        bellpepperInBasket = Search("bellpepper", basket)

        Say(__name__,"Let’s see how many we have here...")
        numBellpeppers = Count(bellpepperInBasket, bellpepperCounting)

        if(numBellpeppers==5):
            Say(__name__,"Ahh...")
            Wait(1)
            Say(__name__,"5 bellpeppers...")
            Wait(1)
            Say(__name__,"Perfect...")
            Wait(1)
            Say(__name__,"*Munch*")
            Wait(2)
            allGreen = True
            for bellpepper in bellpepperInBasket:
                globals()[bellpepper] = importlib.import_module("basket."+bellpepper)
                if (globals()[bellpepper].Colour != "Green"):
                    Say(__name__, "Why did you bring me red apples? "+ bellpepper.__name__+" is not green. Bell peppers should be green. Go find the right ones.")
                    allGreen = False
                    break
            if (allGreen):
                Say(__name__,"*Crunch*")
                Wait(2)
                for bellpepper in bellpepperInBasket:
                    Consume(globals()[bellpepper].__file__)
                Say(__name__,"That was tastey.")
                Update(State.__file__,"quest4complete","True")
        else:
            if(numBellpeppers==0 or bellpepperCounting.index(numBellpeppers)<bellpepperCounting.index(5)):
                Say(__name__,str(numBellpeppers)+"? There are not enough bellpeppers...")
            else:
                Say(__name__,str(numBellpeppers)+"? There are too many bellpeppers...")
            Wait(1)
            Say(__name__,"I thought I said 5! Do you not know how to count eggs? Counting is *FUNDAMENTAL* for the chosen one...")

    else:
        Say(__name__,"Hmm...")
        Wait(2)
        Say(__name__,"Where's my basket?")
