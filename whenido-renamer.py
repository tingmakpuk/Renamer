"""Renamer, Copyright 2014, Whenido, /u/tingmakpuk.  Open source license available.
This program was the first project of a complete novice, and the use of the program is at your own risk.

Current version 3.0: More eligantly avoids renaming this program file.  However, it can still rename other folders in the directory.
WIP v 4.0: Use __file__ to most eligantly skip?  Need to research identifying folders.  
"""
# *Config and warnings*
import os
import sys

#Better way to format?
print "This program is designed to rename tv shows in Plex format of 'Name - s01e01'.ext"
print "Please read directions and use only as instructed, or you may end up renaming files you do not want to rename."
print 
print "Plex prefers your files separated into seasons('Showname' folder -'Season #' folder -'Showname - s01e01.ext')."
print "This program is designed to work with one season at a time; please separate your episodes into seasons per plex protocol."
print "Put this program into a season folder and restart.  Files will be taken alphabetically, and rename them, per your naming instructions."
print
print


# *Get name, season and verification*
name_loop = True
while name_loop == True:  
    name = str(raw_input("Enter the show name the way you want it listed: ")) #Retry once if left blank, but defaults to generic if left blank twice.
    if name == "":
        print "That wouldn't be too smart.  Please try again."
        name = str(raw_input("Enter the show name the way you want it listed: ") or "Herp Derp")
        if name == "Herp Derp":
            print "Well, can't say I didn't try."
    season = int(raw_input("Which season: ") or 1) #Defaults to season 1 if left blank. Crashes if str.
    episode = 0
    print
    print "All the files in this directory will be relabeled as follows:"
    for filename in os.listdir("."):
        #v3.0 has been fixed; previous versions will break at Whenido;
        #Still room for formal fix of checking for folders (?) and using __file__ (?) instead of Whenido
        if filename.startswith("Whenido") == False:  
            print
            print filename
            filename_ext = filename[-3:]
            episode += 1
            newfile = str("{} - S{:02d}E{:02d}.{}".format(name, season, episode, filename_ext))
            print "Will be renamed as %s " % (newfile)
            print
            os.rename(filename, newfile)

        elif filename.startswith("Whenido"):  
            print
            print "Skipping %s." % (filename)
            continue
        
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    yesno_loop = True
    while yesno_loop:
        print
        sys.stdout.write("Type no to cancel; yes to rename all files: ")
        choice = raw_input().lower()
        if choice in valid:
            if valid[choice] == True:
                name_loop = False
                yesno_loop = False
            elif valid[choice] == False:
                name_loop = True
                print
                print "Canceled.  Restarting..."
                break
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

# *Process files*
#Rerunning the newfile is inefficient, but it has to be recalculated for each file, so no way around?  
episode = 0
for filename in os.listdir("."):
    #v3.0 has been fixed; previous versions will break at Whenido;
    #Still room for formal fix of checking for folders (?) and using __file__ (?) instead of Whenido
    if filename.startswith("Whenido") == False:
        print
        print filename
        filename_ext = filename[-3:]
        episode += 1
        newfile = str("{} - S{:02d}E{:02d}.{}".format(name, season, episode, filename_ext))
        print "Renamed as %s " % (newfile)
        print
        os.rename(filename, newfile)

    elif filename.startswith("Whenido"):  #for lack of a better way, keep program named Whenido to skip
        print
        print "Skipped %s." % (filename)
        continue
