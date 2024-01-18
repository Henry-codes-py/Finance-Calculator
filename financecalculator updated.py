import math

print("###### WELCOME ######")

def calculate_investment():     
    deposit = int(input("please enter the total you would like to deposit: "))
    interest_rate = float(input("Please enter the rate of interest (you do not need to enter the % symbol): "))
    duration = int(input("Please enter the length of investment you intend in years: "))
    interest_type = input("Please select by typing either simple or compound: ")
    
    if interest_type.lower() == "simple":
        investment_total = deposit * (1 + interest_rate / 100 * duration)
        print("##########")
        print(f"Your simple investment total is {investment_total:.2f} at {interest_rate} percent interest for {duration} years")
        print("##########")
        
    elif interest_type.lower() == 'compound':
        print("##########")
        investment_total = (deposit * math.pow((1 + interest_rate / 100), duration))
        print(f"Your compound investment total is {investment_total:.2f} at {interest_rate} percent interest for {duration} years")
        print("##########")
        
    else:
        print("Invalid interest type, please try again - you must enter either simple or compound: ")
        
        return

def calculate_bond():
    house_value = int(input("Please enter the current value of the house: "))
    interest_rate = float(input("Please enter the rate of interest (you do not need to add the % symbol): "))
    month_duration = int(input("Please enter the number of months you plan to pay it back: "))
    monthly_interest_rate = float((interest_rate / 100) / 12)

    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-month_duration))
    print("##########")
    print(f"Your bond repayment total is {repayment:.2f} at {interest_rate} percent interest over {month_duration} months")
    print("##########")
    return


calculatorchoice = input("Please select which calculator you want by typing either Bond or Investment: ").lower()

if calculatorchoice == "investment":
    calculate_investment()

elif calculatorchoice == "bond":
    calculate_bond()



# def calculate_bond():