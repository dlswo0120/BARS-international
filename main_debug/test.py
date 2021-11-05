#from checkers_BARS_v_5_1 import *

class D():
    def __init__(self):
        pass


T = []

mas = []
mas.append(4)
mas.append(T)
mas.append(D)

for i in range(len(mas)):
    if isinstance(mas[i], list):
        print("int")
    else:
        print("don't int")
    #print(mas[i].type())
