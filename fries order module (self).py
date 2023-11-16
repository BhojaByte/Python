def order(cash):
    if cash == 20:
        return "Here's your 20rs fries"
    elif cash == 30:
        return "Here's your 30rs fries"
    elif cash == 50:
        return "Here's your 50rs fries"
    else:
        return "invalid amount entered"

#Test

choice = "Y"
attempt = 0

while choice == "Y" and attempt < 3:
    amount = int(input("pay the cash: "))
    if amount == 20 or amount == 30 or amount == 50:
        print(order(amount))
    else:
        print("Enter Valid amount(20,30,50)")
    choice = input("Do you want to try again? Y/N: ")
    attempt += 1
    
print("Thank you for shopping")
end=input("enter any key to exit the program")













