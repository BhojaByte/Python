def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
        return -1
#Example Usage
My_list = [10, 25, 3, 0, 20, 8]
choice="Y"
while choice == "Y":


    target_element = int(input("enter Value to search"))
    result = linear_search(My_list,target_element)

    if result != -1:
        print("Element",target_element,"found at index",result)
    else:
        print("Element",target_element,"not found in the list.")
    choice=input("do you want to search again Y/N")
print("Thanks for using our program")
