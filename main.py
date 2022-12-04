import time, sys

print("Please insert card.")
time.sleep(5)
password = 0000
balance = 10000
cnt = 0 

# enter the password
while True:
    try :
        PIN = int(input("Please enter pin number."))
    except ValueError:
        print("Please enter the valid pin number.")
        cnt += 1
    else:
        if PIN == password:
            break
        else:
            print("Please enter the valid pin number.")
            cnt += 1
            
    if cnt == 5:
        print("Please Ask the bank for the pin number.")
        sys.exit("Please get your card.")
    
            
        
while True:
    # select the number     
    print(" ------------------ \n 1 : Check Balance \n 2 : Deposit \n 3 : WithDraw \n 4 : Exit \n ------------------ "  )
    try :
        select_num = int(input('Please enter the number.'))
        if select_num <= 0 or select_num > 4:
            raise ValueError("Please enter the valid value.")
    except ValueError :
        print("Please enter the valid value.")
    
    else:
        # check balance    
        if select_num == 1:
            print(f"Your balance is {balance}")

        # deposit   
        elif select_num == 2:       
            try : 
                deposit = int(input("Please enter the amount you want to deposit."))
                if deposit < 0 :
                    raise ValueError("Please enter the valid value.")
            except ValueError: 
                print("Please enter the valid value.")
            else: 
                balance += deposit
                print(f"Your balance is {balance}")

        # withdraw        
        elif select_num == 3:
            try : 
                withdraw = int(input("Please enter the amount you want to deposit."))
                if withdraw < 0 or withdraw > balance :
                    raise ValueError("Please enter the valid value.")
            except ValueError : 
                print("Please enter the valid value.")
            else: 
                balance -= withdraw
                print(f"Your balance is {balance}")

        # exit    
        elif select_num == 4:
            print("Please get your card.")
            break


        