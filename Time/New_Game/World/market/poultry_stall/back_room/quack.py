'''The Quack

Surprisingly, he does not look like your father.

'''

from Util import *
import os, importlib
import State


isPerson = True
CurrentLocation = os.path.dirname(__file__)

def talk():
    #checkState
    importlib.reload(State)

    if (not State.quest6complete):
        quest6()
    else:
        if (State.CanLiberate()):
            Say(__name__,"Did you not go to the prophet? I have no more words for you!")
        else:
            Say(__name__, "There's still someone that needs your help! Why are you still here? Go help them!")


def quest6():

    conversation = {
    "Who are you?":
        ["I am the messenger! The one who awaits the File Explorer.",
        "I can’t remember. Just some ass pretending to be a hero."],
    "Behold, I am the File Explorer.":
        ["Is that true!?" ,
        "Yeah right. And I am the messenger."],
    "Why are you here?":
        ["Because the Explorer is nowhere to be found… And we shall all be trapped in an eternity of pain and suffering!",
        "No one shares my pain… not even my wife! That wench… HELP ME"],
    "Stop doing that.":
        ["I can’t help but to punch the door...",
        "Who are you to tell me what to do?"],
    "Nevermind.":[]
    }

    options = list(conversation)

    trainOfThought = [4,1,2,1]

    Say(__name__,"*thump* *thump* ")
    Wait(1.5)
    Say(__name__,"*thump* *thump* ")
    Wait(1.5)
    Say(__name__,"*thump* *thump* ")
    Pause()

    response = 0
    responseTrain = []
    followingTrainOfThought = True

    while (len(options)!=1):
        response = Ask(options)
        if (response!=len(options)):
            playerResponse = options.pop(response-1)
            responseTrain.append(response)
            for i in range(len(responseTrain)):
                if (trainOfThought[i]!= responseTrain[i]):
                    followingTrainOfThought = False
            Wait(2)
            if (followingTrainOfThought):
                Say(__name__, conversation[playerResponse][0])
            else:
                Say(__name__, conversation[playerResponse][1])
            Wait(2)
        else:
            followingTrainOfThought = False
            break

    if (not followingTrainOfThought):
        Say(__name__, "We all remain trapped in this eternal madness... until I find the real Explorer, the only one who can communicate with me in the predestined way!")
    else:
        Update(State.__file__, "quest6complete", "True")
        importlib.reload(State)
        Say(__name__, "If it be true, salvation is upon us! I was driven to madness by my despair of your absence… I can finally let everyone know that you have come. Now all that’s left is to wait and see the miracles that you can do...")
        Wait(1)
        Say(__name__, "...")
        Wait(2)
        if (State.CanLiberate()):
            Say(__name__, "Wait... you’ve solved everyone’s woes... the prophet prophesied that you’ll liberate all of us! Why are we all still here? You have to go to him and find out why!")
        else:
            Say(__name__, "Wait... there's still someone that needs your help! Why are you still here? Go help them!")
