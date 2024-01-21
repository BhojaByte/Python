class computer:
    def __init__(self,ss,cpu,gpu):
        self.__screensize = ss
        self.__ram = None
        self.__rom = None
        self.__peripherals = None
        self.__cpu = cpu
        self.__gpu = gpu
    
    def setram(self,ram):
        self.__ram = ram
    def setrom(self,rom):
        self.__rom = rom
    def setperopherals(self,pp):
        self.__peripherals = pp
    
    def getram(self):
        return self.__ram
    def getrom(self):
        return self.__rom
    def getperipherals(self):
        return self.__peripherals
    

dell = computer("1600x900","Corei5-9400k","gtx 750ti")
dell.setram("8 GB")

print(dell.getram())