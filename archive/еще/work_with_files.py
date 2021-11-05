from copy import deepcopy 
import os.path  #  <===========================================

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

debuts = []
zadania = []
flag_file = 0

def read_file():
    global debuts
    global zadania
    global flag_file
    debuts.clear()
    zadania.clear()
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
            # name
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
                zadania.append(mas)
            else:
                debuts.append(mas)
            #print(mas)
            #print()
            
            S = file.readline()
        file.close()
    else:
        flag_file = 0

read_file()
print(debuts)
print()
print(zadania)

