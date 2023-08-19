import os
def stor(N,E,S,W,frsttime):
    if N == 0 and E == 0 and S==0 and W==0 and frsttime==0:

        frsttime=frsttime+1
    elif  N == 0 and E == 0 and S==0 and W==0 and frsttime ==1:
        os.system('clear')
        print("You are back to where you started\nTo the north there is a cracked station control screen, It seems you are in the station's MONITORING&CONTROL point\nTo the east there is a row of lockers\To the south is a locked reinforced door\nTo the west is the way to the armoury")

    if N == 1 and E == 0 and S==-1 and W==0:      #this works at this point i can move arond pick stuff up and move back i would just have to take ages writing the story and i don't feel like it
        os.system('clear')
        print("You walk over to the control screen.\n MOUNT EREBUS VOLCANIC STATION is at the top in large letters. There are huge red warning signs on the screen. \n EARTHQUAKE EMERGENCY \nThe panel has a map of the station, it seems many staition quarters have been catastrophically damaged.\nThe screen is frozen but there is a message in the corner from the station administrator.\nHOSTILES HAVE INFILTRATED\nYou pick up a pair of of keys on the panel.It says 'LOCKER3' on laminated card attached to the keyring\n.  ")
























