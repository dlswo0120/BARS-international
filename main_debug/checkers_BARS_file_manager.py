from copy import deepcopy 
from time import time
Time = int(time()*1000)
import os.path # для определения наличия файла
import datetime

def BARS_file_manager_version(S=0):
    version = "1.0"
    if (S==0):
        return version
    if (S==version):
        return 1
    else:
        print("<BARS_file_manager> have more version!!!")
        return 0

class my_file():
    
    def __init__(self, name):
        self.debuts = []
        self.zadania = []
        self.NAME = name
        
    def read(self):
        
        def num(a):
            if   (a=='0'):
                return 0
            elif (a=='1'):
                return 1
            elif (a=='2'):
                return 2
            elif (a=='3'):
                return 3
            elif (a=='4'):
                return 4
            elif (a=='5'):
                return 5
            elif (a=='6'):
                return 6
            elif (a=='7'):
                return 7
            elif (a=='8'):
                return 8
            elif (a=='9'):
                return 9
            else:
                return -1
        
        self.debuts.clear()
        self.zadania.clear()
        self.debuts.append([])
        self.zadania.append([])
        file = "BARS_tasks.txt"
        if (os.path.exists(file)):
            flag_file = 1
            file = open('BARS_tasks.txt')
            #S = file.read()
            #print(S)
            #print(line, end='')
            S = file.readline() # пропускаем первую строчку
            S = file.readline()
            while (len(S)>100):
                #print(S)
                mas = [0, [[],[],[],[],[],[],[],[]]]
                # self.NAME
                i = 0
                while (S[i]!='|'):
                    i += 1
                i += 1
                if (S[i]==' '):
                    i += 1
                mas1 = []
                while (S[i]!='|'):
                    mas1.append(S[i])
                    i += 1
                if (mas1[len(mas1)-1]==' '):
                    del mas1[len(mas1)-1]
                mas[0] = ''.join(mas1)
                #area
                ii = 0
                x = 0
                y = 0
                rez = 0
                while (ii<64):
                    while (num(S[i])==-1):
                        if (num(S[i+1])!=-1):
                            ii += 1
                        i += 1
                    while (num(S[i])!=-1):
                        rez = rez*10 + num(S[i])
                        i += 1
                    mas[1][int(ii/8-0.00001)].append(rez)
                    rez = 0
                # protocol
                while (i<len(S)-1 and S[i]!='|'):
                    i += 1
                if (i<len(S)-5): # если он есть
                    mas.append([])
                    #print(i, S[i], S[i+1])
                    while (i<len(S)-5 and 1):
                        mas[2].append([])
                        i += 1
                        while (S[i]!='|'):            
                            rez = 0
                            while (num(S[i])==-1 and S[i]!='|'):
                                i += 1
                            while (num(S[i])!=-1 and S[i]!='|'):
                                rez = rez*10 + num(S[i])
                                i += 1
                            if (rez>0):
                                mas[2][len(mas[2])-1].append(rez)
                            while (num(S[i])==-1 and S[i]!='|'):
                                i += 1
                    self.zadania.append(mas)
                else:
                    self.debuts.append(mas)
                #print(mas)
                #print()
                
                S = file.readline()
            file.close()
        else:
            flag_file = 0
        return self.debuts, self.zadania

    def write(self, history, control_vs):
        
        def num(a):
            if   (a=='0'):
                return 0
            elif (a=='1'):
                return 1
            elif (a=='2'):
                return 2
            elif (a=='3'):
                return 3
            elif (a=='4'):
                return 4
            elif (a=='5'):
                return 5
            elif (a=='6'):
                return 6
            elif (a=='7'):
                return 7
            elif (a=='8'):
                return 8
            elif (a=='9'):
                return 9
            else:
                return -1

        def print_coo(yy,xx):
            if  (xx==0):
                file.write("a")
            elif(xx==1):
                file.write("b")
            elif(xx==2):
                file.write("c")
            elif(xx==3):
                file.write("d")
            elif(xx==4):
                file.write("e")
            elif(xx==5):
                file.write("f")
            elif(xx==6):
                file.write("g")
            elif(xx==7):
                file.write("h")
            else:
                print("error")
            file.write(str(-yy+8))

        def print_field(ch, area):
            i = 0
            x = 0
            y = 0
            while (y<=7):
                if (area[y][x]==ch):
                    if (i==0):
                        if (ch==1):
                            file.write("белые шашки:\n")
                        if (ch==2):
                            file.write("черные шашки:\n")
                        if (ch==11):
                            file.write("белые дамки:\n")
                        if (ch==12):
                            file.write("черные дамки:\n")
                    if (i==100):  # для того, чтобы выводить в столбик по 5 значений
                        file.write("\n")
                    print_coo(y,x)
                    file.write(" ")
                    i = i + 1
                if (x<7):
                    x = x + 1
                else:
                    y = y + 1
                    x = 0
            if(i>0):
                file.write("\n")
        
        file = "BARS_protocol.txt"
        if (os.path.exists(file)==0):
            file = open("BARS_protocol.txt", 'w')
            file.close()
        file = open("BARS_protocol.txt", 'r+')
        len(file.readlines())
        file.write("\n")
        file.write("\n")
        now = datetime.datetime.now()
        str(now)
        file.write(now.strftime("%d-%m-%Y %H:%M"))
        file.write("\n")
        #file.write("Протокол составлен программой BARS 5.0\n") # <========= поменяй версию!!!
        file.write(str("Протокол составлен программой " + self.NAME + "\n"))
        #
        file.write("режим игры: ")
        if (control_vs==1):
            file.write("робот-человек")
        if (control_vs==2):
            file.write("человек-робот")
        if (control_vs==3):
            file.write("человек-человек")
        if (control_vs==4):
            file.write("робот-робот")
        file.write("\n")
        #
        file.write("Начальная позиция шашек:\n")
        area = deepcopy(history[0])
        print_field(1,  area)
        print_field(11, area)
        print_field(2,  area)
        print_field(12, area)
        #
        i = 1
        if (len(history)>1):
            file.write("Протокол:\n")
            while (i < len(history)):
                file.write(str(int(i/2)+1))
                file.write(" ")
                if (int(history[i][0]/100)%10==1):
                    y = int(history[i][0]/10)%10
                    x = history[i][0]%10
                    print_coo(y,x)
                    u = len(history[i])
                    if (u>2):
                        file.write(":")
                    else:
                        file.write("-")
                    y = int(history[i][u-1]/10)%10
                    x = history[i][u-1]%10
                    print_coo(y,x)
                    i = i + 1
                else:
                    file.write(".....")
                file.write(" ")
                if (i<len(history)):
                    if (int(history[i][0]/100)%10==2):
                        y = int(history[i][0]/10)%10
                        x = history[i][0]%10
                        print_coo(y,x)
                        u = len(history[i])
                        if (u>2):
                            file.write(":")
                        else:
                            file.write("-")
                        y = int(history[i][u-1]/10)%10
                        x = history[i][u-1]%10
                        print_coo(y,x)
                    else:
                       file.write(".....") 
                else:
                    file.write(".....")
                file.write("\n")
                i = i + 1
        #
        file.write("Для создания заданий (не забудьте изменить имя): \n")
        S = str(deepcopy(history))
        #print(S)
        i = 0
        f = 0
        #print("| self.NAME | ", end='')
        file.write("| name | ")
        while (f<64): # i<len(S)
            if (num(S[i])!=-1):
                file.write(S[i])
                if (num(S[i+1])==-1):
                    f += 1
                    file.write(" ")
            i += 1
        file.write(" | ")
        while (i<len(S)-5): # есть протокол 
            while (S[i]!='['):
                i += 1
            i += 1
            while (S[i]!=']'):
                while (num(S[i])!=-1):
                    file.write(S[i])
                    i += 1
                file.write(" ")
                while (num(S[i])==-1 and S[i]!=']'):
                    i += 1
            file.write("| ")
        file.write("\n")
        #file.write("------------------------------------\n")
        file.close()

if __name__ == "__main__":
    file = my_file("test")
    a,b=file.read() # 
    # print_file()
    file.write([[[9, 2, 9, 2, 9, 2, 9, 2], [2, 9, 2, 9, 2, 9, 2, 9], [9, 0, 9, 0, 9, 2, 9, 2], [2, 9, 1, 9, 0, 9, 0, 9], [9, 0, 9, 0, 9, 0, 9, 0], [0, 9, 0, 9, 1, 9, 1, 9], [9, 1, 9, 1, 9, 1, 9, 1], [1, 9, 1, 9, 1, 9, 1, 9]]], 3)
    #print(a)
    #print(b)
