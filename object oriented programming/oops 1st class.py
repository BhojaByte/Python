class car():
    def __init__(self,e,n):
        self.__enginesize = n
        self.__registrationnumber = e
        self.__health = 100
        self.__purchaseprice = 0.00
        self.__tax = 0.00
    def setprice(self,p):
        self.__purchaseprice = p 
    def settax(self):
        self.__tax = self.__purchaseprice * 0.25
    def getprice(self):
        return(self.__purchaseprice)
    def gettax(self):
        return(self.__tax)
    
civic = car(1000,"BH104")
price = int(input("Set price for your new civic: "))
civic.setprice(price)
civic.settax()
print("The price of civic is",civic.getprice(),"The tax on civic is:",civic.gettax())