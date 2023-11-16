def calculate(num1,num2,operation):
    choice = "Y"
    while choice == "Y":
    
        if operation == "+":
            answer = num1 + num2
                
        elif operation == "-":
            answer = num1 - num2
                
        elif operation == "/":
            answer = num1 / num2
                 
        elif operation == "*":
            answer = num1 * num2
        else:
            print("invalid Operation")

        return answer
            
        choice = ("Do you want to try again? Y/N")
            


#test

n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
operator = input("To add, press '+'.To subtract, press '-'.To divide, press '/'.To multiply, press '*'.: ")
ans = int(calculate(n1,n2,operator))
print("here is your answer", ans)
