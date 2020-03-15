import os, sys, subprocess, textwrap

def Show(filename):
    path = os.path.join(os.path.dirname(__file__), "Images", filename)
    if sys.platform == "win32":
        os.startfile(path)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, path])

def Say(text):

    text = textwrap.fill(text)
    text = textwrap.indent(text, ' # ', lambda line: True)
    print(text)
    print(' # ')

def Ask(options):
    wrapper = textwrap.TextWrapper()
    wrapper.initial_indent = ' > '
    wrapper.subsequent_indent = '   '

    counter = 1
    for option in options:
        text = str(counter)+'. '+option
        text = wrapper.fill(text)
        print(text+'\n')
        counter+=1

    choice = input("Enter Your choice: ")
    validChoice = choice.isnumeric() and int(choice)<counter
    while (not validChoice):
        if (not choice.isnumeric()):
            choice = input("Please enter a number: ")
        elif (not int(choice)<counter):
            choice = input("Please enter a number from 1~"+ str(counter-1)+": ")
        validChoice = choice.isnumeric() and int(choice)<counter
    return choice
