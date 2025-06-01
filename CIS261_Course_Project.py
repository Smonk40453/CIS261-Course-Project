#Stephanie Monk 
#CIS261
#Course Project 
#Phase 3


import datetime
import os 
FILENAME = "employee_data.txt"
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
def GetDateRange() :
    while True:
        from_date = input("Enter FROM date (mm/dd/yyyy): ").strip()
        to_date = input("Enter TO date (mm/dd/yyyy): ").strip()
        try: 
           datetime.datetime.strptime(from_date, "%m/%d/%Y")
           datetime.datetime.strptime(to_date, "%m/%d/%Y")
           return from_date, to_date 
        except ValueError:
            print("Both dates must be entered in mm/dd/yyyy format.")
def CalculatePay(totalHours, hourlyRate,taxRate):
    GrossPay = totalHours * hourlyRate
    incomeTax = GrossPay * taxRate 
    netPay = GrossPay - incomeTax 
    return GrossPay, incomeTax, netPay 
def displayEmployeeInfo(from_date,to_date,name,totalHours, hourlyRate, GrossPay,taxRate,incomeTax,netPay):
    print( "\n--- Employee Info ---") 
    print(f"{'From Date:' :<20}{from_date}")
    print(f"{'To Date:' :<20}{to_date}")
    print(f"{'Name:' : <20}{name}")
    print(f"{'Total Hours:' :<20}{totalHours:.2f}")
    print(f"{'Hourly Rate:' :<20}${hourlyRate:.2f}")
    print(f"{'Gross Pay:' :<20}${GrossPay:.2f}")
    print(f"{'Tax Rate:' :<20}{taxRate*100:.1f}%")
    print(f"{'Income Tax:' :<20}${incomeTax:.2f}")
    print(f"{'Net Pay:' :<20}${netPay:.2f}\n")
def display_totals(summary) :
    print("\n=== Payroll Summary ===")
    print(f"{'Total Employees:':<20}{summary['total_employees']}")
    print(f"{'Total Hours:':<20}{summary['total_hours']}")
    print(f"{'Total Gross Pay:':<20}${summary['total_grosspay']}")
    print(f"{'Total Income Tax:':<20}${summary['total_incomeTax']}")
    print(f"{'Total Net Pay:':<20}${summary['total_netpay']}")
def ReadAndDisplayFile():
    if not os.path.exists(FILENAME):
        print("Data file not found.")
        return 
    choice = input("\nEnter FROM date for report(mm/dd/yyyy) or 'All' to display all records: ").strip()
    try: 
        if choice.lower() != "all":
            datetime.datetime.strptime(choice, "%m/%d/%Y")
    except ValueError:
        print("Invalid date format. Use mm/dd/yyyy.")
        return
    summary = {
        'total_employees':0,
        'total_hours':0,
        'total_grosspay':0,
        'total_incomeTax':0,
        'total_netpay':0,
    }
    with open(FILENAME,"r") as file: 
            for line in file: 
                from_date, to_date, name, hours,rate,taxRate = line.strip().split("|")
                if choice.lower() != "all" and from_date != choice:
                    continue
                hours = float(hours)
                rate = float(rate)
                taxRate = float(taxRate)
                GrossPay,incomeTax,netPay = CalculatePay(hours,rate,taxRate)
                displayEmployeeInfo(from_date, to_date,name,hours,rate,GrossPay,taxRate,incomeTax,netPay)
                summary['total_employees']+= 1
                summary['total_hours'] += hours 
                summary['total_grosspay'] += GrossPay
                summary['total_incomeTax'] += incomeTax
                summary['total_netpay'] += netPay
    display_totals(summary)
def main() :
    WelcomeMessage()
    with open (FILENAME, "a") as file:
        while True:
            print("Type 'End' to stop or enter employee name to continue: ")
            name = GetEmployeeName()
            if name.lower() =="end":
                break 
            from_date,to_date = GetDateRange()
            hours = GetTotalhours()
            rate = GetHourlyRate()
            taxRate = GetTaxRate()
            file.write(f"{from_date}|{to_date}|{name}|{hours}|{rate}|{taxRate}\n")
    ReadAndDisplayFile()
    GoodbyeMessage()
if __name__=="__main__":
    main()