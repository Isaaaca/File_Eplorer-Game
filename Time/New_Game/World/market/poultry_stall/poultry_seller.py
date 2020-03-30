'''Poultry Seller

She looks just like your mother!

'''

from Util import *
import os, importlib
import State


isPerson = True
CurrentLocation = os.path.dirname(__file__)

def talk():

    #checkState
    importlib.reload(State)

    if(not State.quest5complete) or (not State.quest5given):
        quest5()
    elif (not State.quest6complete):
        quest6()
    else:
        Say("Developer","Game's over dude.")


def quest5():


    if (not State.quest5given):
        Say(__name__,"You! You must be the Explorer everyone is talking about.")
        options = ["For Sure! Worry not, for I am here!",
        "Why do you ask?",
        "You probably got the wrong person..."]
        reply = Ask(options)
        if (reply ==1):
            Say(__name__,"Thank heavens! You must help me!")
        elif (reply==2):
            Say(__name__,"You must help me!")
        elif (reply == 3):
            Say(__name__,"Nonesense. Who else could you be? You must help me!")
        Pause();

        Say(__name__,"My poultry have turned grey. It got hexed wrongly! It’s supposed to be PeachPuff coloured. Please do something about it! ")
        Update(State.__file__, "quest5given","True")

    else:

        options = ["I've already fixed it, please check it out.",
        "What colour is it supposed to be again?",
        "What's a hex?",
        "I'll be back."]
        reply = 0
        while (reply!=4):
            Say(__name__,"Explorer, please fix my poultry!")
            reply = Ask(options)
            if (reply ==1):
                poultryInLocation = Search("poultry", CurrentLocation)
                for poultry in poultryInLocation:
                    if (not "seller" in poultry):
                        if (poultry in globals()):
                            importlib.reload(globals()[poultry])
                        else:
                            globals()[poultry] = importlib.import_module(poultry)
                        if (globals()[poultry].Colour.lower() != "#ffdab9"):
                            Say(__name__, "This "+poultry+" is not PeachPuff, it is "+ globals()[poultry].Colour+". It still has the wrong hex!")
                        else:
                            Update(State.__file__, "quest5complete", "True")
                            importlib.reload(State)
                            reply = 4
            elif (reply==2):
                Say(__name__,"The best poultry are hexed to be PeachPuff colored!")
            elif (reply == 3):
                Say(__name__,"Not all hexes are bad. I only know that the color of the poultry can change depending on how it is hexed. I heard rumors of an \"Interweb\" where information can be found. I wonder what kind of spider weaved such thing?")

            if (reply!=4):
                Pause()


        if (State.quest5complete):
            Say(__name__,"Thank you! Oh, what would I have done without you! I\’m eternally grateful for your help!")
            quest6()





def quest6():
    if(not State.quest6given):
        Wait(3)
        Say("???","*thump* *thump* ")
        Wait(3)
        Say("???","*thump* *thump* ")
        options = ["What was that?",
        "Did you hear that?",
        "Ma'am, standback."]
        Ask(options)
        Say(__name__, "It’s my husband... He's a quest that we have not implemented yet. Stay tuned for updates!")
        Update(State.__file__, "quest6given", "True")
        Update(State.__file__, "quest6complete", "True")
    else:
        Say("Developer","Game's over dude.")
