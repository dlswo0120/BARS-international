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
        [9, 0, 9, 0, 9, 0, 9, 0],
        [0, 9, 0, 9, 0, 9, 0, 9],
        [9, 0, 9, 0, 9, 0, 9, 0],
        [0, 9, 0, 9, 0, 9, 0, 9],
        [9, 1, 9, 1, 9, 1, 9, 1],
        [1, 9, 1, 9, 1, 9, 1, 9]]

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

    def go_controll():
        global area
        global klik
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
            while (y <= 7): # proverka na vozmognost siest shaskami
                if (area[y][x] != 9):
                    if (y-2>=0 and x-2>=0 and flag == 0):
                        if (area[y][x]%10!=area[y-1][x-1]%10 and area[y][x]!=0 and area[y-1][x-1]!=0 and area[y-2][x-2]==0):
                            eat = 1
                            if (y0-2==y1 and x0-2==x1 and y==y0 and x==x0):
                                flag = 1
                    if (y+2<=7 and x-2>=0 and flag == 0):
                        if (area[y][x]%10!=area[y+1][x-1]%10 and area[y][x]!=0 and area[y+1][x-1]!=0 and area[y+2][x-2]==0):
                            eat = 1
                            if (y0+2==y1 and x0-2==x1 and y==y0 and x==x0):
                                flag = 1
                    if (y-2>=0 and x+2<=7 and flag == 0):
                        if (area[y][x]%10!=area[y-1][x+1]%10 and area[y][x]!=0 and area[y-1][x+1]!=0 and area[y-2][x+2]==0):
                            eat = 1
                            if (y0-2==y1 and x0+2==x1 and y==y0 and x==x0):
                                flag = 1
                    if (y+2<=7 and x+2<=7 and flag == 0):
                        if (area[y][x]%10!=area[y+1][x+1]%10 and area[y][x]!=0 and area[y+1][x+1]!=0 and area[y+2][x+2]==0):
                            eat = 1
                            if (y0+2==y1 and x0+2==x1 and y==y0 and x==x0):
                                flag = 1
                x = x + 1
                if (x > 7):
                    x = 0
                    y = y + 1
            x = 0
            y = 0
            while (0): # proverka na vozmognost siest damkami 
                x = 0
            #===========================================
            if (eat == 0):
                #flag = 1
                if (area[y0][x0]/10 < 1): # not queen
                    if   (area[y0][x0]%10==1 and y0-1==y1 and (x0==x1-1 or x0==x1+1)):
                        flag = 1
                    elif (area[y0][x0]%10==2 and y0+1==y1 and (x0==x1-1 or x0==x1+1)):
                        flag = 1
                    else:
                        print("you can not commit this move")
                    #if (eat
                    #
                #else: # queen
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
        if ((abs(x0-x1)==abs(y0-y1) and abs(y0-y1)>=2)): # eat
            while (x1!=x0):
                area[y0][x0] = 0
                x0 = x0 + znak(x1-x0)
                y0 = y0 + znak(y1-y0)
                    
                
            
    #===================================================================================================================================================================================================

    reboot_checkers()
    
    def click(event):
        global area
        global klik
        x = event.x
        y = event.y
        #print(x, y)
        if ((x >= ras/2) and (x <= ras/2*17) and (y >= ras/2) and (y <= ras/2*17)): 
            x = map(x, ras/2, ras/2*17, 0, 8)
            y = map(y, ras/2, ras/2*17, 0, 8)
            print(x, y)
            if ((klik[0][0] == -1) and (area[y][x] != 9) and (area[y][x] != 0)): 
                klik[0][0] = x
                klik[0][1] = y
            elif ((klik[0][0] == x) and (klik[0][1] == y)):
                klik[0][0] = -1
                klik[0][1] = -1
            elif ((area[y][x] != 9) and (area[y][x] == 0)):
                klik[1][0] = x
                klik[1][1] = y 
                if (go_controll()):
                    #============================
                    q = area[ klik[0][1] ][ klik[0][0] ]
                    area[ klik[0][1] ][ klik[0][0] ] = 0
                    area[ klik[1][1] ][ klik[1][0] ] = q
                    #============================
                    eat_checkers()
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
                    klik[0][0] = -1
                    klik[0][1] = -1
                    klik[1][0] = -1
                    klik[1][1] = -1
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

        
        reboot_checkers()
            
            
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
