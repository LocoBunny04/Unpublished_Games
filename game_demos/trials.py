from PIL import Image, ImageTk
import random as rand
import turtle as trtl
# import required module
from playsound import playsound
import tkinter.messagebox
from pynput.keyboard import Key, Listener
import glob
#import prgm_image
# prgm_image_list = []
# for filename in glob.glob('/Users/khaase/Desktop/VroomFold/prgm_gif/'): #assuming gif
#     im=prgm_image.open(filename)
#     prgm_image_list.append(im)
wn = trtl.Screen()
#si = tk.Tk()
si = trtl.Turtle()
caller = trtl.Turtle()
st = trtl.Turtle()
rSt = trtl.Turtle()
user = trtl.Turtle()
point = trtl.Turtle()
atmpt = trtl.Turtle()

frac = trtl.Turtle()
#score = trtl.Turtle()
count = 0
rP = False #count for times restart btn is pressed
alpha = False
digit = False
caller_list = ['abrupt stop', 'speed bump','right','left','go']
caller_txt = []
#Message ="Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP"

#tkinter.messagebox.showinfo('Directions','Press "Go" to start\nabrupt stop = DOWN\nspeed bump = Return\n right = RIGHT\n left = LEFT\n go =UP\n')
#playsound('vvvcopy.wav', False)
attempt = 0
frac.ht()
atmpt.ht()
user_txt = ''
lead = ''


#wn = tk.Tk()
#wn.screensize("400x400")
# --- Window Creator ---
wn.title("Vroom Vroom: BTS EditionT")
#wn.window_height(150)
wn.setup(height=500,width=500)
wn.bgpic('prgm_image/runbtsback.gif')
wn_msg = trtl.textinput('Directions','Press "Go" to start\nabrupt stop = DOWN\nspeed bump = Return\n right = RIGHT\n left = LEFT\n go =UP\nEnter your Name for Leaderboard')
for m in wn_msg:
    if m.isalpha():
        alpha = True
    if m.isdigit():
        digit = True
if wn_msg.isdigit():
    wn_msg = trtl.textinput('Directions','Press "Go" to start\nabrupt stop = DOWN\nspeed bump = Return\n right = RIGHT\n left = LEFT\n go =UP\nEnter your Name for Leaderboard')

msg_input = str(wn_msg)

#while wn_msg != wn_msg.isalpha() == False:
    #wn_msg = trtl.textinput('Directions','Press "Go" to start\nabrupt stop = DOWN\nspeed bump = Return\n right = RIGHT\n left = LEFT\n go =UP\nEnter your Name for Leaderboard')
while wn_msg != msg_input:
    wn_msg = trtl.textinput('Directions','Press "Go" to start\nabrupt stop = DOWN\nspeed bump = Return\n right = RIGHT\n left = LEFT\n go =UP\nEnter your Name for Leaderboard')


#caller_img ="huh_resize.gif"
#user_label = Label(wn,prgm_image=caller_img)

# ---prgm_images ---
as_img = 'prgm_image/as_resize.gif'
wn.addshape(as_img)
sb_img = "prgm_image/vSb_resize_tsp.gif"
wn.addshape(sb_img)
r_img = "prgm_image/right_resize.gif"
wn.addshape(r_img)
l_img = "prgm_image/vL_resize_tsp.gif"
wn.addshape(l_img)
go_img = "prgm_image/go_resize.gif"
wn.addshape(go_img)
caller_img = "prgm_image/huh_resize.gif"
wn.addshape(caller_img)
restart_pic = "prgm_image/restart_resize_tsp.gif"
wn.addshape(restart_pic)
start_pic = "prgm_image/st_resized.gif"
wn.addshape(start_pic)
user_pic = "prgm_image/plyr_resize_tsp.gif"
wn.addshape(user_pic)

point.ht()
#caller.ht()
# --- Functions ---
x = -191
y = 180
caller.pu()
caller.goto(x,y)
si.pu()
si.ht()
si.goto(-120,150)

rSt.shape(restart_pic)
rSt.pu()
rSt.goto(0,180)
rSt.ht()

st.shape(start_pic)
st.pu()
st.goto(0,180)


user.shape(user_pic)
user.pu()
user.goto(0,-50)

point.pu(); point.goto(145,176);atmpt.pu();atmpt.goto(160,160);frac.pu();frac.goto(165,188); frac.pd();frac.goto(150,168)

def startPress(x, y):
    global attempt, count
    global rP
    point.clear()
    caller.shape(caller_img);user.shape(user_pic)
    #caller.st()
    st.ht()
    rSt.st()
    #print('playing sound using native player')
    #playsound('vvvcopy.wav')
    attempt = 0
    count = 0
    wn.delay(100)
    si.clear()
    rP = False
    # callerChoose()
    gameMain()
    
    # callerSoundOs()

def rStPress(x, y):
    global point 
    global count
    global attempt, rP, wn_msg, user
    #print("restart cliicked")
    caller.shape(caller_img)
    rP =  True
    rSt.ht()
    rst_trace(rP)
    # st.st()
    si.clear();point.clear();atmpt.clear()
    #attempt = 0; count = 0
    user.shape(user_pic)
    wn_msg = ''
    wn_msg = trtl.textinput('Leaderboard','Enter your Name to add to the Leaderboard')
    si.clear()
    wn.delay(500)
    # while rP == True:
    #     break
    # if rP == False: 
    #     print("end")
    gameMain()
    # callerChoose()
    st.ht()
    rSt.st()

#    gameMain()
def callerChoose():
    global point
    global caller_txt
    si.ht()
    
    caller_txt = rand.choice(caller_list)
    si.write(caller_txt,font=("Arial",15))
    print(caller_txt)
    callerSoundOs()
    wn.delay(10)
    playsound('audio/vvvSoftfade.wav', False)
    wn.delay(100)
    whilePoint()
    point.clear()
    point.ht()
    print ('point: ', count)
    #wn.delay(10)
    #si.ht()

def usL():
    global user_txt
    user_txt = 'left'
    user.shape(l_img)
def usR():
    global user_txt
    user_txt = 'right'
    user.shape(r_img)
def usAS():
    global user_txt
    user_txt = 'abrupt stop'
    user.shape(as_img)
def usSB():
    global user_txt
    user_txt = 'speed bump'
    user.shape(sb_img)
def usGo():
    global user_txt
    user_txt = 'go'
    user.shape(go_img)

def callerSoundOs():
    global caller_txt
    #print("cSOs")
    #caller_pic = "huh_resize.gif"
    if caller_txt == caller_list[0]:
        #print("ab")
        cAs(),playsound('audio/vDa_ASSoft.wav')
        
    elif caller_txt == caller_list[1]:
        #print("sb")
        cSb(),playsound('audio/vS_sbsoft.wav')
        
    elif caller_txt == caller_list[2]:
        #print("r")
        cR(),playsound('audio/vRsoft.wav')
        
    elif caller_txt == caller_list[3]:
        #print("l")
        cL(),playsound('audio/vLsoft.wav')
        #vroomVroom_wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[4]:
        #print("g")
        cGo(),playsound('audio/vUp_goSoft.wav')

#user change
def abruptStop():
    global user_txt
    user.shape(as_img)
    print('user',user_txt)
    usAS()

def speedBump():
    global user_txt
    user.shape(sb_img)
    print('user',user_txt)
    usSB()

def rightTurn():
    global user_txt
    user.shape(r_img)
    print('user',user_txt)
    usR() 

def leftTurn():
    global user_txt
    user.shape(l_img)
    print('user',user_txt)
    usL()

def goFD():
    global user_txt
    user.shape(go_img)
    print('user',user_txt)
    usGo()

#caller change
def cAs():
    caller.shape(as_img)
    print('caller',caller_txt)

def cSb():
    caller.shape(sb_img)
    print('caller',caller_txt)

def cR():
    caller.shape(r_img)
    print('caller',caller_txt)

def cL():
    caller.shape(l_img)
    print('caller',caller_txt)

def cGo():
    caller.shape(go_img)
    print('caller',caller_txt)

def whilePoint():
    global count, attempt
    global  user_txt, caller_txt
    # wn.delay(200)
    # print(user_txt,"wP")
    # print(caller_txt,"wP")
    point.ht()
    if user_txt == caller_txt:
        wn.delay(150)
        attempt += 1
        count = int(count)
        count += 1
        point.clear(); atmpt.clear()
        atmpt.write(str(attempt),font=("Arial",15)),point.write(str(count),font=("Arial",15))
        wn.delay(50)
        user.shape(user_pic)
    else:
        wn.delay(150)
        attempt += 1
        count = int(count)
        count -= 1
        ah = str(count)
        point.clear(); atmpt.clear()
        atmpt.write(str(attempt),font=("Arial",15)),point.write(ah,font=("Arial",15))
        wn.delay(50)
        user.shape(user_pic)
    #atmpt.clear()
   #attempt +=1;#atmpt.write(str(attempt),font=("Arial",15))
    #print('attempt',attempt)
    si.clear()
    point.ht()
    gameMain()
    
def rst_trace(rP):
    global lead, count, attempt
    if rP:
        name = wn_msg
        name += ' '
        #print("rst_btn pressed")
        print(rP)
        count = str(count)
        attempt = str(attempt)
        lead = name + str( '' + count + '/'  + attempt + '\n')
        print(lead)
    f = open("Leaderboard.txt","a") #'password' always have to be a str
    f.write(lead) #checks to see if code is a completed string consisting of letters and numbers
    f.close()
    count = 0
    attempt = 0
    gameMain()
    rSt.st()
    # wn.onkeypress(rightTurn,'Right')
    # wn.onkeypress(leftTurn,'Left')
    # wn.onkeypress(goFD,'Up')
    # wn.onkeypress(abruptStop,'Down')
    # rP = False

def gameMain():
    global count, attempt
    caller.shape(caller_img);user.shape(user_pic)
    # caller.st()
    si.ht()
    wn.onkeypress(rightTurn,'Right')
    wn.onkeypress(leftTurn,'Left')
    wn.onkeypress(goFD,'Up')
    wn.onkeypress(abruptStop,'Down')
    #point.st()
    #caller.shapesize(10)
    # for t in attempt:
    if attempt < 100:
        wn.delay(200)
        point.ht()
        callerChoose()
        point.clear()
        atmpt.clear()
    else:
        print("You've reached 100 attempts: ")
        exit()
            # break
        # count = 0
        # attempt = 0
        # user.shape(user_pic)
        # caller.shape(caller_img)
        # point.clear()
        # atmpt.clear()
        # wn.delay(200)
        # callerChoose()
        
# gameMain()
st.onclick(startPress)
rSt.onclick(rStPress)

wn.onkeypress(speedBump,'Return')
#wn.onkeypress(gameMain,'BackSpace')

wn.listen()
wn.mainloop()