class ResourceManager:
    "handles stuff"
    def checker(processID):
        if processID == "1.7 process ID":
            17Organizer()
        elif processID == "1.10 process ID":
            110Organizer()

    def 1.7Organizer():
        #run each sub-category of of packs twice, one to move the other versions packs into their folders,
        #the other time to move the current versions packs out of their folders
        #This packs the other versions folders up
        red()
        blue()
        green()
        purple()
        defaultedits()
        #This unpacks the current versions folders up
        red()
        blue()
        green()
        purple()
        defaultedits()

    def 1.10Organizer():
        #run each sub-category of of packs twice, one to move the other versions packs into their folders,
        #the other time to move the current versions packs out of their folders
        #This packs the other versions folders up
        red()
        blue()
        green()
        purple()
        defaultedits()
        #This unpacks the current versions folders up
        red()
        blue()
        green()
        purple()
        defaultedits()

    def red("PATH to resourcepacks/MCVERSION/RED", mcversion, mode="default"):
        #remove the first paramater, not needed just a filler
        "Moves red packs to the specificed mcversion folder, or unpacks them into the base folder"
        if mode == "default":
            #default mode will bring packs out of folders
        elif mode == "repack":
            #repack mode will put them back in folders
    
    def blue("PATH to resourcepacks/MCVERSION/BLUE", mcversion, mode="default"):
        #remove the first paramater, not needed just a filler
        
        "Moves blue packs to the specificed mcversion folder, or unpacks them into the base folder"
    def green("PATH to resourcepacks/MCVERSION/GREEN", mcversion, mode="default"):
        #remove the first paramater, not needed just a filler
        "Moves green packs to the specificed mcversion folder, or unpacks them into the base folder"
    
    def purple("PATH to resourcepacks/MCVERSION/PURPLE", mcversion, mode="default"):
        #remove the first paramater, not needed just a filler
        "Moves purple packs to the specificed mcversion folder, or unpacks them into the base folder"
    
    def defaultedits("PATH to resourcepacks/MCVERSION/DEFAULTEDITS", mcversion, mode="default"):
        #remove the first paramater, not needed just a filler
        "Moves defaultedit packs to the specificed mcversion folder, or unpacks them into the base folder"