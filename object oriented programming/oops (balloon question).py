class balloon():
    def __init__(self,d,c):
        self.__defenceitem = d #defence item assigning d as string ...
        self.__colour = c
        self.__health = 100
    def GetDefenceItem(self):
        return self.__defenceitem()
    def ChangeHealth(self,num):
        self.__health = self.__health + num
    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False
    


def Defend(x):
    
    strenght = int(input("Enter opponent's strenght: "))
    x.ChangeHealth(-strenght) 
    print(x.GetDefenceItem())
    if x.CheckHealt() == True:
        print("it has no health remaining")
    else:
        print("it has health remaining")
    return x



defenceitem = input("enter your defence item: ")
colour = input("enter your colour : ")

balloon1 = balloon(defenceitem,colour)
print(Defend(balloon1))