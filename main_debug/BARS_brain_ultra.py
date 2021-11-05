'''
this program writing Bakay Egor, Moscow, Russia, 2020
download: https://yadi.sk/d/QsL3RJtT-QnlLA
tutorial: https://www.youtube.com/playlist?list=PL24VxeCr7LD1Z3Cm_VS4bLKthcGdkNWSD
rate app: https://docs.google.com/forms/d/e/1FAIpQLSfOLysTI8F9iPvoiu5R__bpcbtZvHo4up4pca1XKYu9sgEkxA/viewform

This script is part of the project "PROMETHEUS"
https://www.youtube.com/playlist?list=PL24VxeCr7LD3qzQenzNS4zYKe5VYeBOxw
'''

#print("$ import <BARS_brain>")

class BARS_brain():
    
    def version(self=0, S=0):
        if (isinstance(self, float) or isinstance(self, str)): S = str(self)
        elif (S!=0): S = str(S)
        version = "1.0"
        #print(S)
        if (S==0):
            return version
        if (S==version):
            return 1
        else:
            print("<BARS_brain> have more version!!!")
            return 0
        
    def __init__(self, mode):
        self.mode = mode
        
    def plan_move(self, area, go_color):
        if (self.mode=='checkers'): return 0
        #if (self.mode=='chess'): return 0
        #if (self.mode=='backgammon'): return 0
        print("ERROR: <BARS_brain> don't have this game mode")
        return 0
    
    def generator_move(self, area, go_color):
        if (self.mode=='checkers'): return 0
        #if (self.mode=='chess'): return 0
        #if (self.mode=='backgammon'): return 0
        print("ERROR: <BARS_brain> don't have this game mode")
        return 0
    
    def estimate_area(self, area, go_color):
        if (self.mode=='checkers'): return 0
        #if (self.mode=='chess'): return 0
        #if (self.mode=='backgammon'): return 0
        print("ERROR: <BARS_brain> don't have this game mode")
        return 0
  
    

