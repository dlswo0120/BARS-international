'''
this program writing Bakay Egor, Moscow, Russia, 2020
BARS_brain version: 1.0
download: https://yadi.sk/d/QsL3RJtT-QnlLA
tutorial: https://www.youtube.com/playlist?list=PL24VxeCr7LD1Z3Cm_VS4bLKthcGdkNWSD
rate app: https://docs.google.com/forms/d/e/1FAIpQLSfOLysTI8F9iPvoiu5R__bpcbtZvHo4up4pca1XKYu9sgEkxA/viewform

This script is part of the project "PROMETHEUS"
https://www.youtube.com/playlist?list=PL24VxeCr7LD3qzQenzNS4zYKe5VYeBOxw

# 9  - нельзя занимать - белая
# 0  - свободная черная клетка
# 1  - белая шашка
# 11 - белая дамка
# 2  - черная шашка
# 12 - черная дамка

area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                [2, 9, 2, 9, 2, 9, 2, 9],
                [9, 2, 9, 2, 9, 2, 9, 2],
                [0, 9, 0, 9, 0, 9, 0, 9],
                [9, 0, 9, 0, 9, 0, 9, 0],
                [1, 9, 1, 9, 1, 9, 1, 9],
                [9, 1, 9, 1, 9, 1, 9, 1],
                [1, 9, 1, 9, 1, 9, 1, 9]]

abcxy - BARS
'''

from random import * # x0 = randint(0, 100)
from copy import deepcopy 
import time
from time import sleep
from time import time
Time = int(time()*1000)

#print("$ import <checkers_BARS_brain>")

def BARS_brain_version(S=0):
    version = "2.0 beta"
    if (S==0):
        return version
    if (S==version):
        return 1
    else:
        print("<BARS_brain> have more version!!!")
        return 0
    
def generator_move(area_operation, go_color):
    area = deepcopy(area_operation)
    klik = [[-1,-1],
            [-1,-1]]
    go_operation = []
    count1 = 0
    
    def bumerang(go_operation, count1, y2, x2):
        
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

    def eating2(go_operation, count1, area1, y0, x0, y1, x1):
        klik = [[x0,y0],
                [x1,y1]]
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
        eating(go_operation, count1, area2, go_color, y1, x1)
    
    def eating(go_operation, count1, area_operation, go_color, y, x):
        #global count1
        #global go_operation
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
                    if (area[y][x]%10!=area[y-1][x-1]%10 and area[y-1][x-1]<100 and area[y][x]!=0 and area[y-1][x-1]!=0 and area[y-2][x-2]==0 and bumerang(go_operation, count1, y-2, x-2)):
                        eat = 1
                        a = 0
                        if (y==2 and go_color==1):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y-2)*10+(x-2))
                        eating2(go_operation, count1, area, y, x, y-2, x-2)
                if (y+2<=7 and x-2>=0):
                    if (area[y][x]%10!=area[y+1][x-1]%10 and area[y+1][x-1]<100 and area[y][x]!=0 and area[y+1][x-1]!=0 and area[y+2][x-2]==0 and bumerang(go_operation, count1, y+2, x-2)):
                        eat = 1
                        a = 0
                        if (y==5 and go_color==2):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y+2)*10+(x-2))
                        eating2(go_operation, count1, area, y, x, y+2, x-2)
                if (y-2>=0 and x+2<=7):
                    if (area[y][x]%10!=area[y-1][x+1]%10 and area[y-1][x+1]<100 and area[y][x]!=0 and area[y-1][x+1]!=0 and area[y-2][x+2]==0 and bumerang(go_operation, count1, y-2, x+2)):
                        eat = 1
                        a = 0
                        if (y==2 and go_color==1):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y-2)*10+(x+2))
                        eating2(go_operation, count1, area, y, x, y-2, x+2)
                if (y+2<=7 and x+2<=7):
                    if (area[y][x]%10!=area[y+1][x+1]%10 and area[y+1][x+1]<100 and area[y][x]!=0 and area[y+1][x+1]!=0 and area[y+2][x+2]==0 and bumerang(go_operation, count1, y+2, x+2)): 
                        eat = 1
                        a = 0
                        if (y==5 and go_color==2):
                            a = 1000 
                        go_operation[len(go_operation)-1].append(a+go_color*100+(y+2)*10+(x+2))
                        eating2(go_operation, count1, area, y, x, y+2, x+2)
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
                    if (go_color!=area[yd1-1][xd1-1]%10 and area[yd1-1][xd1-1]<100 and area[yd1-1][xd1-1]!=0 and area[yd1-2][xd1-2]==0 and bumerang(go_operation, count1, yd1-1, xd1-1)):
                        eat = 1
                        yd1 = yd1 - 2
                        xd1 = xd1 - 2
                        if (1):
                            i = 1
                            while (yd1>=0 and xd1>=0 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd1)*10+(xd1))
                                eating2(go_operation, count1, area, y, x, yd1, xd1)
                                #if (area[yd1][xd1]==0 and yd1==y1 and xd1==x1):
                                yd1 = yd1 - 1
                                xd1 = xd1 - 1
                                if (yd1>=0 and xd1>=0 and area[yd1][xd1]!=0):
                                    i = 0
                if (yd2+2<=7 and xd2-2>=0):
                    if (go_color!=area[yd2+1][xd2-1]%10 and area[yd2+1][xd2-1]<100 and area[yd2+1][xd2-1]!=0 and area[yd2+2][xd2-2]==0 and bumerang(go_operation, count1, yd2+1, xd2-1)):
                        eat = 1
                        yd2 = yd2 + 2
                        xd2 = xd2 - 2
                        if (1):
                            i = 1
                            while (yd2<=7 and xd2>=0 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd2)*10+(xd2))
                                eating2(go_operation, count1, area, y, x, yd2, xd2)
                                #if (area[yd2][xd2]==0 and yd2==y1 and xd2==x1):
                                yd2 = yd2 + 1
                                xd2 = xd2 - 1
                                if (yd2<=7 and xd2>=0 and area[yd2][xd2]!=0):
                                    i = 0
                if (yd3-2>=0 and xd3+2<=7):
                    if (go_color!=area[yd3-1][xd3+1]%10 and area[yd3-1][xd3+1]<100 and area[yd3-1][xd3+1]!=0 and area[yd3-2][xd3+2]==0 and bumerang(go_operation, count1, yd3-1, xd3+1)):
                        eat = 1
                        yd3 = yd3 - 2
                        xd3 = xd3 + 2
                        if (1):
                            i = 1
                            while (yd3>=0 and xd3<=7 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd3)*10+(xd3))
                                eating2(go_operation, count1, area, y, x, yd3, xd3)
                                #if (area[yd3][xd3]==0 and yd3==y1 and xd3==x1):
                                yd3 = yd3 - 1
                                xd3 = xd3 + 1
                                if (yd3>=0 and xd3<=7 and area[yd3][xd3]!=0):
                                    i = 0
                if (yd4+2<=7 and xd4+2<=7):
                    if (go_color!=area[yd4+1][xd4+1]%10 and area[yd4+1][xd4+1]<100 and area[yd4+1][xd4+1]!=0 and area[yd4+2][xd4+2]==0 and bumerang(go_operation, count1, yd4+1, xd4+1)):
                        eat = 1
                        yd4 = yd4 + 2
                        xd4 = xd4 + 2
                        if (1):
                            i = 1
                            while (yd4<=7 and xd4<=7 and i==1):
                                go_operation[len(go_operation)-1].append(1000+go_color*100+(yd4)*10+(xd4))
                                eating2(go_operation, count1, area, y, x, yd4, xd4)
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
        if (eating(go_operation, count1, area, go_color, y ,x)==1):
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
                            #print("selection error")
                            #print(i)
                            #print_mas(area)
                            #print_mas(go_operation)
                            i = i + 1
                    else:
                        i = i + 1
                else:
                    i = i + 1
    #print_go_operation()
    return go_operation

def going(area1, moving1):
    area = deepcopy(area1)
    moving = deepcopy(moving1)
    i = 0
    while (len(moving)>i+1):
        x0 = moving[i]%10
        y0 = int(moving[i]/10)%10
        i = i + 1
        if (moving[i]>5000):
            i = i + 1
        x1 = moving[i]%10
        y1 = int(moving[i]/10)%10
        c = int(moving[i]/100)
        while (x1!=x0):
            area[y0][x0] = 0
            x0 = x0 + znak(x1-x0)
            y0 = y0 + znak(y1-y0)
        area[y1][x1] = c
    return area

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

def more_color(go_color):
    if (go_color==1):
        return 2
    elif (go_color==2):
        return 1
    else:
        return 0

def print_mas(mas):
    i = 0
    while (i<len(mas)):
        print(mas[i])
        i = i + 1
    
def print_coo(yy,xx):
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
    
def estimate_area(go_color, area): # , go_color
    if (1): 
        x = 0
        y = 0
        e = 0
        z = 1
        i1 = 0
        i2 = 0
        if (go_color==2):
            z = -1
        while (y<=7):
            ko = 1.3 # коэффицент - на сколько хорошо, что шашака близка к концу поля (становлению дамкой)
            if (area[y][x]%10==go_color):
                i1 = 1
            if (area[y][x]%10==more_color(go_color)):
                i2 = 1
            if (area[y][x]==1):
                e = e + 200*z
                e = e + int((7-y)*(7-y)*(7-y)*z*ko)
            if (area[y][x]==11):
                e = e + 500*z
            if (area[y][x]==2):
                e = e - 200*z
                e = e - int(y*y*y*z*ko)
            if (area[y][x]==12):
                e = e - 500*z
            if (area[y][x]==11 and (x==7 and y==0 or x==6 and y==1 or x==5 and y==2 or x==4 and y==3 or x==3 and y==4 or x==2 and y==5 or x==1 and y==6 or x==0 and y==7)):
                e = e + 10*z
            if (area[y][x]==12 and (x==7 and y==0 or x==6 and y==1 or x==5 and y==2 or x==4 and y==3 or x==3 and y==4 or x==2 and y==5 or x==1 and y==6 or x==0 and y==7)):
                e = e - 10*z
            if (x<7):
                x = x + 1
            else:
                x = 0
                y = y + 1
        #e = e + len(go_operation)*5
        if (i2==0):
            e = 1000000
        if (i1==0):
            e = -1000000
    else:
        e = -1000000
    return e
    
class go_element(): # for drevo go
    def __init__(self, go=0, estimate=0, area=0, next_go=[]):
        self.go = go # ход, после которого случился этот момент
        self.estimate = estimate # оценка позиции после этого хода
        self.area = area # уже после хода go
        self.next_go = next_go # сюда кидаем новые go_element
    
#===================================================================================================================================================================================================
#===================================================================================================================================================================================================
#===================================================================================================================================================================================================
      
      
def BARS_mind(area_monitor, go_color, level_hard):
      
    def nostardamus_first_mod(area_monitor, go_color):
        go = []

        #def evklid(area, go_color, go_color1):
        #    return estimate_area(go_color, area)#e
        
        def helper(go, area1,H,go_color,go_color1):
            area = deepcopy(area1)
            #if (go_color1==2):
            go_operation = generator_move(area,more_color(go_color))
            go_operation_save = deepcopy(go_operation)
            if (len(go_operation)==0): # если в прошлый ход был заперт соперник
                if (H%2==1):
                    go[len(go)-1][len(go[len(go)-1])-1] = 1000000
                else:
                    go[len(go)-1][len(go[len(go)-1])-1] = -1000000
            else:
                e = len(go_operation)*5
                if (len(go_operation[0])>=3): # надо есть
                    e *= 10
                if (0):
                    if (H%2==1):
                        go[len(go)-1][len(go[len(go)-1])-1] -= e
                    else:
                        go[len(go)-1][len(go[len(go)-1])-1] += e
                i = 0
                while (len(go_operation_save)>i): #  and i<1
                    area2 = going(area, go_operation_save[i])
                    go[len(go)-1].append(go_operation_save[i])
                    go[len(go)-1].append(estimate_area(go_color, area2))
                    mas = deepcopy(go[len(go)-1])
                    if (int(len(go[len(go)-1])/2)<H and abs(go[len(go)-1][len(go[len(go)-1])-1])<999999):
                        helper(go, area2,H,more_color(go_color))
                    go.append(deepcopy(mas))
                    #if (abs(go[len(go)-1][len(go[len(go)-1])-1])<999999 or 1): # or 1
                    del go[len(go)-1][len(go[len(go)-1])-1]
                    del go[len(go)-1][len(go[len(go)-1])-1]
                    i = i + 1
                if (abs(go[len(go)-1][len(go[len(go)-1])-1])<999999 and 1):
                    del go[len(go)-1]
            
            
            
        go.clear()
        H = 2
        go.append(estimate_area(go_color, area_monitor)) # оценка в начале позиции 
        #generator_move(area_operation,go_color) # сделано в evklid
        go_operation = generator_move(area_monitor,go_color)
        go_operation_save = deepcopy(go_operation)
        i = 0
        timer = millis()
        while (i<len(go_operation_save)): # записываем возможные ходы в данный момент времени, и каждый раз вызываем рекрусивно просчет helper
            area_monitor1 = going(area_monitor, go_operation_save[i])
            go.append([go_operation_save[i],estimate_area(go_color, area_monitor1)])
            helper(go, area_monitor1,H,go_color,2)
            i = i + 1
        timer1 = millis()
        #print("--------")
        #print_mas(go)
        #print ("count:",len(go)-1)
        #print ("time:",(timer1-timer)/1000)
        #print("---------------------")
        # выбор наилучшего хода
        i = 1
        ii = -1000001
        while (i<len(go)):
            if (go[i][len(go[i])-1]>ii):
                ii = go[i][len(go[i])-1]
            i = i + 1
        #print(ii)
        i = 1
        while (i<len(go)):
            if (go[i][len(go[i])-1]<ii):
                del go[i]
            else:
                i = i + 1
        #print_mas(go)
        #print ("count:",len(go)-1)
        i = randint(1, len(go)-1)
        #print("variant: ", i)
        #print("---------------------")
        go_operation = deepcopy(go[i][0])
        return go_operation

    def nostardamus_ultra(area_monitor, go_color):

        max_go = 6 # на сколько ходов максимум просчитывать (все варианты)
        max_time = 10000 # millis - максимальное время расчета
        DEBUG = 1
        robot_color = go_color
        # https://habr.com/ru/post/146088/
        
        if __name__ == "__main__" or DEBUG:
            print("max_go:",max_go)
            print("max_time:",max_time)
        time = 0
        time1 = millis()
        
        def print_go(y, go): # вывести древо ходов go
            for i in range (y*3):
                print(end=' ')
            print(go.estimate,go.go)
            y+=1
            for i in range (len(go.next_go)):
                print_go(y,go.next_go[i])
            y-=1                
                
        def counter_go (go): # посчитать кол-во вариантов ходов в древе go
            I = 0
            if (go.next_go==[]):
                return 1
            for i in range (len(go.next_go)):
                I+=counter_go(go.next_go[i])
            return I
        
        #II = 0

        def max_depth(go):
            I = 0
            if (go.next_go==[]):
                return 0
            for i in range (len(go.next_go)):
                I = max(max_depth(go.next_go[i])+1, I)
            return I

        def make_drevo(go, go_color, start_go_color): # добавить древу ходов go еще один уровень (просчитать еще на один ход), но если время выйдет, прерваться
            flag = 1
            if (time+max_time<=millis()):
                flag = 0
            else:
                if (go.next_go==[]):
                    area = deepcopy(go.area)
                    go_operation = deepcopy(generator_move(area, go_color))
                    for i in range(len(go_operation)):
                        area1 = going(area, go_operation[i])
                        go.next_go.append(go_element(go_operation[i], 0, area1, [])) # estimate_area(start_go_color,area1) => 0
                else:
                    go_color1 = more_color(go_color)
                    for i in range (len(go.next_go)):
                        if (flag):
                            flag = make_drevo(go.next_go[i], go_color1, start_go_color)
            return flag

        def add_weight(go, II=0):
            koeficent = 1
            II+=1
            #print(II)
            if (go.next_go!=[]): # т.е. это НЕ последний элемент продумывания
                i = 0
                if (II%2==0): # ход противника
                    go.estimate -= len(go.next_go)*koeficent
                else: # мой ход
                    go.estimate += len(go.next_go)*koeficent
                for i in range(len(go.next_go)):
                    add_weight(go.next_go[i],II)
            II-=1

        def minimax(go, II=0, my_move=[]):
            II+=1
            my_return = 0
            #print(II)
            if (go.next_go==[]): # т.е. это последний элемент продумывания
                #my_return = go.estimate
                if (go.estimate<abs(100000)):
                    my_return = estimate_area(robot_color,go.area)
                else:
                    my_return = go.estimate 
            else:
                player = 1 # кто ходит? (я)
                best_go = -999999
                if (II%2==0): # в этом случае ходит противник
                    player = 0
                    best_go = 999999
                for i in range (len(go.next_go)):
                    if (player): best_go = max(best_go,minimax(go.next_go[i], II, my_move))
                    else: best_go = min(best_go,minimax(go.next_go[i], II, my_move))
                my_return = best_go
            II-=1
            # выбор хода
            if (II==1):
                #print(go.go, my_return)
                my_move.append([go.go, my_return])
            if (II==0):
                weight = []
                move = []
                for i in range(len(my_move)):
                    weight.append(my_move[i][1])
                    move.append(my_move[i][0])
                best_move = []
                for i in range(len(my_move)):
                    if (weight[i]==max(weight)):
                        best_move.append(move[i])
                my_return = best_move[randint(0, len(best_move)-1)]
                #print("minimax",my_return)
            return my_return

        def deepening_drevo(go, II=0, old_eat=0): # добавлять древу ходов go ходы, пока возможно есть, но если время выйдет, прерваться
            #flag = 1
            II+=1
            if (time+max_time<=millis()): # если время вышло, прерываемся
                pass
            else:  # время не вышло
                if (go.next_go==[] and go.go!=0 and 1): # дошли до конца ветки в go
                    #if (old_eat*0+len(go.go)-2>0): # есть смысл что-либо просчитывать
                    #if (1):
                    area = deepcopy(go.area)
                    go_color = more_color(int(go.go[0]/100)%10)
                    go_operation = deepcopy(generator_move(area, go_color))
                    if (go_operation!=[]):
                        if (len(go_operation[0])>2): # есть смысл что-либо просчитывать
                            for i in range(len(go_operation)):
                                area1 = going(area, go_operation[i])
                                go.next_go.append(go_element(go_operation[i], 0, area1, [])) # estimate_area(start_go_color,area1) => 0
                                eat = 0
                                if (len(go.go)>2): eat = 1
                                deepening_drevo(go.next_go[i], II, eat)
                    else:
                        go.estimate = 999999
                        if (II%2==0): # в этом случае ходит противник
                            go.estimate *= -1
                        
                else: # не дошли до конца ветки в go => идем в конец
                    #go_color1 = more_color(go_color)
                    for i in range (len(go.next_go)):
                        if (__name__ == "__main__" or DEBUG) and II==1:
                            print(".", end='')
                        eat = 0
                        if (go.go!=0):
                            if (len(go.go)>2): eat = 1
                        deepening_drevo(go.next_go[i], II, eat)
            II-=1
            #return flag

        def minimax_2(go, II=0, alpha=-999999,beta=999999):
            II+=1
            best_go = 0
            if (II==1):
                best_go_mas = []
            test = 0
            flag = 0
            if (max_go<II):
                flag = 1
                
                #if (go.estimate==0): best_go = estimate_area(robot_color,go.area)
                #else: best_go = go.estimate
            #else:
            if (1):
                area = deepcopy(go.area)
                go_color = robot_color
                if (II%2==0): # в этом случае ходит противник
                    go_color = more_color(robot_color)
                go_operation = deepcopy(generator_move(area, go_color))
                flag_1 = 1
                if (flag and len(go_operation)>0):
                    if (len(go_operation[0])<3):
                        flag_1 = 0
                    flag_1 = 0
                if (len(go_operation)>0 and flag_1):
                    for i in range(len(go_operation)):
                        area1 = going(area, go_operation[i])
                        go.next_go.append(go_element(go_operation[i], 0, area1, [])) # estimate_area(start_go_color,area1) => 0
                        test = minimax_2(go.next_go[i], II, alpha,beta)
                        if (test>best_go):
                            best_go = test
                            if (II==1):
                                best_go_mas.clear()
                                best_go_mas.append(go_operation[i])
                        elif (test==best_go and II==1):
                            best_go_mas.append(go_operation[i])
                        # alpha beta
                        if (II%2==0):
                            alpha = max(alpha,test)
                        else:
                            beta = min(beta,test)
                        if (beta<alpha):
                            break
                        if (__name__ == "__main__" or DEBUG) and II==1:
                            print(".", end='')
                elif (flag_1):
                    best_go = 999999
                    if (II%2==0): # в этом случае ходит противник
                        best_go *= -1
                else: # flag_1 == 0
                    best_go = estimate_area(robot_color,go.area)
            II-=1
            if (II==0): best_go = best_go_mas[randint(0, len(best_go_mas)-1)]
            return best_go
        
        #go = [0] # 
        #print(estimate_area(go_color, area_monitor))
        #go = go_element(go=0, estimate=0, area=0, next_go=[])
        go = go_element(0, estimate_area(go_color,area_monitor), area_monitor, [])
        #go_color = more_color(go_color)

        go_operation = deepcopy(generator_move(area_monitor, go_color))
        if (len(go_operation)==0):
            print("BARS_brain: game over")
            return 0
        if (len(go_operation)==1):
            if __name__ == "__main__" or DEBUG:
                print("one option in <go_operation>")
                print()
            return go_operation[0]
        
        '''
        time += millis()
        my_go = minimax_2(go)
        print("time:", (millis()-time)/1000)
        print("counter_go:",counter_go(go))
        print("max depth:",max_depth(go))
        return my_go
        '''
        if __name__ == "__main__" or DEBUG:
            print("make drevo - ", end='')
        time += millis() # засекаем время
        flag = 0 # 0 - последний просчитываемый ход просчитан полностью, 1 - не полностью
        '''
        for i in range (max_go): # просчет ходов (каждый вызов - просчет на один ход вперед)
            flag = make_drevo(go, go_color, go_color)
            if (__name__ == "__main__" or DEBUG) and flag:
                print(".", end='')
        if __name__ == "__main__" or DEBUG:
            print(" - OK")
            print("deepening drevo - ", end='')
        deepening_drevo(go)
        '''
        best_go = minimax_2(go)
        #flag_1 = 0
        #while (flag_1):
        #    flag_1 = deepening_drevo(go)
        #    if (__name__ == "__main__" or DEBUG) and flag_1:
        #        print(".", end='')
        time2 = millis()
        if __name__ == "__main__" or DEBUG:
            print(" - OK")
            if (flag==1): print("the last move is fully calculated")
            else: print("the last move is NOT FULLY calculated")
            print("counter_go:",counter_go(go))
            print("time_operating:", (time2-time1)/1000)
            print("max depth:",max_depth(go))
            print()
            #print(" OK") # , end=''
            #print("counter_go:",counter_go(go))
            #print("time_operating:", (time3-time2)/1000)
            #print("common_time_operating:", (time3-time1)/1000)
            #print("delta", delta)
            #print("> answer:")
            
        #add_weight(go) # добавление "весов" - баллов за количество возможных ходов
        go_save = deepcopy(go) # в этот момент двево go составленно
        #time3 = millis()
        #print_go(0, go)
        #print(go.next_go[0].go,int(go.next_go[0].go[0]/100)%10)
        
        #return minimax(go)
        return best_go
        

        # выбор хода (из оставшихся в древе go)
        if (len(go.next_go)>0):
            go_operation = []
            for i in range (len(go.next_go)):
                go_operation.append(go.next_go[i].go)
            l = randint(0, len(go_operation)-1)
            return go_operation[l]
        else:
            if __name__ == "__main__" or DEBUG:
                print("nostardamus_first_mod")
            return nostardamus_first_mod(area_monitor, go_color)


    if (level_hard==0):
        go_operation = deepcopy(generator_move(area_monitor, go_color))
        l = randint(0, len(go_operation)-1)
        return go_operation[l] 
    elif (level_hard==1):
        return nostardamus_first_mod(area_monitor, go_color)
    else:
        return nostardamus_ultra(area_monitor, go_color)
    


def test():
    level_hard = 2
    print("level_hard:",level_hard)
    print("===> test 1:")
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                    [2, 9, 2, 9, 2, 9, 2, 9],
                    [9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [1, 9, 1, 9, 1, 9, 1, 9],
                    [9, 1, 9, 1, 9, 1, 9, 1],    
                    [1, 9, 1, 9, 1, 9, 1, 9]]    
    print(BARS_mind(area_monitor, 1, level_hard),"<")
    print("===> test 2:")
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                    [2, 9, 2, 9, 2, 9, 2, 9],
                    [9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 2, 9, 0, 9, 0],
                    [1, 9, 1, 9, 1, 9, 1, 9],
                    [9, 1, 9, 1, 9, 1, 9, 1],    
                    [1, 9, 1, 9, 1, 9, 1, 9]]
    print(BARS_mind(area_monitor, 1, level_hard),"<")
    print("===> successful test")

def test0():
    level_hard = 2
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                    [2, 9, 2, 9, 2, 9, 2, 9],
                    [9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [1, 9, 1, 9, 1, 9, 1, 9],
                    [9, 1, 9, 1, 9, 1, 9, 1],    
                    [1, 9, 1, 9, 1, 9, 1, 9]]
    #t = millis()
    # test for this position: 
    # I  time    count 
    # 1  0.039   7
    # 2  0.159   49
    # 3  0.46    302
    # 4  2.234   1469
    # 5  10.898  7482
    # 6  56.564  37986
    # 7  285.155 190146
    print(BARS_mind(area_monitor, 1, level_hard),"<")
    #print("time:", (millis()-t)/1000)
    print("===> successful test")

def test2():
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 0, 9, 0, 9, 2, 9, 0],
                    [0, 9, 0, 9, 2, 9, 0, 9],
                    [9, 2, 9, 2, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 1, 9, 0, 9, 0],
                    [1, 9, 1, 9, 0, 9, 0, 9],
                    [9, 1, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9]]   
    print(BARS_mind(area_monitor, 1, level_hard),"<")
    print("===> successful test")

def test3():
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 0, 9, 0, 9, 0, 9, 11],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 2, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 12],
                    [0, 9, 0, 9, 2, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9]]   
    print(BARS_mind(area_monitor, 2, level_hard))
    print("===> successful test")

def test4(): # game over
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9]]   
    print(BARS_mind(area_monitor, 2, level_hard))
    print("===> successful test")

def test5():
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 2, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [1, 9, 1, 9, 1, 9, 1, 9]]   
    print(BARS_mind(area_monitor, 2, level_hard))
    print("===> successful test")

def test6():
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 2, 9, 2, 9, 0, 9, 2],
                    [2, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 11, 9, 2, 9, 0],
                    [2, 9, 0, 9, 0, 9, 0, 9],
                    [9, 1, 9, 1, 9, 1, 9, 0],
                    [1, 9, 1, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [1, 9, 1, 9, 1, 9, 1, 9]]   
    print(BARS_mind(area_monitor, 2, level_hard))
    print("===> successful test")

def test7():
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 2, 9, 0, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 2, 9, 2, 9, 0, 9],
                    [9, 1, 9, 2, 9, 0, 9, 0],
                    [1, 9, 0, 9, 2, 9, 1, 9],
                    [9, 1, 9, 0, 9, 0, 9, 0],
                    [1, 9, 1, 9, 0, 9, 1, 9]]   
    print(BARS_mind(area_monitor, 2, level_hard))
    print("===> successful test")

def test8():
    level_hard = 3
    print("level_hard:",level_hard)
    #print("===> test 1:")
    area_monitor = [[9, 2, 9, 2, 9, 2, 9, 2],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 1, 9, 0, 9, 0],
                    [2, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 2],
                    [1, 9, 0, 9, 1, 9, 0, 9],
                    [9, 1, 9, 0, 9, 0, 9, 0],
                    [1, 9, 0, 9, 1, 9, 0, 9]]   
    print(BARS_mind(area_monitor, 2, level_hard))
    print("===> successful test")

 

'''
    area_monitor = [[9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9],
                    [9, 0, 9, 0, 9, 0, 9, 0],
                    [0, 9, 0, 9, 0, 9, 0, 9]]

'''

if __name__ == "__main__":
    test0()
    #test3()
    #test6()

