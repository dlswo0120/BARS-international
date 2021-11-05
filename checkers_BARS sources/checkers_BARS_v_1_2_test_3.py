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

print("Russian checkers")
print("made by Bakay Egor")
print("w - white")
print("b - black")
print("c - simple checker")
print("l - lady checker")
print("<> - eat checker")
print("possible moves:")
print("====================")

area_zero = [[9, 2, 9, 2, 9, 2, 9, 2],
             [2, 9, 2, 9, 2, 9, 2, 9],
             [9, 2, 9, 2, 9, 2, 9, 2],
             [0, 9, 0, 9, 0, 9, 0, 9],
             [9, 0, 9, 0, 9, 0, 9, 0],
             [1, 9, 1, 9, 1, 9, 1, 9],
             [9, 1, 9, 1, 9, 1, 9, 1],
             [1, 9, 1, 9, 1, 9, 1, 9]]

area_zero2 = [[9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9],
              [9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9],
              [9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9],
              [9, 0, 9, 0, 9, 0, 9, 0],
              [0, 9, 0, 9, 0, 9, 0, 9]]

#area_operation = []

area_monitor0 = [[9, 12, 9, 12, 9, 2, 9, 2],
                [2, 9, 2, 9, 2, 9, 2, 9],
                [9, 2, 9, 2, 9, 2, 9, 2],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [1, 9, 1, 9, 1, 9, 1, 9],
                [9, 1, 9, 1, 9, 1, 9, 1],
                [1, 9, 11, 9, 11, 9, 1, 9]]

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
                [0, 9, 1, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 1, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 1, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor4 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 2, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 2, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor5 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 2, 9, 2, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 2, 9, 2, 9, 0],
                [0, 9, 0, 9, 1, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor6 = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 2, 9, 2, 9, 0, 9],
                [9, 0, 9, 2, 9, 0, 9, 0],
                [12, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 1, 9, 0],
                [0, 9, 1, 9, 1, 9, 0, 9],
                [9, 0, 9, 0, 9, 1, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9]]

area_monitor = [[9, 0, 9, 0, 9, 0, 9, 0],
                [0, 9, 2, 9, 2, 9, 2, 9],
                [9, 0, 9, 0, 9, 2, 9, 0],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 1, 9, 1, 9, 12],
                [0, 9, 0, 9, 1, 9, 0, 9],
                [9, 0, 9, 1, 9, 0, 9, 1],
                [0, 9, 0, 9, 0, 9, 0, 9]]

history = []
go = [] # все варианты будующих ходов
go_operation = []

#massive[1][0].clear()
#massive[1][0].append(5)
#massive[1][0].append(5)
#len(massive[0])
#mas = deepcopy(massive)
#del mas[y]
#print(go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1])# самый последний элемент

#print('Text text', end='')

klik = [[-1,-1],
        [-1,-1]]
klik_flag = 1

moved_checkers = -1

go_color = 1

count1 = 0  # for generator_move
#count2 = 0
#count3 = 0

#value = 0

control_move = go_color
control_add = 1
control_edit = 0
control_vs = 3
go_error = 0
control_back = 0
control_forward = 0

def qwerty():
    global area_monitor
    global area_zero
    global area_zero2
    global klik
    global klik_flag
    global go_color
    global history
    global go
    global go_operation
    global count1
    #global count2
    #global count3
    global control_move
    global control_add
    global control_edit
    global control_vs
    global go_error
    global control_forward
    global control_back
    global moved_checkers
    
    out_window = Tk()
    out_window.title('BARS 1.2')  # demonstration
    #window.geometry('1000x1000')
    #canvas = Canvas(out_window,width=9*ras,height=9*ras)
    canvas = Canvas(out_window,width=9*ras,height=10*ras,bg="grey") # ,cursor="pencil"

    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
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
    
    def reboot_controller():
        global go_color     
        global control_move
        global control_add
        global control_edit
        global control_vs # за кого играет робот
        global go_error
        global control_back
        canvas.create_rectangle(0,ras*9,ras*9,ras*10,fill="#c96") #feb 
        if (control_edit==0):
            canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="#c96")
            if (go_error==11):
                canvas.create_text(ras*7,ras*9.5,text="white wins!",font="Verdana 15",justify=CENTER,fill="black")
            elif (go_error==12):
                canvas.create_text(ras*7,ras*9.5,text="black wins!",font="Verdana 15",justify=CENTER,fill="black")
            elif (control_vs==1 and go_color==2 or control_vs==2 and go_color==1 or control_vs==3):
                if (go_error==1):
                    canvas.create_text(ras*7,ras*9.5,text="you must eat",font="Verdana 10",justify=CENTER,fill="black")
                elif (go_error==2):
                    canvas.create_text(ras*7,ras*9.5,text="you can't walk like that",font="Verdana 10",justify=CENTER,fill="black")
                elif (go_error==3):
                    canvas.create_text(ras*7,ras*9.5,text="now moved other color",font="Verdana 10",justify=CENTER,fill="black")
            #canvas.create_rectangle(ras*0.2,ras*9.2,ras*1.8,ras*9.8,fill="grey")
            if (control_back==1):
                #canvas.create_rectangle(ras*0.2,ras*9.2,ras*1.2,ras*9.8,fill="grey")
                canvas.create_rectangle(ras*0.2,ras*9.2,ras*0.8,ras*9.8,fill="grey")
                canvas.create_text(ras*0.5,ras*9.5,text="back",font="Verdana 7",justify=CENTER,fill="black")
            if (control_forward==1):
                #canvas.create_rectangle(ras*2,ras*9.2,ras*3.8,ras*9.8,fill="grey")
                canvas.create_rectangle(ras*1.4,ras*9.2,ras*3.0,ras*9.8,fill="grey")
                canvas.create_text(ras*2.2,ras*9.5,text="forward",font="Verdana 10",justify=CENTER,fill="black")
        else:
            canvas.create_rectangle(ras*4,ras*9.2,ras*5,ras*9.8,fill="red")
            #-----------------
            canvas.create_rectangle(ras*0.2,ras*9.2,ras*0.8,ras*9.8,fill="grey")
            canvas.create_text(ras/2,ras*9.5,text="clear",font="Verdana 7",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*1.0,ras*9.2,ras*2.2,ras*9.8,fill="grey")
            if (control_add==1):
                canvas.create_text(ras*1.6,ras*9.5,text="add white",font="Verdana 8",justify=CENTER,fill="black")
            else:
                canvas.create_text(ras*1.6,ras*9.5,text="add black",font="Verdana 8",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*2.4,ras*9.2,ras*3.8,ras*9.8,fill="grey")
            if (control_move==1):
                canvas.create_text(3.1*ras,ras*9.5,text="move white",font="Verdana 8",justify=CENTER,fill="black")
            else:
                canvas.create_text(3.1*ras,ras*9.5,text="move black",font="Verdana 8",justify=CENTER,fill="black")
            #canvas.create_rectangle(ras*5.2,ras*9.2,ras*8.8,ras*9.8,fill="grey")   7*ras
            canvas.create_rectangle(ras*5.2,ras*9.2,ras*8.0,ras*9.8,fill="grey")
            if (control_vs==1):
                canvas.create_text(6.6*ras,ras*9.5,text="robot(white) vs people",font="Verdana 8",justify=CENTER,fill="black")
            elif (control_vs==2):
                canvas.create_text(6.6*ras,ras*9.5,text="people vs robot(black)",font="Verdana 8",justify=CENTER,fill="black")
            elif (control_vs==3):
                canvas.create_text(6.6*ras,ras*9.5,text="people vs people",font="Verdana 10",justify=CENTER,fill="black")
            else:
                canvas.create_text(7*ras,ras*9.5,text="robor vs robot",font="Verdana 10",justify=CENTER,fill="black")
            canvas.create_rectangle(ras*8.2,ras*9.2,ras*8.8,ras*9.8,fill="grey")
            canvas.create_text(8.5*ras,ras*9.4,text="new", font="Verdana 7",justify=CENTER,fill="black")
            canvas.create_text(8.5*ras,ras*9.6,text="game",font="Verdana 7",justify=CENTER,fill="black")
        canvas.create_text(ras*4.5,ras*9.5,text="edit",font="Verdana 12",justify=CENTER,fill="black")
        x = 0
    
    def reboot_checkers():
        global area_monitor
        area = area_monitor
        global klik
        global go_color
        global moved_checkers
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
        canvas.create_rectangle(0,0,ras*9,ras*9,fill="#feb")
        canvas.create_rectangle(ras*0.5,ras*0.5,ras*8.5,ras*8.5,fill="#feb")
        while (y < 8):
            x = 0
            while (x < 8):
                if (area[y][x]!=9):
                    canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="#c96",outline="#c96") # "#630"
                    if (area[y][x]!=0 and area[y][x]<100 and 1):
                        wer = 0.05
                        canvas.create_oval([x*ras+ras/2+ras*wer+ras/10,(y-1)*ras+ras/2*3+ras/10+ras*wer],[x*ras+ras/2*3-ras/10+ras*wer,(y-1)*ras+ras/2*5-ras/10+ras*wer],fill="#643", outline="#643")
                        
                x = x + 1
            y = y + 1
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
                    #if (area[y][x]==5):
                    #    canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="blue", outline="blue")
                    if (area[y][x]%10==1):
                        if (moved_checkers==y*10+x):
                            canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="red")
                        elif (go_color==1):
                            canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="white")
                        else:
                            canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10],fill="white", outline="white") # , width=2
                    else:
                        qwe = 10
                        if (moved_checkers==y*10+x):
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="red")
                        elif (go_color==2):
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="black")
                        else:
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="black")
                    if (int(area[y][x]/10)%10 >= 1):
                        #canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="green")
                        if (area[y][x]%10==1):
                            #canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="white")
                            wer = 5
                            canvas.create_oval([x*ras+ras/2+ras/wer,(y-1)*ras+ras/2*3+ras/wer],[x*ras+ras/2*3-ras/wer,(y-1)*ras+ras/2*5-ras/wer],fill="#bb9", outline="#bb9") 
                        else:
                            #canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="grey")
                            wer = 5
                            canvas.create_oval([x*ras+ras/2+ras/wer,(y-1)*ras+ras/2*3+ras/wer],[x*ras+ras/2*3-ras/wer,(y-1)*ras+ras/2*5-ras/wer],fill="#555", outline="#555") 
                            #qwe = 3.5
                            #canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="grey")
                    else:
                        if (area[y][x]%10==1):
                            wer = 5
                            canvas.create_oval([x*ras+ras/2+ras/wer,(y-1)*ras+ras/2*3+ras/wer],[x*ras+ras/2*3-ras/wer,(y-1)*ras+ras/2*5-ras/wer],fill="white", outline="grey")
                            qwe = 3.3
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="white", outline="grey")
                            #canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="white")
                        else:
                            #canvas.create_oval([x*ras+ras/2+ras/4,(y-1)*ras+ras/2*3+ras/4],[x*ras+ras/2*3-ras/4,(y-1)*ras+ras/2*5-ras/4],fill="grey")
                            wer = 5
                            canvas.create_oval([x*ras+ras/2+ras/wer,(y-1)*ras+ras/2*3+ras/wer],[x*ras+ras/2*3-ras/wer,(y-1)*ras+ras/2*5-ras/wer],fill="black", outline="grey")
                            qwe = 3.3
                            canvas.create_oval([x*ras+ras/2+ras/qwe,(y-1)*ras+ras/2*3+ras/qwe],[x*ras+ras/2*3-ras/qwe,(y-1)*ras+ras/2*5-ras/qwe],fill="black", outline="grey")
                    if (area[y][x]>100):
                        #canvas.create_rectangle(x*ras+ras/2,y*ras+ras/2,x*ras+ras/2*3,y*ras+ras/2*3,fill="#000",outline="#c96")
                        #canvas.create_oval([x*ras+ras/2+ras/10,(y-1)*ras+ras/2*3+ras/10],[x*ras+ras/2*3-ras/10,(y-1)*ras+ras/2*5-ras/10], fill="#dca", outline="black")
                        canvas.create_line(x*ras+ras*0.8,y*ras+ras*0.55,x*ras+ras*1.45,y*ras+ras*1.0,width=3,fill="#c96") # \
                        canvas.create_line(x*ras+ras*0.55,y*ras+ras*1.4,x*ras+ras*1.2,y*ras+ras*0.6,width=5,fill="#c96") # /
                        #canvas.create_line(x*ras+ras*1.0,y*ras+ras*0.5,x*ras+ras*1.0,y*ras+ras*1.5,width=2,fill="#c96") # |
                        canvas.create_line(x*ras+ras*1.5,y*ras+ras*1.2,x*ras+ras*0.5,y*ras+ras*1.4,width=4,fill="#c96") # -
                x = x + 1
            y = y + 1
            canvas.create_rectangle(ras*0.5,ras*0.5,ras*8.5,ras*8.5)
            #out_window.update()
    
    def reboot_monitor():
        canvas.delete("all")
        reboot_checkers()
        reboot_controller()
        
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    
    def generator_move(area_operation, go_color):
        global go_operation
        global count1
        global area_monitor
        area = deepcopy(area_operation)
        klik = [[-1,-1],
                [-1,-1]]
        go_operation = []
        count1 = 0
        #massive[1][0].clear()
        #massive[1][0].append(5)
        #massive[1][0].append(5)
        #len(massive[0])
        #mas = deepcopy(massive)
        #del mas[y]
        
        def bumerang(y2, x2):
            global go_operation

            def znak2(r):
                if (r>0):
                    return 1
                else:
                    return 0
                
            if (len(go_operation[len(go_operation)-1])<2):
                return 1
            else:
                into = go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]  # самый последний элемент
                into = into%100
                y1 = int(into/10)
                x1 = into%10
                into = go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-2] # самый предпоследний элемент
                into = into%100
                y0 = int(into/10)
                x0 = into%10
                a = znak2(x1-x0)
                b = znak2(y1-y0)
                c = znak2(x2-x1)
                d = znak2(y2-y1)
                if ((a==0 and c==1 or a==1 and c==0) and (d==0 and b==1 or d==1 and b==0)): # просто алгебра логики
                    return 0 # <=====
                    #return 1
                else:
                    return 1
    
        def eating2(area1, y0, x0, y1, x1):
            global count1
            klik = [[x0,y0],
                    [x1,y1]]
            if(1):
                if(1):
                    if(1):
                        area2 = deepcopy(area1)
                        q = area2[ klik[0][1] ][ klik[0][0] ]
                        area2[ klik[0][1] ][ klik[0][0] ] = 0
                        area2[ klik[1][1] ][ klik[1][0] ] = q
                        x0c = klik[0][0]
                        y0c = klik[0][1]
                        x1c = klik[1][0]
                        y1c = klik[1][1]
                        c = 0
                        if ((abs(x0c-x1c)==abs(y0c-y1c) and abs(y0c-y1c)>=2)): # eat
                            while (x1c!=x0c):
                                if (area2[y0c][x0c] != 0):
                                    if(1): # записать в go_operation какие шашки были съедены
                                        count1 = count1 + 1
                                        into = go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]
                                        go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1] = 10000+area2[y0c][x0c]*100+y0c*10+x0c
                                        go_operation[len(go_operation)-1].append(into)
                                        #go_operation[len(go_operation)-1].append(10000+area2[y0c][x0c]*100+y0c*10+x0c)
                                    area2[y0c][x0c] = area2[y0c][x0c] + 100 # правило одной руки
                                    #area2[y0c][x0c] = 0
                                x0c = x0c + znak(x1c-x0c)
                                y0c = y0c + znak(y1c-y0c)
                        area2[ klik[0][1] ][ klik[0][0] ] = 0
                        eating(area2, go_color, y1, x1)
        
        def eating(area_operation, go_color, y, x):
            global count1
            global go_operation
            count1 = count1 + 1
            area = deepcopy(area_operation)
            x0 = klik[0][0]
            y0 = klik[0][1]
            x1 = klik[1][0]
            y1 = klik[1][1]
            eat = 0
            xa = 0 # shaska => damka
            while (xa <= 7):
                if (area[0][xa] == 1):
                    area[0][xa] = area[0][xa] + 10
                if (area[7][xa] == 2):
                    area[7][xa] = area[7][xa] + 10
                xa = xa + 1
            if(1):
                if (area[y][x]==go_color): # proverka na vozmognost siest shaskami
                    if (y-2>=0 and x-2>=0):
                        if (area[y][x]%10!=area[y-1][x-1]%10 and area[y-1][x-1]<100 and area[y][x]!=0 and area[y-1][x-1]!=0 and area[y-2][x-2]==0 and bumerang(y-2, x-2)):
                            eat = 1
                            a = 0
                            if (y==2 and go_color==1):
                                a = 1000 
                            go_operation[len(go_operation)-1].append(a+go_color*100+(y-2)*10+(x-2))
                            eating2(area, y, x, y-2, x-2)
                    if (y+2<=7 and x-2>=0):
                        if (area[y][x]%10!=area[y+1][x-1]%10 and area[y+1][x-1]<100 and area[y][x]!=0 and area[y+1][x-1]!=0 and area[y+2][x-2]==0 and bumerang(y+2, x-2)):
                            eat = 1
                            a = 0
                            if (y==5 and go_color==2):
                                a = 1000 
                            go_operation[len(go_operation)-1].append(a+go_color*100+(y+2)*10+(x-2))
                            eating2(area, y, x, y+2, x-2)
                    if (y-2>=0 and x+2<=7):
                        if (area[y][x]%10!=area[y-1][x+1]%10 and area[y-1][x+1]<100 and area[y][x]!=0 and area[y-1][x+1]!=0 and area[y-2][x+2]==0 and bumerang(y-2, x+2)):
                            eat = 1
                            a = 0
                            if (y==2 and go_color==1):
                                a = 1000 
                            go_operation[len(go_operation)-1].append(a+go_color*100+(y-2)*10+(x+2))
                            eating2(area, y, x, y-2, x+2)
                    if (y+2<=7 and x+2<=7):
                        if (area[y][x]%10!=area[y+1][x+1]%10 and area[y+1][x+1]<100 and area[y][x]!=0 and area[y+1][x+1]!=0 and area[y+2][x+2]==0 and bumerang(y+2, x+2)): 
                            eat = 1
                            a = 0
                            if (y==5 and go_color==2):
                                a = 1000 
                            go_operation[len(go_operation)-1].append(a+go_color*100+(y+2)*10+(x+2))
                            eating2(area, y, x, y+2, x+2)
                if (area[y][x]==go_color+10 and 1): # proverka na vozmognost siest damkami 
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
                        if (yd1>0 and xd1>0 and area[yd1-1][xd1-1]==0 and area[yd1-1][xd1-1]<100):
                            yd1 = yd1 - 1
                            xd1 = xd1 - 1
                        if (yd2<7 and xd2>0 and area[yd2+1][xd2-1]==0 and area[yd2+1][xd2-1]<100):
                            yd2 = yd2 + 1
                            xd2 = xd2 - 1
                        if (yd3>0 and xd3<7 and area[yd3-1][xd3+1]==0 and area[yd3-1][xd3+1]<100):
                            yd3 = yd3 - 1
                            xd3 = xd3 + 1
                        if (yd4<7 and xd4<7 and area[yd4+1][xd4+1]==0 and area[yd4+1][xd4+1]<100):
                            yd4 = yd4 + 1
                            xd4 = xd4 + 1
                        i = i + 1
                    if (yd1-2>=0 and xd1-2>=0):
                        if (go_color!=area[yd1-1][xd1-1]%10 and area[yd1-1][xd1-1]<100 and area[yd1-1][xd1-1]!=0 and area[yd1-2][xd1-2]==0 and bumerang(yd1-1, xd1-1)):
                            eat = 1
                            yd1 = yd1 - 2
                            xd1 = xd1 - 2
                            if (1):
                                i = 1
                                while (yd1>=0 and xd1>=0 and i==1):
                                    go_operation[len(go_operation)-1].append(1000+go_color*100+(yd1)*10+(xd1))
                                    eating2(area, y, x, yd1, xd1)
                                    #if (area[yd1][xd1]==0 and yd1==y1 and xd1==x1):
                                    yd1 = yd1 - 1
                                    xd1 = xd1 - 1
                                    if (yd1>=0 and xd1>=0 and area[yd1][xd1]!=0):
                                        i = 0
                    if (yd2+2<=7 and xd2-2>=0):
                        if (go_color!=area[yd2+1][xd2-1]%10 and area[yd2+1][xd2-1]<100 and area[yd2+1][xd2-1]!=0 and area[yd2+2][xd2-2]==0 and bumerang(yd2+1, xd2-1)):
                            eat = 1
                            yd2 = yd2 + 2
                            xd2 = xd2 - 2
                            if (1):
                                i = 1
                                while (yd2<=7 and xd2>=0 and i==1):
                                    go_operation[len(go_operation)-1].append(1000+go_color*100+(yd2)*10+(xd2))
                                    eating2(area, y, x, yd2, xd2)
                                    #if (area[yd2][xd2]==0 and yd2==y1 and xd2==x1):
                                    yd2 = yd2 + 1
                                    xd2 = xd2 - 1
                                    if (yd2<=7 and xd2>=0 and area[yd2][xd2]!=0):
                                        i = 0
                    if (yd3-2>=0 and xd3+2<=7):
                        if (go_color!=area[yd3-1][xd3+1]%10 and area[yd3-1][xd3+1]<100 and area[yd3-1][xd3+1]!=0 and area[yd3-2][xd3+2]==0 and bumerang(yd3-1, xd3+1)):
                            eat = 1
                            yd3 = yd3 - 2
                            xd3 = xd3 + 2
                            if (1):
                                i = 1
                                while (yd3>=0 and xd3<=7 and i==1):
                                    go_operation[len(go_operation)-1].append(1000+go_color*100+(yd3)*10+(xd3))
                                    eating2(area, y, x, yd3, xd3)
                                    #if (area[yd3][xd3]==0 and yd3==y1 and xd3==x1):
                                    yd3 = yd3 - 1
                                    xd3 = xd3 + 1
                                    if (yd3>=0 and xd3<=7 and area[yd3][xd3]!=0):
                                        i = 0
                    if (yd4+2<=7 and xd4+2<=7):
                        if (go_color!=area[yd4+1][xd4+1]%10 and area[yd4+1][xd4+1]<100 and area[yd4+1][xd4+1]!=0 and area[yd4+2][xd4+2]==0 and bumerang(yd4+1, xd4+1)):
                            eat = 1
                            yd4 = yd4 + 2
                            xd4 = xd4 + 2
                            if (1):
                                i = 1
                                while (yd4<=7 and xd4<=7 and i==1):
                                    go_operation[len(go_operation)-1].append(1000+go_color*100+(yd4)*10+(xd4))
                                    eating2(area, y, x, yd4, xd4)
                                    #if (area[yd4][xd4]==0 and yd4==y1 and xd4==x1):
                                    yd4 = yd4 + 1
                                    xd4 = xd4 + 1
                                    if (yd4<=7 and xd4<=7 and area[yd4][xd4]!=0):
                                        i = 0
                    #==================================================================
            count1 = count1 - 1
            if (eat==0 and len(go_operation[len(go_operation) - 1])>1):
                #print(count1)
                go_operation.append([])
                i = 0
                c = len(go_operation) - 1
                while (i < count1):
                    go_operation[c].append(go_operation[c-1][i])
                    i = i + 1
            else:
                del go_operation[len(go_operation) - 1][count1]
            if (len(go_operation[len(go_operation)-1])>0):
                if (go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]>2000):
                    del go_operation[len(go_operation)-1][len(go_operation[len(go_operation)-1])-1]
                    count1 = count1 - 1
            return eat
        ##############################################################################
        x = 0
        y = 0
        eat = 0
        while (y<=7):
            go_operation.append([area[y][x]*100+y*10+x])
            if (eating(area, go_color, y ,x)==1):
                eat = 1
            else:
                del go_operation[len(go_operation)-1]
            x = x + 1
            if (x > 7):
                x = 0
                y = y + 1
        if (eat==1):
            wer = 0
            while (len(go_operation) > wer):
                if (len(go_operation[wer])==0):
                    del go_operation[wer]
                else:
                    wer = wer + 1
        #eat = 0
        ###########################
        if (eat==0): # not eat
            go_operation.clear()
            x = 0
            y = 0
            while (y<=7):
                if (area[y][x]%10==go_color):
                    if (area[y][x]/10<1): # not queen
                        if (go_color==1 and y>=1 and x>=1):
                            if (area[y-1][x-1]==0):
                                if (y==1):
                                    go_operation.append([100+y*10+x,1100+(y-1)*10+x-1])
                                else:
                                    go_operation.append([100+y*10+x, 100+(y-1)*10+x-1])
                        if (go_color==1 and y>=1 and x<=6):
                            if (area[y-1][x+1]==0):
                                if (y==1):
                                    go_operation.append([100+y*10+x,1100+(y-1)*10+x+1])
                                else:
                                    go_operation.append([100+y*10+x, 100+(y-1)*10+x+1])
                        if (go_color==2 and y<=6 and x>=1):
                            if (area[y+1][x-1]==0):
                                if (y==6):
                                    go_operation.append([200+y*10+x,1200+(y+1)*10+x-1])
                                else:
                                    go_operation.append([200+y*10+x, 200+(y+1)*10+x-1])
                        if (go_color==2 and y<=6 and x<=6):
                            if (area[y+1][x+1]==0):
                                if (y==6):
                                    go_operation.append([200+y*10+x,1200+(y+1)*10+x+1])
                                else:
                                    go_operation.append([200+y*10+x, 200+(y+1)*10+x+1])
                    else: # queen
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
                                go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd1*10+xd1])
                            if (yd2<7 and xd2>0 and area[yd2+1][xd2-1]==0):
                                yd2 = yd2 + 1
                                xd2 = xd2 - 1
                                go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd2*10+xd2])
                            if (yd3>0 and xd3<7 and area[yd3-1][xd3+1]==0):
                                yd3 = yd3 - 1
                                xd3 = xd3 + 1
                                go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd3*10+xd3])
                            if (yd4<7 and xd4<7 and area[yd4+1][xd4+1]==0):
                                yd4 = yd4 + 1
                                xd4 = xd4 + 1
                                go_operation.append([1000+go_color*100+y*10+x,1000+go_color*100+yd4*10+xd4])
                            i = i + 1
                x = x + 1
                if (x > 7):
                    x = 0
                    y = y + 1
        klik = [[-1,-1],
                [-1,-1]]
        if (1):
            #print('Text text', end='')
            go_operation2 = deepcopy(go_operation)
            i = 0
            if (eat==1 and 0):
                go_operation.clear()
                while (i < len(go_operation2)): # and 0
                    if (len(go_operation2[i]) > 1):
                        go_operation.append(go_operation2[i])
                    i = i + 1
                i = 0
        #=======================================================
        # съесть 0 или 1, 2 или 3?
        if (len(go_operation)>1): # если есть варианты, из чего выбирать
            if (len(go_operation[0])>2): # полюбас надо есть
                i = 0
                while (len(go_operation)>i+1):
                    u = 1
                    if (go_operation[i][0]==go_operation[i+1][0]):
                        flag = 1
                        while (len(go_operation[i])>u+1 and len(go_operation[i+1])>u+1 and flag==1):
                            if (go_operation[i][u]==go_operation[i+1][u] and go_operation[i][u+1]!=go_operation[i+1][u+1]):
                                flag = 0
                            else:
                                u = u + 2
                        if (flag==1):
                            u = u - 2
                        if (go_operation[i][u]==go_operation[i+1][u] and go_operation[i][u+1]!=go_operation[i+1][u+1]):
                            d1 = len(go_operation[i])
                            d2 = len(go_operation[i+1])
                            if (d1==d2):
                                i = i + 1
                            elif (u+2>=d1 and u+2<d2):
                                del go_operation[i]
                            elif (u+2<d1 and u+2>=d2):
                                del go_operation[i+1]
                            else:
                                print("selection error")
                                i = i + 1
                        else:
                            i = i + 1
                    else:
                        i = i + 1
        #print_go_operation()

    def print_go_operation():
        if (1): # 1 - выводить (0 - нет)
            i = 0
            while (i < len(go_operation)):
                print(i+1, " ", end='')
                if (1): # как выводить (1 - с человеческими координатами, 0 - как реально выглядит массив)
                    u = 0
                    while(u < len(go_operation[i])):
                        if (go_operation[i][u]>2000):
                            print("<", end='')
                        if (1): # 1 - выводить (0 - нет) какая шашка
                            asd = int(go_operation[i][u]/100)%100
                            if (asd==1):
                                print("(wc) ", end='')
                            if (asd==2):
                                print("(bc) ", end='')
                            if (asd==11):
                                print("(wl) ", end='')
                            if (asd==12):
                                print("(bl) ", end='')
                        yy = int(go_operation[i][u]/10)%10
                        xx = go_operation[i][u]%10
                        if  (xx==0):
                            print("a",-yy+8, end='')
                        elif(xx==1):
                            print("b",-yy+8, end='')
                        elif(xx==2):
                            print("c",-yy+8, end='')
                        elif(xx==3):
                            print("d",-yy+8, end='')
                        elif(xx==4):
                            print("e",-yy+8, end='')
                        elif(xx==5):
                            print("f",-yy+8, end='')
                        elif(xx==6):
                            print("g",-yy+8, end='')
                        elif(xx==7):
                            print("h",-yy+8, end='')
                        else:
                            print("error")
                        if (go_operation[i][u]>2000):
                            print(">", end='')
                        if (u+1 < len(go_operation[i])):
                            print(" - ", end='')
                        u = u + 1
                    if (len(go_operation[i])>0):
                        print()
                else:
                    print(go_operation[i])
                i = i + 1
            print("====================")
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def print_mas(mas):
        i = 0
        while (i<len(mas)):
            print(mas[i])
            i = i + 1

    def print_history():

        def print_coo(yy,xx):
            if(1):
                if(1):
                    if  (xx==0):
                        print("a", end='')
                    elif(xx==1):
                        print("b", end='')
                    elif(xx==2):
                        print("c", end='')
                    elif(xx==3):
                        print("d", end='')
                    elif(xx==4):
                        print("e", end='')
                    elif(xx==5):
                        print("f", end='')
                    elif(xx==6):
                        print("g", end='')
                    elif(xx==7):
                        print("h", end='')
                    else:
                        print("error")
                    print(-yy+8, end='')
        
        global history
        if (1): # 1 - выводить (0 - нет)
            print("history game:")
            print("** - white cell")
            print("-- - black cell")
            print("w - white")
            print("b - black")
            print("c - simple checker")
            print("l - lady checker")
            print("start field:")
            x = 0
            y = 0
            area = deepcopy(history[0])
            while (y<=7):
                if (area[y][x]==0):
                    print("-- ", end='')
                elif (area[y][x]==9):
                    print("** ", end='')
                elif (area[y][x]==1):
                    print("wc ", end='')
                elif (area[y][x]==2):
                    print("bc ", end='')
                elif (area[y][x]==11):
                    print("wl ", end='')
                elif (area[y][x]==12):
                    print("bl ", end='')
                x = x + 1
                if (x>7):
                    print()
                    x = 0
                    y = y + 1
            print("moves:")
            i = 1
            if (0): # непрофессиональный вывод (1 - да, 0 - профессиональный вывод)
                while (i < len(history)):
                    print(i, " ", end='')
                    if (1): # как выводить (1 - с человеческими координатами, 0 - как реально выглядит массив)
                        u = 0
                        while(u < len(history[i])):
                            if (history[i][u]>2000):
                                print("<", end='')
                            if (1): # 1 - выводить (0 - нет) какая шашка
                                asd = int(history[i][u]/100)%100
                                if (asd==1):
                                    print("(wc) ", end='')
                                if (asd==2):
                                    print("(bc) ", end='')
                                if (asd==11):
                                    print("(wl) ", end='')
                                if (asd==12):
                                    print("(bl) ", end='')
                            yy = int(history[i][u]/10)%10
                            xx = history[i][u]%10
                            print_coo(yy,xx)
                            if (history[i][u]>2000):
                                print(">", end='')
                            if (u+1 < len(history[i])):
                                print(" - ", end='')
                            u = u + 1
                        if (len(history[i])>0):
                            print()
                    else:
                        print(go_operation[i])
                    i = i + 1
            else:
                while (i < len(history)):
                    print(int(i/2)+1, " ", end='')
                    if (int(history[i][0]/100)%10==1):
                        y = int(history[i][0]/10)%10
                        x = history[i][0]%10
                        print_coo(y,x)
                        u = len(history[i])
                        if (u>2):
                            print(":", end='')
                        else:
                            print("-", end='')
                        y = int(history[i][u-1]/10)%10
                        x = history[i][u-1]%10
                        print_coo(y,x)
                    else:
                        print(".....", end='')
                    i = i + 1
                    print(" ", end='')
                    if (i<len(history)):
                        if (int(history[i][0]/100)%10==2):
                            y = int(history[i][0]/10)%10
                            x = history[i][0]%10
                            print_coo(y,x)
                            u = len(history[i])
                            if (u>2):
                                print(":", end='')
                            else:
                                print("-", end='')
                            y = int(history[i][u-1]/10)%10
                            x = history[i][u-1]%10
                            print_coo(y,x)
                        else:
                           print(".....", end='') 
                    else:
                        print(".....", end='')
                    print()
                    i = i + 1
            print("====================")
    
    def move(y0, x0, y1, x1, c):
        global area_monitor
        area_monitor[y0][x0] = 0
        x0 = x0 + znak(x1-x0)
        y0 = y0 + znak(y1-y0)
        while (x1!=x0):
            if (area_monitor[y0][x0]!=0):
                area_monitor[y0][x0] = area_monitor[y0][x0] + 500 # corpse
            x0 = x0 + znak(x1-x0)
            y0 = y0 + znak(y1-y0)
        area_monitor[y1][x1] = c
        reboot_monitor()
        out_window.update()

    def clear_corpse():
        reboot_checkers()
        reboot_controller()
        global area_monitor
        x = 0
        y = 0
        eat = 0
        while (y<=7):
            if(area_monitor[y][x]>100):
                area_monitor[y][x] = 0
                eat = 1
            x = x + 1
            if (x>7):
                y = y + 1
                x = 0
        if (eat==1):
            sleep(0.5)
            reboot_checkers()
            reboot_controller()

    def no_wins(go_color):
        global go_operation
        flag = 1
        if (len(go_operation)==0):
            flag = 0
        return flag

    def wins(go_color):
        global go_operation
        if (len(go_operation)==0):
            if (go_color==1):
                canvas.create_text(4.5*ras,4.5*ras,text="black wins!",font="Verdana 52",justify=CENTER,fill="blue")
            else:
                canvas.create_text(4.5*ras,4.5*ras,text="white wins!",font="Verdana 52",justify=CENTER,fill="blue")
            out_window.update()
        
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    #===================================================================================================================================================================================================
    
    def mozg_random():
        global area_monitor
        global go_color
        global go_operation
        global go_error
        global history
        generator_move(area_monitor,go_color)
        if (no_wins(go_color)):
            i = 1
            go_error = 0
            l = randint(0, len(go_operation)-1)
            history.append(go_operation[l])
            while (len(go_operation[l])-1>=i):
                into = go_operation[l][i-1]
                y0 = int(into/10)%10
                x0 = into%10
                if (go_operation[l][i]>2000):
                    i = i + 1
                into = go_operation[l][i]
                y1 = int(into/10)%10
                x1 = into%10
                ch = int(into/100)%100
                sleep(0.5)
                move(y0, x0, y1, x1, ch)
                i = i + 1
            clear_corpse()
        else:
            if (go_color==1):
                go_error = 12
            else:
                go_error = 11
            go_color = -1
            reboot_checkers()
            reboot_controller()
            out_window.update()
            print_history()
            
    
    def mozg():
        global go_color
        global go_error
        reboot_checkers()
        reboot_controller()
        out_window.update()
        if (go_color!=-1):
            mozg_random()
            if (go_color!=-1): # no_wins(go_color)
                if (go_color==1):
                    go_color = 2
                else:
                    go_color = 1
                generator_move(area_monitor,go_color)
                if (no_wins(go_color)==0):
                    if (go_color==1):
                        go_error = 12
                    else:
                        go_error = 11
                    go_color = -1
                    reboot_checkers()
                    reboot_controller()
                    out_window.update()
                    print_history()
                else:
                    print_go_operation()
            reboot_checkers()
            reboot_controller()

    def people_move(y,x):
        global history
        global go_operation
        global area_monitor
        global go_color
        global klik
        global go_error
        global moved_checkers
        if (klik[0][0]==-1 and area_monitor[y][x]!=9 and area_monitor[y][x]!=0): # взять шашку
            if (area_monitor[y][x]%10==go_color):
                klik[0][0] = x
                klik[0][1] = y
                moved_checkers = y*10+x
                go_error = 0
            else:
                go_error = 3
        elif (klik[0][0]!=-1 and klik[1][0]==-1 and klik[0][0]==x and klik[0][1]==y): # если никуда не ходили при необходимости отпустить
            klik[0][0] = -1
            klik[0][1] = -1
            moved_checkers = -1
            go_error = 0
        elif (klik[0][0]!=-1 and klik[1][0]==-1 and area_monitor[y][x]%10==go_color): # если никуда не ходили при необходимости смешить шашку
            klik[0][0] = x
            klik[0][1] = y
            moved_checkers = y*10+x
            go_error = 0
        elif ((klik[0][0] != -1) and (area_monitor[y][x] != 9) and (area_monitor[y][x] == 0)): # если все-таки ходим
            flag = 0
            i = 0
            l = 0
            g = 0
            gg = 0
            while (klik[gg][0]!=-1 and gg<len(klik)):
                gg = gg + 1
            klik[gg][0] = x
            klik[gg][1] = y
            gg = gg + 1
            ch = 0
            eat = 0
            while (l<len(go_operation) and flag==0):
                i = 0
                g = 0
                flag = 1
                while (i<len(go_operation[l]) and g<gg): #  and flag==0
                    if (go_operation[l][i]>2000):
                        i = i + 1
                        eat = 1
                    if (go_operation[l][i]%100!=klik[g][1]*10+klik[g][0]):
                        flag = 0
                    else:
                        ch = int(go_operation[l][i]/100)%100
                    g = g + 1
                    i = i + 1
                l = l + 1
            l = l - 1
            if (flag==1):
                #print("yes")
                move(klik[gg-2][1],klik[gg-2][0],klik[gg-1][1],klik[gg-1][0],ch)
                #klik.append([-1,-1])
                if (i<len(go_operation[l])): # продолжаем ходить
                    moved_checkers = klik[gg-1][1]*10+klik[gg-1][0]
                    klik.append([-1,-1])
                else: # конец хода, смена цвета
                    #print("--",go_operation[l])
                    history.append(go_operation[l])
                    moved_checkers = -1
                    klik.clear()
                    klik = [[-1,-1],[-1,-1]]
                    if (go_color == 1):
                        go_color = 2
                    else:
                        go_color = 1
                    clear_corpse()
                    generator_move(area_monitor, go_color)
                    print_go_operation()
                go_error = 0
            else:
                #moved_checkers = -1
                klik[gg-1][0] = -1
                klik[gg-1][1] = -1
                if (eat==1):
                    go_error = 1
                else:
                    go_error = 2
        else:
            go_error = 2
        if (no_wins(go_color)==0):
            if (go_color==1):
                go_error = 12
            else:
                go_error = 11
            go_color = -1
            reboot_checkers()
            reboot_controller()
            out_window.update()
            print_history()
        reboot_checkers()
        reboot_controller()
        #wins(go_color)
        
    
    def click(event):
        global area_monitor
        global klik
        global klik_flag
        global go_color
        global go_error
        global control_move
        global control_add
        global control_edit
        global control_vs
        global control_back
        global area_zero
        global area_zero2
        global moved_checkers
        if (klik_flag==1):
            klik_flag = 0
            x = event.x
            y = event.y
            #area = area_monitor
            #print(x, y)
            if ((x >= ras/2) and (x <= ras/2*17) and (y >= ras/2) and (y <= ras/2*17)): 
                x = map(x, ras/2, ras/2*17, 0, 8)
                y = map(y, ras/2, ras/2*17, 0, 8)
                #print(x, y)
                if (control_edit==0):
                    if (control_vs==1 and go_color==2 or control_vs==2 and go_color==1 or control_vs==3): 
                        people_move(y,x)
                        if (control_vs==go_color or control_vs==4):
                            mozg()
                    else:
                        go_error = 3
                        reboot_controller()
                elif (area_monitor[y][x] != 9):
                    if (area_monitor[y][x]==0):
                        area_monitor[y][x] = control_add
                    elif (area_monitor[y][x]%10==control_add and area_monitor[y][x]/10<1):
                        area_monitor[y][x] = control_add + 10
                    elif (area_monitor[y][x]%10!=control_add or area_monitor[y][x]/10>1):
                        area_monitor[y][x] = 0
                    #reboot_monitor()
                    reboot_checkers()
            else:
                if (y>=ras*9.2 and y<=ras*9.8):
                    if (x>=ras*4 and x<=ras*5):
                        klik.clear()
                        klik = [[-1,-1],[-1,-1]]
                        moved_checkers = -1
                        go_error = 0
                        if (control_edit==1):
                            control_edit = 0
                            go_color = control_move
                            history.clear()
                            history.append(deepcopy(area_monitor))
                            generator_move(area_monitor, go_color)
                            print_go_operation()
                            if (go_color==control_vs or control_vs==4):
                                mozg()
                        else:
                            control_edit = 1
                            control_move = go_color
                            if (control_move==-1):
                                control_move = 1
                            go_color = -1
                        #reboot_monitor()
                        reboot_checkers()
                        #reboot_controller()
                    elif (control_edit==1):
                        if (x>=ras*0.2 and x<=ras*0.8):
                            area_monitor = deepcopy(area_zero2)
                            reboot_checkers()
                        if (x>=ras*1.0 and x<=ras*2.2):
                            if (control_add==1):
                                control_add=2
                            else:
                                control_add=1
                        if (x>=ras*2.4 and x<=ras*3.8):
                            if (control_move==1):
                                control_move=2
                            else:
                                control_move=1
                        if (x>=ras*5.2 and x<=ras*8.0):
                            if (control_vs<=2):
                                control_vs=control_vs+1
                            else:
                                control_vs=1
                        if (x>=ras*8.2 and x<=ras*8.8):
                            area_monitor = deepcopy(area_zero)
                            control_move = 1
                            #reboot_monitor()
                            reboot_checkers()
                        #reboot_monitor()
                        #reboot_controller()
                    else:
                        if (x>=ras*0.2 and x<=ras*0.8 and control_back==1):
                            #print("==",klik)
                            if (klik[1][0]==-1):
                                moved_checkers = -1
                                #print("go back")
                                mov1 = deepcopy(history[len(history)-1])
                                del history[len(history)-1]
                                i = len(mov1)-2
                                while (i>=0):
                                    into = mov1[i+1]
                                    y0 = int(into/10)%10
                                    x0 = into%10
                                    ea = 0
                                    if (mov1[i]>2000):
                                        i = i - 1
                                        ea = 1
                                    into = mov1[i]
                                    y1 = int(into/10)%10
                                    x1 = into%10
                                    ch = int(into/100)%100
                                    sleep(0.2)
                                    move(y0, x0, y1, x1, ch)
                                    if (ea==1):
                                        into = mov1[i+1]
                                        ye = int(into/10)%10
                                        xe = into%10
                                        che = int(into/100)%100
                                        area_monitor[ye][xe] = che
                                    i = i - 1
                                if (control_vs==3):
                                    if (go_color==1):
                                        go_color = 2
                                    elif (go_color==2):
                                        go_color = 1
                                    elif (go_error==11 or go_error==12):
                                        go_color = go_error%10
                                else:
                                    mov1 = deepcopy(history[len(history)-1])
                                    del history[len(history)-1]
                                    i = len(mov1)-2
                                    while (i>=0):
                                        into = mov1[i+1]
                                        y0 = int(into/10)%10
                                        x0 = into%10
                                        ea = 0
                                        if (mov1[i]>2000):
                                            i = i - 1
                                            ea = 1
                                        into = mov1[i]
                                        y1 = int(into/10)%10
                                        x1 = into%10
                                        ch = int(into/100)%100
                                        sleep(0.2)
                                        move(y0, x0, y1, x1, ch)
                                        if (ea==1):
                                            into = mov1[i+1]
                                            ye = int(into/10)%10
                                            xe = into%10
                                            che = int(into/100)%100
                                            area_monitor[ye][xe] = che
                                        i = i - 1
                                    if (go_color==-1):
                                        if (control_vs==1):
                                            go_color = 2
                                        else:
                                            go_color = 1
                                go_error = 0
                                #print(history[len(history)-1][0])
                                #go_color = int(history[len(history)-1][0]/100)%10
                                reboot_checkers()
                                generator_move(area_monitor,go_color)
                                print_go_operation()
                            else:
                                moved_checkers = -1
                                flag = 0
                                i = 0
                                l = 0
                                g = 0
                                gg = 0
                                while (klik[gg][0]!=-1 and gg<len(klik)):
                                    gg = gg + 1
                                ch = 0
                                eat = 0
                                while (l<len(go_operation) and flag==0):
                                    i = 0
                                    g = 0
                                    flag = 1
                                    while (i<len(go_operation[l]) and g<gg): #  and flag==0
                                        if (go_operation[l][i]>2000):
                                            i = i + 1
                                            eat = 1
                                        if (go_operation[l][i]%100!=klik[g][1]*10+klik[g][0]):
                                            flag = 0
                                        else:
                                            ch = int(go_operation[l][i]/100)%100
                                        g = g + 1
                                        i = i + 1
                                    l = l + 1
                                l = l - 1
                                mov1 = []
                                iii = 0
                                while (iii<i):
                                    mov1.append(go_operation[l][iii])
                                    iii = iii + 1
                                i = len(mov1)-2
                                while (i>=0):
                                    into = mov1[i+1]
                                    y0 = int(into/10)%10
                                    x0 = into%10
                                    ea = 0
                                    if (mov1[i]>2000):
                                        i = i - 1
                                        ea = 1
                                    into = mov1[i]
                                    y1 = int(into/10)%10
                                    x1 = into%10
                                    ch = int(into/100)%100
                                    sleep(0.2)
                                    move(y0, x0, y1, x1, ch)
                                    if (ea==1):
                                        into = mov1[i+1]
                                        ye = int(into/10)%10
                                        xe = into%10
                                        che = int(into/100)%100
                                        area_monitor[ye][xe] = che
                                    i = i - 1
                                go_error = 0
                                klik.clear()
                                klik = [[-1,-1],[-1,-1]]
                                reboot_checkers()
                                generator_move(area_monitor,go_color)
                                print_go_operation()
                        if (x>=ras*1.4 and x<=ras*3.0 and control_back==1 and 0):
                            sdfghkl=0
                            print("go forward")
            if ((len(history)>1 and control_vs==3 or len(history)>2 and control_vs!=4) and control_edit==0 and go_error<10):
                control_back = 1
            else:
                control_back = 0
            reboot_controller()
            klik_flag = 1
                    
    #reboot_monitor()
    reboot_checkers()
    reboot_controller()
    generator_move(area_monitor, go_color)
    print_go_operation()
    history.append(deepcopy(area_monitor))
    if (control_vs==go_color or control_vs==4):
        mozg()
        reboot_checkers()
        reboot_controller()
        generator_move(area_monitor, go_color)
        print_go_operation()
    
    canvas.bind("<Button-1>", click)

    canvas.pack()
    out_window.mainloop()
    #in_window.mainloop()

qwerty()
