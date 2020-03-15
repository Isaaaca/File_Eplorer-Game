'''The Prophet

'''

from Util import *
import os
import ProphetState as State


Type = 'person'
CurrentLocation = os.path.dirname(__file__)

def talk():
    #checkState
    if(not State.quest1complete) or (not State.quest1given):
        quest1()

def quest1():
    wrapper = textwrap.TextWrapper()
    wrapper.initial_indent = "* "
    print('\n',__name__)

    #check if quest is complete
    appleInLocation = os.path.exists(os.path.join(CurrentLocation, "Apple.py"))
    if (appleInLocation):
        pass
        #update the state and reimport


    if (not State.quest1complete):
        if (not State.quest1given):
            Say("Hail Adventurer! I have not seen you in these parts before. Could you be the prophesied File Explorer?")
            options = ["I don\'t know, I just got here.",
            "Perhaps.",
            "I don\'t think so..."]
            Ask(options)

            print('\n',__name__)
            Say("I have been earning for the apple that is upon the tree for ages past. But alas, I am but lines of code in this world, unable to move! This Prophecy Neo Graphics (PNG) depicts a way to move things, but I cannot understand it. Perhaps you could help? Please bring me the apple!")
            Show("poop.png")
        else:
            Say("Please Explorer, bring me the apple!")
