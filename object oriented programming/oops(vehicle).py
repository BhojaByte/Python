class vehicle:
    def __init__(self,i,ms,ia):
        self.__id = i #self.__id = i as string
        self.__maxspeed = ms #self.__maxspeed = ms as Integer
        self.__increaseamount = ia #self.__increaseamount = ia as Integer
        self.__currentspeed = 0 #current speed is initialised by zero
        self.__horizontalpostion = 0 #horizontal postion is initialised by zero 

    # Get methods

    def getcurrentspeed(self):
        return self.__currentspeed
    def getincreaseamount(self):
        return self.__increaseamount
    def getmaxspeed(self):
        return self.__maxspeed
    def gethorizontalposition(self):
        return self.__horizontalpostion
    
    # set methods
    
    def setcurrentspeed(self,cs):
        self.__currentspeed = cs
    def sethorizontalposition(self,hp):
        self.__horizontalpostion = hp
    
    ##

    def Increasespeed(self):
        self.__currentspeed = self.__currentspeed + self.__increaseamount
        if self.__currentspeed < self.__maxspeed:
            self.__horizontalpostion = self.__currentspeed
            return "the speed is= ",self.__horizontalpostion
        else:
            return ("invalid speed entered")

ferrari = vehicle("ABC-123",100,50)
cs = int(input("Enter your current speed: "))
hp = int(input("Enter your Horizonal position: "))
ferrari.setcurrentspeed(cs)
ferrari.sethorizontalposition(hp)
print(ferrari.Increasespeed())

#print(ferrari.getincreaseamount())