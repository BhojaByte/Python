#password Generator

import random

pwd = ''
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{,.,/<>:"
again = True

while again:
    again = False


    pass_lenght = int(input("enter password lenght"))
    numeberofpass = int(input("How many passwords you want to generate?"))
    password = ''
    for c in range(numeberofpass):
        password = ''
        for i in range(pass_lenght):
            
            result = ''
            result = random.sample(chars,1)[0] #picks a random character from 'chars'
            #password += ''.join(result) #Concatenation
            #trying another way to concatenate
            password += result
        print(password)
        # Select a random character
            #result = ''.join(random_char)

    choice = input("Do you want to generate password again? Yes/No")
    choice = choice.upper()

    if choice == "YES":
        again = True
    else:
        again = False

End = input("Press any key to close the program")