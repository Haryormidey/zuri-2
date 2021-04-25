
import random

database = {
    9315065624:['akinsanyaayomide99@gmail.com','Precious','Akinsanya','password',345]

}

def init():

    
    print("Welcome to Pricy Bank")
    

    haveAccount = int(input('Do you have an account with us: 1 (yes) 2 (no)\n'))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
       print(register())
    else:
        print('You have selected an invalid option')
        init()

def login():
    print("Login to your account")

    accountNumberFromUser = int(input('What is your account number?\n'))
    password = input('what is your password\n')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperations(userDetails)

    print('Invalid account or password')
    login()

def register():
    print('Registration')
    email = input('What is your email address?\n')
    first_name = input('What is your First name?\n')
    last_name = input('What is your Last name?\n')
    password = input('create a password for yourself\n')

    accountNumber = generationOfAccountNumber()

    database[accountNumber] = [email,first_name,last_name,password,currentBalance]

    print('Your account has been successfully created')
    print('== === ======== === ==')
    print('Your account number is %d' % accountNumber)
    print('Make sure you keep it safe')
    print('== === ======== === ==')

    login()

    

def bankOperations(user):
    print("Welcome %s %s" % (user[1], user[2]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) logout (4) exit\n"))  

    if(selectedOption == 1):
        deposit()

    elif(selectedOption == 2):
        withdrawal()

    elif(selectedOption ==3):
        logout()

    elif(selectedOption == 4):
        exit()

    else:
        print('Invalid option selected')
        bankOperations(user)


def deposit():
    input('How much would you like to deposit?\n')
    print('Deposit successful')
    login()

def withdrawal():
    input('How much would you like to wihdraw?\n')
    print('withdrawal successful')
    login()



def generationOfAccountNumber():
    
    return random.randrange(1111111111,9999999999)

def currentBalance(userDetails):
    return userDetails[4]

def logout():
    login()
init()