import inspect, os
import State
from Util import *

def help(command = ""):
    """COMMAND: HELP
    For learning how to use commands.
    Enter "help()" to see your available commands.
    Enter "help(<command_name>)" to learn more about a command.
    """
    UpdateState()
    print()
    if (command):
        if(callable(command)):
            print(inspect.getdoc(command))
        else:
            print(command.__name__ + " is not a command. Enter \"help()\" to see a list of available commands")
    else:
        print("Available Commands:")
        print("\"look()\"")
        print("\"talk()\"")
        print("\"help()\"")
        print("\nEnter \"help(<command_name>)\" to learn more about a command.")
        print("E.g. \"help(look)\",\"help(talk)\"")
        print("Remember to look before you do anything when you move to a different location!\n")
        print("Don't forget to try out all the commands!")
    print()

def look(thing = ""):
    """COMMAND: LOOK
    For looking at objects, places or people.
    Enter "look()" to look at your surroundings.
    Enter "look(<name>)" to take a closer look at something.
    """
    UpdateState()
    print()
    if not thing:
        print('You are currently in ' + CurrentLocation.__name__ + '\n')
        print('The following things/people are here:')
        for interactable in interactables:
            print(interactable)
    else:
        print(inspect.getdoc(thing))
    print("\nEnter \"look(<name>)\" to take a closer look at something.")
    print("Enter \"talk(<name>)\" to have a conversation with someone")
    print()




def talk(person = ""):
    """COMMAND: TALK
    For talking to people.
    Enter "talk()" to view and select someone to talk to.
    Enter "talk(<name>)" to directly enter into conversation with the person.
    """
    UpdateState()
    print()
    if not person:
        persons = []
        for interactable in interactables:
            if (hasattr(globals()[interactable], 'isPerson')):
                persons.append(interactable)
        if (len(persons)==0):
            print("There is no one to talk to here.\n")
        else:
            print("Who do you wish to talk to?")
            target = GetChoice(persons)
            print()
            if (target != 0):
                talk(globals()[persons[target-1]])
    else:
        if (person.isPerson):
            person.talk()

#this is the answer, go liberate everyone O Explorer!
def liberate(target):
    """COMMAND: LIBERATE
    For liberating persons that no longer have woes in the world.
    Enter "liberate(<name>)" to liberate a person.
    """
    UpdateState()
    importlib.reload(State)
    if (target.isPerson):
        if(State.CanLiberate()):
            for line in target.lastWords.split('\n'):
                finalWords = ""
                for c in line:
                        finalWords+=chr((ord(c)-42)%95+32)
                Say(target.__name__,finalWords)

            Update(State.__file__, target.__name__ + "_liberated","True")
            os.remove(target.__file__)
            importlib.reload(State)

            if(State.allLiberated()):
                Wait(5)
                Pause()
                print("!!!!!!GAME OVER!!!!!!!\N")
                for line in GameOverMsg.split('\n'):
                    finalWords = ""
                    for c in line:
                            finalWords+=chr((ord(c)-42)%95+32)
                    Say("Developers",finalWords)
        else:
            print("\nIt seems there is still unease in the world, and you are unable to liberate the "+ target.__name__+".\n")
    else:
        print("\n"+target.__name__+" is not a person and cannot be liberated.\n")


GameOverMsg ="""\
Q|oo~sxq}*zvk$o|6*"o*k|o*~ro*o!sv*m|ok~y|}*~rk~*~ro*z|yzro~*}zyuo*yp8*Qyyn*tyl*yx*,vslo|k~sxq,*o!o|$yxo*7*$y *lk}smkvv$*t }~*novo~on*~ros|*psvo}8*cy *nsnx1~*xoon*~y*}yv!o*kx$*n wl*z %%vo*~y*novo~o*psvo}8*L ~*$y *nsn8*Ryzo*~rk~*~swo*"k}*"ovv*}zox~6*kxn*$y *poov*lo~~o|*kly ~*$y |}ovp*xy"8*D3
Xy"*~ro*qkwo*rk}*oxnon6*s~1}*t }~*$y *kxn*~ro*"y|vn*vop~*~y*o#zvy|o8*Yp*my |}o6*$y *mkx*}~k|~*k*xo"*qkwo*kxn*~|$*~y*}yv!o*~ro*z %%vo}*sx*k*nsppo|ox~*"k$8*O!o|$yxo*"svv*lo*lkmu*kqksx6*kxn*~ro$*mkx*loq*$y *kxn*~rkxu*$y *kvv*y!o|*kqksx+*cy 1vv*lo*} |o*~y*poov*o!ox*lo~~o|*kly ~*$y |}ovp8*E3\
"""
