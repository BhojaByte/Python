TheData = [20,3,4,8,12,99,4,26,4]

def insertionsort(arr):
    for count in range(len(arr)):
        insertdata = arr [count]
        inserted = 0
        nextvalue = count - 1
        while nextvalue >= 0 and inserted != 1:
            if insertdata < arr[nextvalue]:
                arr[nextvalue + 1] = arr [nextvalue]
                nextvalue -= 1
                arr[nextvalue + 1] = arr [nextvalue]
            else:
                inserted = 1
    print(arr)

def getarr(arr):
    for i in range(len(arr)):
        print(arr[i])
getarr(TheData)

print("Data before sorting:") 
getarr(TheData)

print("Data after sorting")
insertionsort(TheData)

#test and take screenshot and submit to evidence

def checknum(arr):
    found = False
    num = int(input("Enter number to search: "))
    for i in range(len(arr)):
        if num == arr[i]:
            found = True
    if found == True:
        print("Found")
    else:
        print("not found")

checknum(TheData)
       

