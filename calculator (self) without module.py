choice = "Y"
attempt = 0
while choice == "Y":
    num1 = 0
    num2 = 0
    operation = " "
    

    
    num1 = int(input("enter first num: "))
    num2 = int(input("enter second num: "))
    
    issue = "true"
    while issue == "false":
        operation = input("To add, press '+'.To subtract, press '-'.To divide, press '/'.To multiply, press '*'.: ")
        
        if operation == "+":
            ans = num1 + num2
            issue = "true"
            
                
        elif operation == "-":
            ans = num1 - num2
            issue = "true"
            
                
        elif operation == "/":
            ans = num1 / num2
            issue = "true"
                 
        elif operation == "*":
            ans = num1 * num2
            issue = "true"
            
        else:
            print("invalid error entered. Enter again")
            issue = "true"

    print(ans)
        
    choice = input("Do you want to try again? Y/N")

print("Thank you for using our service")
end = input("Press any key to end the program") 
    
