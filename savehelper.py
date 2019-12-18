import configparser,json,inspect
config = configparser.ConfigParser()

name = ""

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def loadcreatesave(text,choice,default):
    global name
    if choice == "l":
        name = text
        name = name+".txt"
        print("loaded")
        config.read(name)
        print("loaded save")
    elif choice == "n":
        name = text
        name = name+".txt"
        config["save"] = default
        with open(name, 'w') as configfile: config.write(configfile)

def loadvar(var):
    save = config["save"]
    loadvar = save[var]
    return loadvar
    
def loadlist(listname):
    list1 = config.get("save",listname)
    list1 = list1.replace("[","")
    list1 = list1.replace("]","")
    list1 = list1.replace("'","")
    li = list(list1.split(", "))
    return li

def save(input,nam):
    save = config["save"]
    save[str(nam)] = str(input)

def saveall():
    global name
    with open(name, 'w') as configfile: config.write(configfile)