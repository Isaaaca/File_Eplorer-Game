quest1given = False
quest1complete = False
quest2given = False
quest2complete = False
quest3given = False
quest3complete = False
quest4given = False
quest4complete = False
quest5given = False
quest5complete = False
quest6given = False
quest6complete = False

def CanLiberate():
    for att in globals():
        if ("complete" in att) and (globals()[att]== False):
            return False
    return True
