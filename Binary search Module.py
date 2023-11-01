def binary_search(arr,target):
    #initialize the search range boundaries
    left = 0
    right = len(arr)-1

    while left<= right:
        #calculate the middle index
        mid=(left + right )//2
        if arr[mid] == target:
            return mid #found the target, return its index.
        elif arr[mid] < target:
            #if target  is greater, narrow the search to the right half.
             left = mid + 1
        else:
            #if target is smaller, narrow the search to the left half
            right = mid - 1


    #if the target is not in th list, return -1 to indicate not found
    return -1

#Example usage

my_list = [1,3,5,7,9,11,13,17,19]
target = 13
result = binary_search(my_list,target)

if result != -1:
    print(f"Element{target} found at index {result}")
else:
    print(f"Element{target} not found in the list")




    
