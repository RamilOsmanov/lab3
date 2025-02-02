class Str:
    
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())


str_obj = Str()
str_obj.getString()
str_obj.printString() 
