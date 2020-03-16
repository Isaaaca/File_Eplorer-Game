'''The Prophet

'''

from Util import *
import os, importlib
import ProphetState as State


isPerson = True
CurrentLocation = os.path.dirname(__file__)

def talk():
    #checkState
    if(not State.quest1complete) or (not State.quest1given):
        quest1()
    elif (not State.quest2complete) or (not State.quest2given):
        quest2()

def quest1():

    #check if quest is complete
    applesInLocation = Search("Apple", CurrentLocation)
    if (applesInLocation):
        #update the state and reimport
        Update(State.__file__, "quest1complete","True")

    importlib.reload(State)

    if (not State.quest1complete):
        if (not State.quest1given):
            Say(__name__,"Hail Adventurer! I have not seen you in these parts before. Could you be the prophesied File Explorer?")

            options = ["I don\'t know, I just got here.",
            "Perhaps.",
            "I don\'t think so..."]
            Ask(options)

            Say(__name__,"I have been earning for the apple that is upon the tree for ages past. But alas, I am but lines of code in this world, unable to move! This Prophetic Neo Graphics (PNG) depicts a way to move things, but I cannot understand it. Perhaps you could help? Please bring me the apple!")
            Show("poop.png")
            Update(State.__file__, "quest1given","True")

        else:
            Say(__name__,"Do you want to see the PNG again?")

            options = ["Yes, please.",
            "No thank you."]
            if (Ask(options)==1):
                Say(__name__,"Here you go.")
                Show("poop.png")

            Say(__name__,"Please Explorer, bring me the apple!")
    else:
        if (not State.quest1given):
            Say(__name__,"Hail Adventurer!")
            Say(__name__,"...")
            Wait(2)
            Say(__name__,"How... HOW DID YOU GET THE APPLE DOWN!?!?!? I have been here for ages pining for that apple. But alas, I am but lines of code in this world, unable to move. You must be the prophesised File Explorer!")
        else:
            Say(__name__,"...")
            Wait(1)
            Say(__name__,"IT IS TRUE. You are the Explorer.")

        quest2()

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
            Show("poop.png")
            Update(State.__file__, "quest2given","True")

        else:
            Say(__name__,"Do you want to see the PNG again?")

            options = ["Yes, please.",
            "No thank you."]
            if (Ask(options)==1):
                Say(__name__,"Here you go.")
                Show("poop.png")

            Say(__name__,"Please Explorer, make this apple Red!")
    else:
        Say(__name__,"You have my utmost gratitude, O Explorer. Please, talk to me whenever you need to see the Prophetic Neo Graphics (PNG) again.")
        Say("Developer","You have come to the end of the tutorial/Demo! Thanks for playing!")
