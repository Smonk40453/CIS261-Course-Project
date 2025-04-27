#Stephanie Monk 
#CIS261
#Course Project 
#Phase 1 

def WelcomeMessage () : 
    print("\n Welcome to the Employee Payroll System")
def GoodbyeMessage (): 
    print ("\n Thank you for using the payroll system. Goodbye.")
def GetPositiveFloat(prompt) :
    while True:
        try:
            value = float(input(prompt))
            if value < 0: 
                print("Please enter a positive number")
            else: 
                return value 
        except ValueError: 
            print("Invalid input. Please enter a valid number.")
def GetEmployeeName (): 
    while True: 
        name = input("Enter employee name: ").strip()
        if name:
            return name 
        else: 
            print("Employee name cannot be empty.")
def GetTotalhours():
    return GetPositiveFloat ("Enter total hours worked: ")
def GetHourlyRate(): 
    return GetPositiveFloat ("Enter hourly rate: ")
def GetTaxRate():
    while True: 
        tax = GetPositiveFloat("Enter income tax rate (as decimal, e.g.,0.2 for 20%): ")
        if 0 <= tax <= 1: 
            return tax 
        else: 
            print("Tax rate must be between 0 and 1.")
def CalculatePay(totalHours, hourlyRate,taxRate):
    GrossPay = totalHours * hourlyRate
    incomeTax = GrossPay * taxRate 
    netPay = GrossPay - incomeTax 
    return GrossPay, incomeTax, netPay 
def displayEmployeeInfo(name,totalHours, hourlyRate, GrossPay,taxRate,incomeTax,netPay):
    print( "\n--- Employee Info ---") 
    print(f"{'Name:' : <20}{name}")
    print(f"{'Total Hours:' :<20}{totalHours:.2f}")
    print(f"{'Hourly Rate:' :<20}${hourlyRate:.2f}")
    print(f"{'Gross Pay:' :<20}${GrossPay:.2f}")
    print(f"{'Tax Rate:' :<20}{taxRate*100:.1f}%")
    print(f"{'Income Tax:' :<20}${incomeTax:.2f}")
    print(f"{'Net Pay:' :<20}${netPay:.2f}\n")
def display_totals(total_employees, total_hours,total_GrossPay,total_incomeTax,total_netPay) :
    print("\n=== Payroll Summary ===")
    print(f"{'Total Employees:':<20}{total_employees}")
    print(f"{'Total Hours:':<20}{total_hours}")
    print(f"{'Total Gross Pay:':<20}{total_GrossPay}")
    print(f"{'Total Income Tax:':<20}{total_incomeTax}")
    print(f"{'Total Net Pay:':<20}{total_netPay}")
def main() :
    WelcomeMessage()
    total_employees = 0 
    total_hours = 0 
    total_grossPay = 0 
    total_incometax = 0 
    total_netPay = 0 
    while True: 
       print("Type 'End' to stop or enter employee name to continue: ")
       name = GetEmployeeName()
       if name.lower() == "end":
           break 
       hours = GetTotalhours()
       rate = GetHourlyRate()
       taxRate = GetTaxRate()
       GrossPay, incomeTax, netPay = CalculatePay(hours, rate, taxRate)
       displayEmployeeInfo(name, hours,rate,GrossPay, taxRate,incomeTax,netPay)
       total_employees += 1
       total_hours += hours
       total_grossPay += GrossPay
       total_incometax += incomeTax
       total_netPay += netPay
       display_totals(total_employees,total_hours,total_grossPay,total_incometax,total_netPay)
    GoodbyeMessage()
if __name__=="__main__":
    main()
    

    

