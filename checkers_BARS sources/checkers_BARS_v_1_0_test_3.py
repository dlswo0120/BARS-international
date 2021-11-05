from tkinter import *
from random import * # x0 = randint(0, 100)
from copy import deepcopy 
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

area_zero = [[9, 2, 9, 2, 9, 2, 9, 2],
             [2, 9, 2, 9, 2, 9, 2, 9],
             [9, 2, 9, 2, 9, 2, 9, 2],
             [0, 9, 0, 9, 0, 9, 0, 9],
             [9, 0, 9, 0, 9, 0, 9, 0],
             [1, 9, 1, 9, 1, 9, 1, 9],
             [9, 1, 9, 1, 9, 1, 9, 1],
             [1, 9, 1, 9, 1, 9, 1, 9]]

area_operation = []

area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                [2, 9, 2, 9, 2, 9, 2, 9],
                [9, 2, 9, 2, 9, 2, 9, 2],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [1, 9, 1, 9, 1, 9, 1, 9],
                [9, 1, 9, 1, 9, 1, 9, 1],
                [1, 9, 1, 9, 1, 9, 1, 9]]

area_monitor1 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [2, 9, 0, 9, 0, 9, 0, 9],
                [9, 1, 9, 0, 9, 0, 9, 0],
                [0, 9, 1, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 1],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor2 = [[9, 0, 9, 0, 9, 0, 9, 12],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 11],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor3 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 2, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 1, 9, 0, 0, 0, 9],
                [9, 0, 9, 1, 9, 1, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 1, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor4 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 2, 9, 2, 9, 2, 9, 2],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [1, 9, 1, 9, 1, 9, 1, 9],
                [9, 1, 9, 1, 9, 1, 9, 1],
                [1, 9, 1, 9, 1, 9, 1, 9]]

go = []
go_operation = []

#massive[1][0].clear()
#massive[1][0].append(5)
#massive[1][0].append(5)
#len(massive[0])
#mas = deepcopy(massive)

klik = [[-1,-1],
        [-1,-1]]

click_flag = 0
go_color = 1
people_color = 1 # 1- white, 2 - black, 3 - people vs people

#print(area[-1][-1])

count1 = 0
count2 = 0
count3 = 0

value = 0

control_move = 1
control_add = 1
control_edit = 0
control_vs = 3
go_error = 0

def qwerty():
    global area_monitor
    global klik
    global go_color
    global go
    global go_operation
    global count1
    global count2
    #global count3
    global control_move
    global control_add
    global control_edit
    global control_vs
    global go_error
    
    out_window = Tk()
    out_window.title('BARS field')
    #window.geometry('1000x1000')
    #canvas = Canvas(out_window,width=9*ras,height=9*ras)
    canvas = Canvas(out_window,width=9*ras,height=10*ras,bg="grey") # ,cursor="pencil"

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

    def coordinates_write(y0,x0,y1,x1):
        #massive[1][0].clear()
        #massive[1][0].append(5)
        #massive[1][0].append(5)
        #len(massive[0])
        #mas = deepcopy(massive)
        global go
        coo  = y0*10 + x0
        into = y1*10 + x1
        i = 0
        c = 0
        flag = 0
        while(len(go)<c and flag==0):
            if (go[c]==coo):
                flag = 1
            i = i + 1
        if (flag==0):
            go.append(coo)
        go[c] = into
        print(go)

    def reboot_controller():
        global go_color
        global control_move
        global control_add
        global control_edit
        global control_vs # за кого играет робот
        global go_error
        canvas.create_rectangle(0,ras*9,ras*9,ras*10,fill="grey")
        if (control_edit==0):
            canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="grey")
            if (control_vs==1 and go_color==2 or control_vs==2 and go_color==1 or control_vs==3):
                if (go_error==1):
                    canvas.create_text(ras*6.75,ras*9.5,text="you must eat",font="Verdana 10",justify=CENTER,fill="black")
                elif (go_error==2):
                    canvas.create_text(ras*6.75,ras*9.5,text="you can't walk like that",font="Verdana 10",justify=CENTER,fill="black")
                elif (go_error==3):
                    canvas.create_text(ras*6.75,ras*9.5,text="now moved other color",font="Verdana 10",justify=CENTER,fill="black")
        else:
            canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="red")
            #-----------------
            canvas.create_rectangle(ras*0.2,ras*9.2,ras*1.8,ras*9.8,fill="grey")
            if (control_add==1):
                canvas.create_text(ras,ras*9.5,text="add white",font="Verdana 10",justify=CENTER,fill="black")
            else:
                canvas.create_text(ras,ras*9.5,text="add black",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*2,ras*9.2,ras*3.8,ras*9.8,fill="grey")
            if (control_move==1):
                canvas.create_text(2.9*ras,ras*9.5,text="move white",font="Verdana 10",justify=CENTER,fill="black")
            else:
                canvas.create_text(2.9*ras,ras*9.5,text="move black",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*5.2,ras*9.2,ras*8.8,ras*9.8,fill="grey")
            if (control_vs==1):
                canvas.create_text(7*ras,ras*9.5,text="robot(white) vs people",font="Verdana 10",justify=CENTER,fill="black")
            elif (control_vs==2):
                canvas.create_text(7*ras,ras*9.5,text="robot(black) vs people",font="Verdana 10",justify=CENTER,fill="black")
            elif (control_vs==3):
                canvas.create_text(7*ras,ras*9.5,text="people vs people",font="Verdana 10",justify=CENTER,fill="black")
            else:
                canvas.create_text(7*ras,ras*9.5,text="robor vs robot",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*4.5,ras*9.5,text="edit",font="Verdana 12",justify=CENTER,fill="black")
        x = 0
    
    def reboot_checkers():
        global area_monitor
        area = area_monitor
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
        canvas.create_rectangle(0,0,ras*9,ras*9,fill="grey")
        canvas.create_rectangle(ras*0.5,ras*0.5,ras*8.5,ras*8.5,fill="white")
        while (y < 8):
            x = 0
            while (x < 8):
                if ((klik[0][0] == x) and (klik[0][1] == y+1) and (klik[1][0] == -1) and (klik[1][1] == -1)):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="red",outline="red")
                elif (go_color == area[y+1][x]%10):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="black",outline="red",width=1.5)
                else:
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2*3,x*ras+ras/2*3,y*ras+ras/2*5,fill="black",outline="black")
                x = x + 1
                if ((klik[0][0] == x) and (klik[0][1] == y) and (klik[1][0] == -1) and (klik[1][1] == -1)):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="red",outline="red")
                elif (go_color == area[y][x]%10):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="black",outline="red",width=1.5)
                else:
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="black",outline="black")
                x = x + 1
            y = y + 2
        #canvas.create_text(ras/4+0*ras,ras/4+1*ras,text="A",font="Verdana 12",justify=CENTER,fill="black")
        canvas.create_text(ras*1,ras*0.25,text="a",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*2,ras*0.25,text="b",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*3,ras*0.25,text="c",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*4,ras*0.25,text="d",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*5,ras*0.25,text="e",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*6,ras*0.25,text="f",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*7,ras*0.25,text="g",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8,ras*0.25,text="h",font="Verdana 10",justify=CENTER,fill="black")
        
        canvas.create_text(ras*1,ras*8.75,text="a",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*2,ras*8.75,text="b",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*3,ras*8.75,text="c",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*4,ras*8.75,text="d",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*5,ras*8.75,text="e",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*6,ras*8.75,text="f",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*7,ras*8.75,text="g",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8,ras*8.75,text="h",font="Verdana 10",justify=CENTER,fill="black")

        canvas.create_text(ras*0.25,ras*1,text="8",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*2,text="7",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*3,text="6",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*4,text="5",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*5,text="4",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*6,text="3",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*7,text="2",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*0.25,ras*8,text="1",font="Verdana 10",justify=CENTER,fill="black")
        
        canvas.create_text(ras*8.75,ras*1,text="8",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*2,text="7",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*3,text="6",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*4,text="5",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*5,text="4",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*6,text="3",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*7,text="2",font="Verdana 10",justify=CENTER,fill="black")
        canvas.create_text(ras*8.75,ras*8,text="1",font="Verdana 10",justify=CENTER,fill="black")
        # make checkers
        x = 0
        y = 0
        while (y < 8):
            x = 0
            while (x < 8): 
                if ((area[y][x] != 9) and (area[y][x] != 0)):
                    if (area[y][x]%10 == 1):
                        canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="black")
                    else:
                        canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="grey", outline="grey")
                    if (area[y][x]/10 >= 1):
                        canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="red")
                x = x + 1
            y = y + 1
            #out_window.update()

    def can_i_eat(y,x,area):
        global go_color
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

    def coordinates_print(y,x):
        if (1):
            if  (x==0):
                print("a",-y+8)
            elif(x==1):
                print("b",-y+8)
            elif(x==2):
                print("c",-y+8)
            elif(x==3):
                print("d",-y+8)
            elif(x==4):
                print("e",-y+8)
            elif(x==5):
                print("f",-y+8)
            elif(x==6):
                print("g",-y+8)
            elif(x==7):
                print("h",-y+8)
            else:
                print("ERROR: coordinates")

    
        

    def generator_move():
        x = 0
                
    
    def go_controll(area, K):
        k = 0
        #global area
        global klik
        global go_color
        global go_error
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
                        if(K==1):
                            go_error = 2
                        if(k==1):
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
                            if(K==1):
                                go_error = 2
                            if(k==1):
                                print("you can not commit this move (error number 1)")
                    else:
                        if(K==1):
                            go_error = 2
                        if(k==1):
                            print("you can not commit this move (error number 2)")
            elif (eat==1 and flag==0):
                if(K==1):
                    go_error = 1
                if(k==1):
                    print("you mast eat")
            elif (flag==0):
                if(K==1):
                    go_error = 2
                if(k==1):
                    print("you can not commit this move (error number 3)")
        else:
            if(K==1):
                go_error = 2
            if(k==1):
                print("you can not commit this move (error number 4)")
        if (flag==1):
            go_error = 0
        reboot_controller()
        #print(go_error)
        return flag

    def eat_checkers():
        global area_monitor
        area = area_monitor
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
        global area_monitor
        area = area_monitor
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
        global area_monitor
        area = area_monitor
        global klik
        global go_color
        global go_error
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
        if (can_i_eat( klik[1][1] , klik[1][0] ,area) and c==1):
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
        area_monitor = area
        go_error = 0
        #reboot_controller()
        reboot_checkers()
        no_wins()
        
    #===================================================================================================================================================================================================

    def mozg_random():
        out_window.update()
        global area_monitor
        global klik
        global go_color
        area = area_monitor
        if (no_wins()):
            x = 0
            y = 7
            flag = 1
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
                    if (go_controll(area,0)):
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
            if(can_i_eat(klik[0][1],klik[0][0],area)):
                mozg_random()


    def mozg_random2():
        #out_window.update()
        global area_operation
        #area = area_operation
        global klik
        global go_color
        global go_operation
        global count1
        global count2
        #massive[1][0].clear()
        #massive[1][0].append(5)
        #massive[1][0].append(5)
        #len(massive[0])
        #mas = deepcopy(massive)
        go_operation = []
        count1 = 0
        count2 = 0
        count3 = 0

        def go_more2(area1):
            global klik
            global go_color
            global go_operation
            global count1
            global count2
            global count3
            count2 = count2 + 1
            x = 0
            y = 0
            xa = 0 # shaska => damka
            while (xa <= 7):
                if (area1[0][xa] == 1):
                    area1[0][xa] = area1[0][xa] + 10
                xa = xa + 1
            xa = 0
            while (xa <= 7):
                if (area1[7][xa] == 2):
                    area1[7][xa] = area1[7][xa] + 10
                xa = xa + 1
            while (y <= 7):
                if (area1[y][x]==0):
                    klik[1][0] = x
                    klik[1][1] = y
                    if (go_controll(area1,0)):
                        area2 = deepcopy(area1)
                        coordinates_print(y,x)
                        if (len(go_operation[count1])==0 and 0):
                            u = 0
                            while(u < count2):
                                go_operation[count1].append(go_operation[count1-1][u])
                                u = u + 1
                        go_operation[count1].append(y*10+x)
                        #============================
                        q = area2[ klik[0][1] ][ klik[0][0] ]
                        area2[ klik[0][1] ][ klik[0][0] ] = 0
                        area2[ klik[1][1] ][ klik[1][0] ] = q
                        #============================
                        x0c = klik[0][0]
                        y0c = klik[0][1]
                        x1c = klik[1][0]
                        y1c = klik[1][1]
                        c = 0
                        if ((abs(x0c-x1c)==abs(y0c-y1c) and abs(y0c-y1c)>=2)): # eat
                            while (x1c!=x0c):
                                if (area2[y0c][x0c] != 0):
                                    c = 1
                                area2[y0c][x0c] = 0
                                x0c = x0c + znak(x1c-x0c)
                                y0c = y0c + znak(y1c-y0c)
                        #c = eat_checkers(area)
                        if (can_i_eat( klik[1][1] , klik[1][0] ,area2) and c==1):
                            kl0 = klik[0][0]
                            kl1 = klik[0][1]
                            klik[0][0] = klik[1][0]
                            klik[0][1] = klik[1][1]
                            klik[1][0] = -1
                            klik[1][1] = -1
                            go_more(area2)
                            klik[0][0] = kl0
                            klik[0][1] = kl1
                        else:
                            go_operation.append([])
                            count1 = count1 + 1
                            u = 0
                            while(u < count2 and 0):
                                go_operation[count1].append(go_operation[count1-1][u])
                                u = u + 1

        def go_more(area1):
            global klik
            global go_color
            global go_operation
            global count1
            global count2
            #global count3
            count2 = count2 + 1
            x = 0
            y = 0
            xa = 0 # shaska => damka
            while (xa <= 7):
                if (area1[0][xa] == 1):
                    area1[0][xa] = area1[0][xa] + 10
                xa = xa + 1
            xa = 0
            while (xa <= 7):
                if (area1[7][xa] == 2):
                    area1[7][xa] = area1[7][xa] + 10
                xa = xa + 1
            while (y <= 7):
                if (area1[y][x]==0):
                    klik[1][0] = x
                    klik[1][1] = y
                    if (go_controll(area1,0)):
                        area2 = deepcopy(area1)
                        #coordinates_print(y,x)
                        if (len(go_operation[count1])==0):
                            u = 0
                            while(u < count2):
                                go_operation[count1].append(go_operation[count1-1][u])
                                u = u + 1
                        go_operation[count1].append(y*10+x)
                        #============================
                        q = area2[ klik[0][1] ][ klik[0][0] ]
                        area2[ klik[0][1] ][ klik[0][0] ] = 0
                        area2[ klik[1][1] ][ klik[1][0] ] = q
                        #============================
                        x0c = klik[0][0]
                        y0c = klik[0][1]
                        x1c = klik[1][0]
                        y1c = klik[1][1]
                        c = 0
                        if ((abs(x0c-x1c)==abs(y0c-y1c) and abs(y0c-y1c)>=2)): # eat
                            while (x1c!=x0c):
                                if (area2[y0c][x0c] != 0):
                                    c = 1
                                area2[y0c][x0c] = 0
                                x0c = x0c + znak(x1c-x0c)
                                y0c = y0c + znak(y1c-y0c)
                        #c = eat_checkers(area)
                        if (can_i_eat( klik[1][1] , klik[1][0] ,area2) and c==1):
                            kl0 = klik[0][0]
                            kl1 = klik[0][1]
                            klik[0][0] = klik[1][0]
                            klik[0][1] = klik[1][1]
                            klik[1][0] = -1
                            klik[1][1] = -1
                            go_more(area2)
                            klik[0][0] = kl0
                            klik[0][1] = kl1
                        else:
                            go_operation.append([])
                            count1 = count1 + 1
                if(x >= 7):
                    x = 0
                    y = y + 1
                else:
                    x = x + 1
            if (count2<2):
                count1 = count1 + 1
            count2 = count2 - 1
        
        if (no_wins()):
            x = 0
            y = 0
            flag = 0
            while (y <= 7): 
                area2 = deepcopy(area_operation)
                if (area2[y][x]%10==go_color):
                    klik[0][0] = x
                    klik[0][1] = y
                    go_operation.append([y*10+x])
                    count2 = 0
                    go_more(area2)
                    #print("--------------------")
                if(x >= 7):
                    x = 0
                    y = y + 1
                else:
                    x = x + 1
            # celection go_operation
            go_operation2 = deepcopy(go_operation)
            i = 0
            go_operation.clear()
            while (i < len(go_operation2)): # and 0
                if (len(go_operation2[i]) > 1):
                    go_operation.append(go_operation2[i])
                i = i + 1
            i = 0
            while (i < len(go_operation)):
                print(go_operation[i])
                i = i + 1
            print("====================")

    
    def mozg():
        global area_operation
        global area_monitor
        global klik
        area_operation = area_monitor
        #generator_move()
        mozg_random2()
        klik = [[-1,-1],
                [-1,-1]]
        mozg_random()
        klik = [[-1,-1],
                [-1,-1]]
        
    
        
    
    def click(event):
        global area_monitor
        global klik
        global go_color
        global go_error
        global control_move
        global control_add
        global control_edit
        global control_vs
        x = event.x
        y = event.y
        #area = area_monitor
        #print(x, y)
        if ((x >= ras/2) and (x <= ras/2*17) and (y >= ras/2) and (y <= ras/2*17)): 
            x = map(x, ras/2, ras/2*17, 0, 8)
            y = map(y, ras/2, ras/2*17, 0, 8)
            #print(x, y)
            if (control_edit==0):
                if ((klik[0][0] == -1) and (area_monitor[y][x] != 9) and (area_monitor[y][x] != 0)):
                    if (area_monitor[y][x]%10==go_color):
                        klik[0][0] = x
                        klik[0][1] = y
                        go_error = 0
                        reboot_checkers()
                        reboot_controller()
                    else:
                        go_error = 3
                        reboot_controller()
                        #print("now moved other color")
                elif ((klik[0][0] != -1) and (klik[0][0] == x) and (klik[0][1] == y)):
                    klik[0][0] = -1
                    klik[0][1] = -1
                    go_error = 0
                    reboot_controller()
                    reboot_checkers()
                elif ((klik[0][0] != -1) and (area_monitor[y][x] != 9) and (area_monitor[y][x] == 0)):
                    klik[1][0] = x
                    klik[1][1] = y 
                    if (go_controll(area_monitor,1)):
                        c = go_color
                        move();
                        go_error = 0
                        if (go_color!=c and control_vs!=3):
                            mozg()
                            go_color = c
                        go_error = 0
                    else:
                        klik[1][0] = -1
                        klik[1][1] = -1
                else:
                    print("ERROR")
                    go_error = 2
                    reboot_controller()
                    #print(klik)
                    #print(area_monitor)
            elif (area_monitor[y][x] != 9):
                if (area_monitor[y][x]==0):
                    area_monitor[y][x] = control_add
                elif (area_monitor[y][x]%10==control_add and area_monitor[y][x]/10<1):
                    area_monitor[y][x] = control_add + 10
                elif (area_monitor[y][x]%10!=control_add or area_monitor[y][x]/10>1):
                    area_monitor[y][x] = 0
                reboot_checkers()
                
        else:
            klik[0][0] = -1
            klik[0][1] = -1
            klik[1][0] = -1
            klik[1][1] = -1
            if (y>=ras*9.2 and y<=ras*9.8):
                if (x>=ras*4 and x<=ras*5):
                    if (control_edit==1):
                        control_edit = 0
                        go_color = control_move
                        if (go_color==control_vs or control_vs==4):
                            mozg()
                    else:
                        control_edit = 1
                        control_move = go_color
                        go_color = -1
                    reboot_controller()
                    reboot_checkers()
                elif (control_edit==1):
                    if (x>=ras*0.2 and x<=ras*1.8):
                        if (control_add==1):
                            control_add=2
                        else:
                            control_add=1
                    if (x>=ras*2   and x<=ras*3.8):
                        if (control_move==1):
                            control_move=2
                        else:
                            control_move=1
                    if (x>=ras*5.2 and x<=ras*8.8):
                        if (control_vs<=2):
                            control_vs=control_vs+1
                        else:
                            control_vs=1
                    reboot_controller()

        #reboot_checkers()
        #no_wins()
            
            
    reboot_checkers()
    reboot_controller()
    
    canvas.bind("<Button-1>", click)

    canvas.pack()
    out_window.mainloop()
    #in_window.mainloop()

qwerty()
