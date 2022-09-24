#Coffee Machine

from resources import MENU, resources

def resource():
    '''If the user asks for resources this function is called.'''
    global balance
    for elements in resources:
        print(f'{elements.capitalize()}: {resources[elements]}')
        print(f'Money: {balance}')


def resource_sufficient(drink):
    '''Checks  If the resource is sufficient and returns True or False'''
    for types in MENU[drink]['ingredients']:
        if resources[types] <= MENU[drink]['ingredients'][types]:
            print(f'Sorry not enough {types.capitalize()}')
            return False
    return True


def process_coins(drink):
    '''Processes the coins and find the total of input coins.'''
    global MENU
    print(f"Your total will be: {MENU[drink]['cost']}")
    print('Please insert coins.')   
    total = int(input('How many quarters: ')) * 0.25
    total += int(input('How many dimes: '))   * 0.10
    total += int(input('How many nickels: ')) * 0.05
    total += int(input('How many pennies: ')) * 0.01
    return total


def is_transaction_sucessful(drink):
    '''Checks if the input coins is enough and returns the balance if extra.'''       
    global balance, MENU, process_coin
    process_coin = process_coins(drink)
    if MENU[drink]['cost'] <= process_coin:
        if MENU[drink]['cost'] < process_coin:
            balance = process_coin - MENU[drink]['cost']
            print(f'Your balance: ${round(balance,2)}')
            return True
    else:
        print(f'Sorry not enough amount.\nCash returned.')
        return False



def make_coffee(drink):
    global resources
    for types in MENU[drink]['ingredients']:
        resources[types] -= MENU[drink]['ingredients'][types]
    print(f'Here is your {drink}☕ enjoy!!')



run = True

while run:
    inp = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if inp == 'off':
        run = False
    elif inp == 'report':
        resource()
    else:
        drink = inp
        if resource_sufficient(inp):
            if is_transaction_sucessful(inp):
                make_coffee(drink)


