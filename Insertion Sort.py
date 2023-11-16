#Insertion sort Program

def insertion_sort(arr):
    #traverse through the entire array
    for i in range( 1 , len(arr)):
        #store the current element to be inserted.
        current_element = arr[i]

        #Initialize a pointer to the previous element.

        j = i - 1

        #move elements of arr[0..i-1] that are greater  than the current_element
        #one position ahead of thier current postion.

        while j>= 0 and current_element < arr[j]:
            arr[j + 1] = arr [j]
            j -= 1

        #insert the crrent_element into its current postion.
            arr[j + 1] = current_element


#example usage
my_list = [12, 11, 13 , 5, 6]
insertion_sort(my_list)
print("sorted array:", my_list)
