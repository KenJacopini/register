from time import ctime as current_time

##list of help commands
HELP_COMMANDS = ['help', 'h']

##list of end program commands
QUIT_COMMANDS = ['q', 'quit']

##command to show all logs
SHOW_COMMAND = 'showlogs'

##Program state
IS_RUNNING = True

##initialize variables globally
CUSTOMER_NAME = PRODUCT_NAME = TIME_OF_PURCHASE = QTY = PRICE = TOTAL_COST = None

def trim(var):
    return var.strip()

def getInput():
    global IS_RUNNING
    try:
        ##this is the input prompt to the user
        prompt = 'Type info here: '

        ##collcet info from user and assigns to respective vars
        info = input(prompt)

        if info.lower() in HELP_COMMANDS:
            displayHelpMessage()
            return False, None

        if info.lower() in QUIT_COMMANDS:
            IS_RUNNING = False
            return True, None

        if info.lower() == SHOW_COMMAND:
            showLogs()
            return False, None
        
        info = info.split(',')
        if len(info) != 4:
            displayErrorMessage()
            return False, None
        
        return True, info

    except Exception as e:
        displayErrorMessage()
        return False, None

def displayErrorMessage(d):
    print('Invalid Input!!!\n')
    
def displayHelpMessage():
    print('Here are the working commands')
    print('-----------------------------')
    print('showLogs: to see all registered information')
    print('help [or h,]: to see the help message')
    print('Custormer Name, Product Name, Quantity, PRICE: seperated by commas to register information')
    print()

def getUserInput():
    status = False
    while status == False:
        status, info = getInput()
    return info

def showLogs():
    if QTY is None:
        print('Empty Logs!\n')

    else:
        print('{:<20s} {:<15s} {:<10s} {:<10s} {:<10s} {:<10s}'.format(
                'Customer\'s Name', 'Product Name', 'QTY', 'PRICE', 'Total Cost', 'Time'
                )
            )    
        print('{:<20s} {:<15s} {:<10.2f} {:<10.2f} {:<10.2f} {:<10s}\n'.format(
                CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE, TOTAL_COST, TIME_OF_PURCHASE
                )
            )
    
def main():
    global CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE, TOTAL_COST, TIME_OF_PURCHASE 
    #shows how to use program
    displayHelpMessage()

    while True:
        #collects the necessary input
        info = getUserInput()
        
        if IS_RUNNING == False:
            print('Program is Shutting down...')
            print('Program Shut down Sucessfully!')
            break
        
        ##trim var spaces
        CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE = list(map(trim, info))

        ##cast to number
        PRICE = float(PRICE)
        QTY = float(QTY)

        ##the total cost of purchase
        TOTAL_COST = PRICE * QTY

        ##time of purchase
        TIME_OF_PURCHASE = current_time()

        

if __name__ == '__main__':
    main()
