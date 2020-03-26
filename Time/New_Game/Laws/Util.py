import os, sys, subprocess, textwrap, time

def Show(filename):
    path = os.path.join(os.path.dirname(__file__), "Images", filename)
    try:
        if sys.platform == "win32":
            os.startfile(path)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])
    except:
        print("Unable to open image in your current system. To see it manually go to: ")
        print(path)

def Say(name, text):

    print(name)
    text = textwrap.fill(text)
    text = textwrap.indent(text, ' | ', lambda line: True)
    print(text+'\n')

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

    choice = int(choice)
    reply = textwrap.fill(options[choice-1])
    reply = textwrap.indent(reply, ' * ', lambda line: True)
    print("\nYou")
    print(reply+'\n')

    return choice

def Pause():
    input("\nPress Enter to continue...")
    print()

def Search(item, location):

    items = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
    items = [os.path.splitext(f)[0] for f in items if (item in f)]
    return items

def Consume(item):
    os.remove(item)

def Update(item, attribute, value):
    f = open(item,'r+')
    contents = f.readlines()
    for i in range(len(contents)):
        line = contents[i]
        parts = line.split('=')
        if (len(parts) == 2):
            att = parts[0].replace(' ','')
            val = parts[1].replace(' ','')
            if (att == attribute):
                contents[i]= att+'='+value+'\n'
                break
    f.seek(0)
    f.truncate()
    f.writelines(contents)
    f.close()

def Wait(t):
    time.sleep(t)
