import inspect, os

def poo(command = ""):
    """COMMAND: HELP
    For learning how to use commands.
    Enter "help()" to see your available commands.
    Enter "help(<command_name>)" to learn more about a command.
    """
    UpdateState()
    if (command):
        if(callable(command)):
            print(inspect.getdoc(command))
        else:
            print(command.__name__ + " is not a command. Enter \"help()\" to see a list of available commands")
    else:
        print("Available Commands:")
        print("\"look()\"")
        print("\"talk(<target>)\"")
        print("\"help()\"")
        print("\nEnter \"help(<command_name>)\" to learn more about a command.")
        print("E.g. \"help(look)\",\"help(talk)\"")

def look(thing = ""):
    """COMMAND: LOOK
    For looking at obects, places or people.
    Enter "look()" to look at your surroundings.
    Enter "look(<name>)" to take a closer look at something.
    """
    UpdateState()
    if not thing:
        print('You are curently in ' + CurrentLocation.__name__)
        for interactable in interactables:
            print(interactable)
    else:
        print(inspect.getdoc(thing))




def talk(person = ""):
    """COMMAND: TALK
    For talking to people.
    Enter "look(<name>)" to enter into coversation with the person.
    """
    UpdateState()
    if not person:
        print("A name is required for this command.")
    else:
        if (person.isPerson):
            print()
            person.talk()
