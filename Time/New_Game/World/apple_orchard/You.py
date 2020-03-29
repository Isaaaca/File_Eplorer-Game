import inspect, os
import State
from Util import GetChoice, Say

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
    print()

def look(thing = ""):
    """COMMAND: LOOK
    For looking at obects, places or people.
    Enter "look()" to look at your surroundings.
    Enter "look(<name>)" to take a closer look at something.
    """
    UpdateState()
    print()
    if not thing:
        print('You are curently in ' + CurrentLocation.__name__ + '\n')
        print('The following things/people are here:')
        for interactable in interactables:
            print(interactable)
    else:
        print(inspect.getdoc(thing))
    print("\nEnter \"look(<name>)\" to take a closer look at something.")
    print()




def talk(person = ""):
    """COMMAND: TALK
    For talking to people.
    Enter "talk()" to view and select someone to talk to.
    Enter "talk(<name>)" to directly enter into coversation with the person.
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


def liberate(target):
    """COMMAND: LIBERATE
    For liberating persons that no longer have woes in the world.
    Enter "talk(<name>)" to liberate a person.
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
            os.remove(target.__file__)
        else:
            print("\nIt seems there is still unease in the world, and you are unable to liberate the "+ target.__name__+".\n")
    else:
        print("\n"+target.__name__+" is not a person and cannot be liberated.\n")
