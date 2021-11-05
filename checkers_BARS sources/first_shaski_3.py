from tkinter import *
from random import * # x0 = randint(0, 100)
import time
from time import sleep
from time import time
Time = int(time()*1000)
ras = 50

# 9  - нельзя занимать - белая
# 0  - свободная черная клетка
# 1  - белая шашка
# 11 - белая дамка
# 2  - черная шашка
# 12 - черная дамка
area = [[9, 2, 9, 2, 9, 2, 9, 2],
        [2, 9, 2, 9, 2, 9, 2, 9],
        [9, 2, 9, 2, 9, 2, 9, 2],
        [0, 9, 0, 9, 0, 9, 0, 9],
        [9, 0, 9, 0, 9, 0, 9, 0],
        [1, 9, 1, 9, 1, 9, 1, 9],
        [9, 1, 9, 1, 9, 1, 9, 1],
        [1, 9, 1, 9, 1, 9, 1, 9]]

area2 = [[9, 2, 9, 2, 9, 2, 9, 2],
        [2, 9, 2, 9, 2, 9, 2, 9],
        [9, 0, 9, 0, 9, 0, 9, 0],
        [0, 9, 0, 9, 0, 9, 0, 9],
        [9, 0, 9, 0, 9, 0, 9, 0],
        [0, 9, 0, 9, 0, 9, 0, 9],
        [9, 1, 9, 1, 9, 1, 9, 0],
        [1, 9, 1, 9, 1, 9, 2, 9]]

area1 = [[9, 0, 9, 0, 9, 0, 9, 0],
        [0, 9, 0, 9, 2, 9, 0, 9],
        [9, 2, 9, 0, 9, 0, 9, 0],
        [0, 9, 0, 9, 2, 9, 2, 9],
        [9, 0, 9, 0, 9, 2, 9, 0],
        [0, 9, 0, 9, 0, 9, 0, 9],
        [9, 0, 9, 1, 9, 0, 9, 0],
        [0, 9, 0, 9, 0, 9, 0, 9]]


klik = [[-1,-1],
        [-1,-1]]

click_flag = 0
go_color = 1

#print(area[-1][-1])

def qwerty():
    global area
    global klik
    global go_color
    
    out_window = Tk()
    out_window.title('OUTPUT')
    #window.geometry('900x900')
    canvas = Canvas(out_window,width=9*ras,height=9*ras,bg="grey") # ,cursor="pencil"

    in_window = Tk()
    in_window.title('INPUT')
    in_window.geometry('400x250')

    #===================================================================================================================================================================================================

    def clicked():
        #res = "Привет {}".format(txt.get())
        #lbl.configure(text=res)
        print(txt.get())

    lbl = Label(in_window, text="Привет")  
    lbl.grid(column=0, row=0)  
    txt = Entry(in_window,width=10)  
    txt.grid(column=1, row=0)  
    btn = Button(in_window, text="Не нажимать!", command=clicked)  
    btn.grid(column=2, row=0) 

    #===================================================================================================================================================================================================
    def map(x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min);

    def millis():
        return int(time()*1000);

    def cut(i, a):
        if (abs(i) > a):
            i = abs(i)/i*a;
            i = int(i);
        return i;

    def znak(a):
        if   (a > 0):
            return  1
        elif (a < 0):
            return -1
        else:
            return  0
    
    def reboot_checkers():
        global area
        global klik
        global go_color
        x = 0 # shaska => damka
        while (x <= 7):
            if (area[0][x] == 1):
                area[0][x] = area[0][x] + 10
            x = x + 1
        x = 0
        while (x <= 7):
            if (area[7][x] == 2):
                area[7][x] = area[7][x] + 10
            x = x + 1
        x = 0
        y = 0
        # make area
        #canvas.create_line(0,0,600,600,width=5,fill="yellow")
        while (y < 8):
            x = 0
            while (x < 8):
                canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="white",outline="white")
                if ((klik[0][0] == x) and (klik[0][1] == y+1) and (klik[1][0] == -1) and (klik[1][1] == -1)):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="red",outline="red")
                elif (go_color == area[y+1][x]%10):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="black",outline="red")
                else:
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="black",outline="black")
                x = x + 1
                if ((klik[0][0] == x) and (klik[0][1] == y) and (klik[1][0] == -1) and (klik[1][1] == -1)):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="red",outline="red")
                elif (go_color == area[y][x]%10):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="black",outline="red")
                else:
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="black",outline="black")
                canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="white",outline="white")
                x = x + 1
            y = y + 2
        #canvas.create_text(ras/4+0*ras,ras/4+1*ras,text="A",font="Verdana 12",justify=CENTER,fill="black")
            
        # make checkers
        x = 0
        y = 0
        while (y < 8):
            x = 0
            while (x < 8): 
                if ((area[y][x] != 9) and (area[y][x] != 0)):
                    if (area[y][x]%10 == 1):
                        canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white")
                    else:
                        canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="grey")
                    if (area[y][x]/10 >= 1):
                        canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="red")
                        #canvas.create_oval([x*ras+ras/2+ras/3,(y-1)*ras+ras/2*3+ras/3],[x*ras+ras/2*3-ras/3,(y-1)*ras+ras/2*5-ras/3],fill="red")
                x = x + 1
            y = y + 1

    def can_i_eat(y,x):
        if (1):
            if (1):
                eat = 0
                if (area[y][x]!=9): # proverka na vozmognost siest shaskami
                    if (y-2>=0 and x-2>=0):
                        if (area[y][x]%10!=area[y-1][x-1]%10 and area[y][x]!=0 and area[y-1][x-1]!=0 and area[y-2][x-2]==0 and area[y][x]%10==go_color):
                            eat = 1
                    if (y+2<=7 and x-2>=0):
                        if (area[y][x]%10!=area[y+1][x-1]%10 and area[y][x]!=0 and area[y+1][x-1]!=0 and area[y+2][x-2]==0 and area[y][x]%10==go_color):
                            eat = 1
                    if (y-2>=0 and x+2<=7):
                        if (area[y][x]%10!=area[y-1][x+1]%10 and area[y][x]!=0 and area[y-1][x+1]!=0 and area[y-2][x+2]==0 and area[y][x]%10==go_color):
                            eat = 1
                    if (y+2<=7 and x+2<=7):
                        if (area[y][x]%10!=area[y+1][x+1]%10 and area[y][x]!=0 and area[y+1][x+1]!=0 and area[y+2][x+2]==0 and area[y][x]%10==go_color):
                            eat = 1
                if (area[y][x]/10>1 and area[y][x]%10==go_color): # proverka na vozmognost siest damkami 
                    xd1 = x
                    xd2 = x
                    xd3 = x
                    xd4 = x
                    yd1 = y
                    yd2 = y
                    yd3 = y
                    yd4 = y
                    i = 0
                    while (i < 10):
                        if (yd1>0 and xd1>0 and area[yd1-1][xd1-1]==0):
                            yd1 = yd1 - 1
                            xd1 = xd1 - 1
                        if (yd2<7 and xd2>0 and area[yd2+1][xd2-1]==0):
                            yd2 = yd2 + 1
                            xd2 = xd2 - 1
                        if (yd3>0 and xd3<7 and area[yd3-1][xd3+1]==0):
                            yd3 = yd3 - 1
                            xd3 = xd3 + 1
                        if (yd4<7 and xd4<7 and area[yd4+1][xd4+1]==0):
                            yd4 = yd4 + 1
                            xd4 = xd4 + 1
                        i = i + 1
                    if (yd1-2>=0 and xd1-2>=0):
                        if (go_color!=area[yd1-1][xd1-1]%10 and area[yd1-1][xd1-1]!=0 and area[yd1-2][xd1-2]==0):
                            eat = 1
                            yd1 = yd1 - 2
                            xd1 = xd1 - 2
                    if (yd2+2<=7 and xd2-2>=0):
                        if (go_color!=area[yd2+1][xd2-1]%10 and area[yd2+1][xd2-1]!=0 and area[yd2+2][xd2-2]==0):
                            eat = 1
                            yd2 = yd2 + 2
                            xd2 = xd2 - 2
                    if (yd3-2>=0 and xd3+2<=7):
                        if (go_color!=area[yd3-1][xd3+1]%10 and area[yd3-1][xd3+1]!=0 and area[yd3-2][xd3+2]==0):
                            eat = 1
                            yd3 = yd3 - 2
                            xd3 = xd3 + 2
                    if (yd4+2<=7 and xd4+2<=7):
                        if (go_color!=area[yd4+1][xd4+1]%10 and area[yd4+1][xd4+1]!=0 and area[yd4+2][xd4+2]==0):
                            eat = 1
                            yd4 = yd4 + 2
                            xd4 = xd4 + 2
                return eat

    def go_controll():
        global area
        global klik
        global go_color
        x0 = klik[0][0]
        y0 = klik[0][1]
        x1 = klik[1][0]
        y1 = klik[1][1]
        flag = 0
        eat = 0
        color = area[x0][y0]%10
        if ((area[y0][x0] > 0) and (area[y0][x0] != 9) and (area[y1][x1] == 0)):
            x = 0
            y = 0
            while (y <= 7): 
                if (area[y][x]!=9 and flag == 0): # proverka na vozmognost siest shaskami
                    if (y-2>=0 and x-2>=0 and flag == 0):
                        if (area[y][x]%10!=area[y-1][x-1]%10 and area[y][x]!=0 and area[y-1][x-1]!=0 and area[y-2][x-2]==0 and area[y][x]%10==go_color):
                            eat = 1
                            if (y0-2==y1 and x0-2==x1 and y==y0 and x==x0):
                                flag = 1
                    if (y+2<=7 and x-2>=0 and flag == 0):
                        if (area[y][x]%10!=area[y+1][x-1]%10 and area[y][x]!=0 and area[y+1][x-1]!=0 and area[y+2][x-2]==0 and area[y][x]%10==go_color):
                            eat = 1
                            if (y0+2==y1 and x0-2==x1 and y==y0 and x==x0):
                                flag = 1
                    if (y-2>=0 and x+2<=7 and flag == 0):
                        if (area[y][x]%10!=area[y-1][x+1]%10 and area[y][x]!=0 and area[y-1][x+1]!=0 and area[y-2][x+2]==0 and area[y][x]%10==go_color):
                            eat = 1
                            if (y0-2==y1 and x0+2==x1 and y==y0 and x==x0):
                                flag = 1
                    if (y+2<=7 and x+2<=7 and flag == 0):
                        if (area[y][x]%10!=area[y+1][x+1]%10 and area[y][x]!=0 and area[y+1][x+1]!=0 and area[y+2][x+2]==0 and area[y][x]%10==go_color):
                            eat = 1
                            if (y0+2==y1 and x0+2==x1 and y==y0 and x==x0):
                                flag = 1
                if (area[y][x]/10>1 and area[y][x]%10==go_color and flag == 0): # proverka na vozmognost siest damkami 
                    xd1 = x
                    xd2 = x
                    xd3 = x
                    xd4 = x
                    yd1 = y
                    yd2 = y
                    yd3 = y
                    yd4 = y
                    i = 0
                    while (i < 10):
                        if (yd1>0 and xd1>0 and area[yd1-1][xd1-1]==0):
                            yd1 = yd1 - 1
                            xd1 = xd1 - 1
                        if (yd2<7 and xd2>0 and area[yd2+1][xd2-1]==0):
                            yd2 = yd2 + 1
                            xd2 = xd2 - 1
                        if (yd3>0 and xd3<7 and area[yd3-1][xd3+1]==0):
                            yd3 = yd3 - 1
                            xd3 = xd3 + 1
                        if (yd4<7 and xd4<7 and area[yd4+1][xd4+1]==0):
                            yd4 = yd4 + 1
                            xd4 = xd4 + 1
                        i = i + 1
                    if (yd1-2>=0 and xd1-2>=0 and flag == 0):
                        if (go_color!=area[yd1-1][xd1-1]%10 and area[yd1-1][xd1-1]!=0 and area[yd1-2][xd1-2]==0):
                            eat = 1
                            yd1 = yd1 - 2
                            xd1 = xd1 - 2
                            if (y==y0 and x==x0):
                                i = 1
                                while (yd1>=0 and xd1>=0 and i==1):
                                    if (area[yd1][xd1]==0 and yd1==y1 and xd1==x1):
                                        flag = 1
                                    yd1 = yd1 - 1
                                    xd1 = xd1 - 1
                                    if (yd1>=0 and xd1>=0 and area[yd1][xd1]!=0):
                                        i = 0
                    if (yd2+2<=7 and xd2-2>=0 and flag == 0):
                        if (go_color!=area[yd2+1][xd2-1]%10 and area[yd2+1][xd2-1]!=0 and area[yd2+2][xd2-2]==0):
                            eat = 1
                            yd2 = yd2 + 2
                            xd2 = xd2 - 2
                            if (y==y0 and x==x0):
                                i = 1
                                while (yd2<=7 and xd2>=0 and i==1):
                                    if (area[yd2][xd2]==0 and yd2==y1 and xd2==x1):
                                        flag = 1
                                    yd2 = yd2 + 1
                                    xd2 = xd2 - 1
                                    if (yd2<=7 and xd2>=0 and area[yd2][xd2]!=0):
                                        i = 0
                    if (yd3-2>=0 and xd3+2<=7 and flag == 0):
                        if (go_color!=area[yd3-1][xd3+1]%10 and area[yd3-1][xd3+1]!=0 and area[yd3-2][xd3+2]==0):
                            eat = 1
                            yd3 = yd3 - 2
                            xd3 = xd3 + 2
                            if (y==y0 and x==x0):
                                i = 1
                                while (yd3>=0 and xd3<=7 and i==1):
                                    if (area[yd3][xd3]==0 and yd3==y1 and xd3==x1):
                                        flag = 1
                                    yd3 = yd3 - 1
                                    xd3 = xd3 + 1
                                    if (yd3>=0 and xd3<=7 and area[yd3][xd3]!=0):
                                        i = 0
                    if (yd4+2<=7 and xd4+2<=7 and flag == 0):
                        if (go_color!=area[yd4+1][xd4+1]%10 and area[yd4+1][xd4+1]!=0 and area[yd4+2][xd4+2]==0):
                            eat = 1
                            yd4 = yd4 + 2
                            xd4 = xd4 + 2
                            if (y==y0 and x==x0):
                                i = 1
                                while (yd4<=7 and xd4<=7 and i==1):
                                    if (area[yd4][xd4]==0 and yd4==y1 and xd4==x1):
                                        flag = 1
                                    yd4 = yd4 + 1
                                    xd4 = xd4 + 1
                                    if (yd4<=7 and xd4<=7 and area[yd4][xd4]!=0):
                                        i = 0
                    #===============================================
                x = x + 1
                if (x > 7):
                    x = 0
                    y = y + 1
            if (eat == 0):
                #flag = 1
                if (area[y0][x0]/10 < 1): # not queen
                    if   (area[y0][x0]%10==1 and y0-1==y1 and (x0==x1-1 or x0==x1+1)):
                        flag = 1
                    elif (area[y0][x0]%10==2 and y0+1==y1 and (x0==x1-1 or x0==x1+1)):
                        flag = 1
                    else:
                        print("you can not commit this move")
                else: # queen
                    if ((abs(x0-x1)==abs(y0-y1))): #  and abs(y0-y1)>=1)
                        flag = 1
                        x11 = x1
                        y11 = y1
                        while (x11!=x0):
                            if (area[y11][x11] != 0):
                                flag = 0
                            x11 = x11 - znak(x11-x0)
                            y11 = y11 - znak(y11-y0)
                        if (flag == 0):
                            print("you can not commit this move")
                    else:
                        print("you can not commit this move")
            elif (eat==1 and flag==0):
                print("you mast eat")
            elif (flag==0):
                print("you can not commit this move")
        else:
            print("you can not commit this move")
                
        return flag

    def eat_checkers():
        global area
        global klik
        x0 = klik[0][0]
        y0 = klik[0][1]
        x1 = klik[1][0]
        y1 = klik[1][1]
        c = 0
        if ((abs(x0-x1)==abs(y0-y1) and abs(y0-y1)>=2)): # eat
            while (x1!=x0):
                if (area[y0][x0] != 0):
                    c = 1
                area[y0][x0] = 0
                x0 = x0 + znak(x1-x0)
                y0 = y0 + znak(y1-y0)
        return c
    
    def no_wins():
        global area
        x = 0
        y = 0
        flag_b = 0
        flag_w = 0
        while (y<=7 and (flag_w==0 or flag_b==0)):
            if (area[y][x]%10==1):
                flag_w = 1
            if (area[y][x]%10==2):
                flag_b = 1
            if(x >= 7):
                x = 0
                y = y + 1
            else:
                x = x + 1
        flag = flag_b*flag_w
        if (flag == 0):
            if (flag_b==1):
                canvas.create_text(4.5*ras,4.5*ras,text="black wins!",font="Verdana 52",justify=CENTER,fill="blue")
            else:
                canvas.create_text(4.5*ras,4.5*ras,text="white wins!",font="Verdana 52",justify=CENTER,fill="blue")
        return flag


    def move():
        global area
        global klik
        global go_color
        #============================
        q = area[ klik[0][1] ][ klik[0][0] ]
        area[ klik[0][1] ][ klik[0][0] ] = 0
        area[ klik[1][1] ][ klik[1][0] ] = q
        #============================
        c = eat_checkers()
        xa = 0 # shaska => damka
        while (xa <= 7):
            if (area[0][xa] == 1):
                area[0][xa] = area[0][xa] + 10
            xa = xa + 1
        xa = 0
        while (xa <= 7):
            if (area[7][xa] == 2):
                area[7][xa] = area[7][xa] + 10
            xa = xa + 1
        if (can_i_eat( klik[1][1] , klik[1][0] ) and c==1):
            klik[0][0] = klik[1][0]
            klik[0][1] = klik[1][1]
            klik[1][0] = -1
            klik[1][1] = -1
        else:
            klik[0][0] = -1
            klik[0][1] = -1
            klik[1][0] = -1
            klik[1][1] = -1
            if (go_color == 1):
                go_color = 2
            else:
                go_color = 1
        reboot_checkers()
        no_wins()
    #===================================================================================================================================================================================================

    reboot_checkers()

    def mozg_random1():
        x = 1
        while (flag==1 and y>=0 and 0):
            if (area[y][x]%10==go_color and can_i_eat(y,x)):
                klik[0][0] = x
                klik[0][1] = y
                x = 0
                y = 7
                while (flag==1 and y>=0):
                    if (area[y][x]%10==go_color and can_i_eat(y,x)):
                        flag = 1
                        
                    if(x >= 7):
                        y = y - 1
                        x = 0
                    else:
                        x = x + 1
                flag = 0
            if(x >= 7):
                y = y - 1
                x = 0
            else:
                x = x + 1
    
    def mozg_random():
        global area
        global klik
        global go_color
        if (no_wins()):
            x = 0
            y = 7
            flag = 1
            print(go_color)
            while (flag==1):
                if (area[y][x]%10==go_color):
                    #print("--------------------")
                    y1 = randint(0, 7)
                    x1 = randint(0, 7)
                    while (area[y1][x1]!=0 or x==x1 and y==y1):
                        y1 = randint(0, 7)
                        x1 = randint(0, 7)
                    klik[0][0] = x
                    klik[0][1] = y
                    klik[1][0] = x1
                    klik[1][1] = y1
                    if (go_controll()):
                        flag = 0
                
                if(x >= 7):
                    x = 0
                    if(y <= 0):
                        y = 7
                    else:
                        y = y - 1
                else:
                    x = x + 1
            move()
            if(can_i_eat(klik[0][1],klik[0][0])):
                mozg_random()
        
    
    def click(event):
        global area
        global klik
        global go_color
        x = event.x
        y = event.y
        #print(x, y)
        if ((x >= ras/2) and (x <= ras/2*17) and (y >= ras/2) and (y <= ras/2*17)): 
            x = map(x, ras/2, ras/2*17, 0, 8)
            y = map(y, ras/2, ras/2*17, 0, 8)
            #print(x, y)
            if ((klik[0][0] == -1) and (area[y][x] != 9) and (area[y][x] != 0)):
                if (area[y][x]%10==go_color):
                    klik[0][0] = x
                    klik[0][1] = y
                    reboot_checkers()
                else:
                    print("now moved other color")
            elif ((klik[0][0] != -1) and (klik[0][0] == x) and (klik[0][1] == y)):
                klik[0][0] = -1
                klik[0][1] = -1
                reboot_checkers()
            elif ((klik[0][0] != -1) and (area[y][x] != 9) and (area[y][x] == 0)):
                klik[1][0] = x
                klik[1][1] = y 
                if (go_controll()):
                    c = go_color
                    move();                    
                    if (go_color != c):
                        #go_color = 2
                        mozg_random()
                        go_color = c
                else:
                    klik[1][0] = -1
                    klik[1][1] = -1
            else:
                print("ERROR")
        else:
            klik[0][0] = -1
            klik[0][1] = -1
            klik[1][0] = -1
            klik[1][1] = -1

        #reboot_checkers()
        #no_wins()
            
            
            
    canvas.bind("<Button-1>", click)

    if (Time + 2000 < millis()):
    #i = 2
    #if (i == '1'):
        #print(area[2][1])
        area[2][1] = 2
        area[1][2] = 0
        reboot_checkers()

    canvas.pack()
    out_window.mainloop()
    in_window.mainloop()

qwerty()
