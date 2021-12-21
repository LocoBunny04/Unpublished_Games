from lead_game import rP, trtl, wn



#import functions

wn_msg = trtl.textinput('Directions','Press "Go" to start\nabrupt stop = DOWN\nspeed bump = Return\n right = RIGHT\n left = LEFT\n go =UP\nEnter your NAME to record score')

def rst_trace():
    if rP == True:
        name = str(wn_msg)
        name += '\n'
        print("press")
        print(rP)

    f = open("Leaderboard.txt","a") #'password' always have to be a str
    f.write(name) #checks to see if code is a completed string consisting of letters and numbers
    f.close()




#st_trace()
wn.bgpic('prgm_image/runbts.gif')



