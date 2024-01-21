class employee:
    def __init__(self,name,staffno):
        self.__name = name
        self.__staffno = staffno
        self.__fulltimestaff = True

    def showdetails(self):
        print("Employee Name = "+ str(self.__name))
        print("Employee Number = "+ str(self.__staffno))
class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self,name,staffno)
        self.__fulltimestaff = False
        self.__hoursworked = 0

    def getsHoursWorked(self):
        return self.__hoursworked
    
class Fulltime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fulltimestaff = True
        self.__yearlysalary = 0
    def getyearlysalary(self):
        return self.__yearlysalary
    

# instance making

permenentstaff = Fulltime("Eric Jones", 72)
permenentstaff.showdetails()
temporarystaff = partTime("Alice Hue", 1017)
temporarystaff.showdetails()