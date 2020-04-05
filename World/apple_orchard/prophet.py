'''The Prophet

He looks just like your grandfather!
Maybe you should talk to him!

'''

from Util import *
import os, importlib
import State


isPerson = True
CurrentLocation = os.path.dirname(__file__)

def talk():
    #checkState
    importlib.reload(State)
    if(not State.quest1complete) or (not State.quest1given):
        quest1()
    elif (not State.quest2complete) or (not State.quest2given):
        quest2()
    elif (State.CanLiberate()):
        if( not State.spokenToProphetOnLiberation):
            Say(__name__, "You’ve returned earlier than expected! It must have been a rough journey, O Explorer. But... ")
            Wait(2)
            Say(__name__,"have you solved everyone’s problems? You have? Then why is the world still the same? Hmm... this baffles me as well...")
            Pause()
            Say(__name__,"I don’t have the answer... But you ARE the file explorer! The answer must lie within You!")
            Update(State.__file__, "spokenToProphetOnLiberation","True")
        else:
            Say(__name__,"The answer must lie within You! Liberation must be *FUNDAMENTAL* for You!")
    else:
        Say(__name__,"How can I help, Explorer?")
        options = ["Where is the Grandmaster again?",
        "How do I move things again?",
        "How do I change FUNDAMENTAL properties again?",
        "What am I supposed to in this world?"
        "Nothing, I just wanted to talk."]
        choice = Ask(options)
        if (choice == 1):
            Say(__name__,"Ah, my grandmaster! He\’s been prophesising your arrival since the beginning of time! He should be at the market. Since you moved the apple, you surely can move yourself there.")
        elif (choice ==2):
            Say(__name__,"This Prophetic Neo Graphics (PNG) depicts a way to move things. Here you go.")
            Pause()
            Show("How_To_Move_Things.png")
        elif (choice ==3):
            Say(__name__,"This PNG will show you how to change *FUNDAMENTAL* properties. Be careful with it! ")
            Pause()
            Show("How_To_Change_Fundamental_Things.png")
        elif (choice == 4):
            Say(__name__,"Our evil creators have made our lives very, very difficult! Now that you’ve come, it is your calling to solve our mortal coils and fix this strange world! Only then can we all be liberated...")
        else:
            Say(__name__,"How kind of you. But alas I can only say what I was made to say.")


def quest1():

    #check if quest is complete
    applesInLocation = Search("apple", CurrentLocation)
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

            Say(__name__,"I have been yearning for the apple that is upon the tree for ages past. But alas, I am but lines of code in this world, unable to move! This Prophetic Neo Graphics (PNG) depicts a way to move things, but I cannot understand it. Perhaps you could help? Please bring me the apple!")
            Pause()
            Show("How_To_Move_Things.png")
            Update(State.__file__, "quest1given","True")
            Say(__name__,"Come back and talk to me when you’re done!")

        else:
            Say(__name__,"Do you want to see the PNG again?")

            options = ["Yes, please.",
            "No thank you."]
            if (Ask(options)==1):
                Say(__name__,"Here you go.")
                Pause()
                Show("How_To_Move_Things.png")

            Say(__name__,"Please Explorer, bring me the apple!Come back and talk to me when you’re done.")
    else:
        if (not State.quest1given):
            Say(__name__,"Hail Adventurer!")
            Say(__name__,"...")
            Wait(2)
            Say(__name__,"How... HOW DID YOU GET THE APPLE DOWN!?!?!? I have been here for ages pining for that apple. But alas, I am but lines of code in this world, unable to move. You must be the prophesised File Explorer!")
            Update(State.__file__, "quest1given","True")
        else:
            Say(__name__,"...")
            Wait(1)
            Say(__name__,"IT IS TRUE. You are the Explorer.")

        quest2()

def quest2():

    #get the apples in the location
    applesInLocation = Search("apple", CurrentLocation)
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
            Say(__name__,"Explorer, if you really are who you are, you must be able to change the *FUNDAMENTAL* properties of this apple. This PNG will show you how. Come back and talk to me when you’re done!")
            Pause()
            Show("How_To_Change_Fundamental_Things.png")
            Update(State.__file__, "quest2given","True")

        else:
            Say(__name__,"Do you want to see the PNG again?")

            options = ["Yes, please.",
            "No thank you."]
            if (Ask(options)==1):
                Say(__name__,"Here you go.")
                Pause()
                Show("How_To_Change_Fundamental_Things.png")

            Say(__name__,"Please Explorer, make this apple Red! Come back and talk to me when you’re done.")
    else:
        Say(__name__,"You have my utmost gratitude, O Explorer. Our evil creators have made our lives very, very difficult! Now that you’ve come, it is your calling to solve our mortal coils and fix this strange world! Only then can we all be liberated... Please, talk to me whenever you need to see the Prophetic Neo Graphics (PNG) again.")
        Pause()
        Say(__name__,"But for now, you should go see my grandmaster! He’s been prophesising your arrival since the beginning of time… but he should be at the market at this time of day, *YOU* should go there now and talk to him!")

lastWords ="""\
^rkxu*$y *py|*xy~*py|qo~~sxq*wo8*
S1!o*vs!on*"ovv*lo$yxn*w$*$ok|}6*wo~*kvv*usxn}*yp*zoyzvo*l ~*xyxo*yp*~row*"svv*o!o|*wk~mr* z*~y*$y 8
Pk|o"ovv*nok|*O#zvy|o|+*^ro*"y|vn*s}*kvv*$y |}*~y*o#zvy|o*xy"+\
"""
