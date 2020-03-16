import os, sys
import importlib

print("===========================================")
print("===============FILE EXPLORER===============")
print("===========================================")
print("This game is played via commands. Enter \"help()\" to get started.")


path = ""
root = os.getcwd()
gamestate = {}
CurrentLocation = None
interactables = []
sys.path.append(os.path.join(root, "Laws"))



def UpdateState():
    global path, gamestate, CurrentLocation
    newstate ={}
    for currPath, folders, files in os.walk(root):
        filestates=[]
        for file in files:
            filestates.append((file, os.stat(os.path.join(currPath, file)).st_mtime))
            if file == 'You.py':
                path = (os.path.join(currPath, file))
        newstate[currPath]=folders,filestates

    if(gamestate != newstate):
        gamestate = newstate
        cwd = os.getcwd()
        if (cwd !=root):
            sys.path.remove(cwd)
        os.chdir(os.path.dirname(path))
        sys.path.append(os.getcwd())
        del CurrentLocation
        if sys.platform == "win32":
            location = os.path.relpath(os.path.dirname(path),root).replace('\\','.')
        else:
            location = os.path.relpath(os.path.dirname(path),root).replace('/','.')
        CurrentLocation = importlib.import_module(location)


        while interactables:
            itemx = interactables.pop()
            del globals()[itemx]

        for itemx in os.listdir():
            print
            if itemx != '__init__.py' and itemx != '__pycache__' and itemx != 'You.py':
                name = os.path.splitext(itemx)[0]
                globals()[name] = importlib.import_module(name)
                importlib.reload(globals()[name])
                interactables.append(name)



UpdateState()


exec(open(path).read())
