#Income tax Calculator using function

from datetime import date
today = date.today()

name = [] 
address = [] 
age = [] 
phone = [] 
monthly_income = [] 
marital_status = [] 
insurance = [] 
disability = [] 
gender = [] 
diplomat = [] 
monthly_allowance = [] 
annual_income = [] 
taxable_income = []
finaltax = []

def StaticInformation():
    print("\t\t\t\t____________________________________________________________________________________________\n")
    print("\t\t\t\t\t\t\t\tGovernment of Nepal")
    print("\t\t\t\t\t\t\t\tMinistry of Finance")
    print("\t\t\t\t\t\t\t     Inland Revenue Department")
    print("\t\t\t\t____________________________________________________________________________________________\n")
    print("\t\t\t\t\t\t   Welcome to the Income Tax Calculation System")
    print("\t\t\t\t\t\t\t\tDate: {}".format(today))
    print("\t\t\t\t_____________________________________________________________________________________________\n")

def EmployeeInformation(number_of_customer):
    for i in range(number_of_customer):
        print("\nFor customer '{}'".format(i+1))
        print("----------------")
        name.append(input("\nName: "))
        address.append(input("Address: "))
        age.append(int(input("Age: ")))
        phone.append(int(input("Phone: ")))
        marital_status.append(input("Are you married or unmarried? Please type 'Y' or 'N': ")) 
        insurance.append(input("Have you done your insurance? Please type 'Y' or 'N': "))
        gender.append(input("Are you male or female? Please type 'M' or 'F': "))
        disability.append(input("Are you disabled in any form? Please type 'Y' or 'N': "))
        if disability[i].lower() == "n": # only asks diplomat information in case the individal is not disabled
            diplomat.append(input("Are you a diplomat? Please type 'Y' or 'N': "))
            if diplomat[i].lower() == "y":
                monthly_allowance.append(int(input("Enter your monthly foreign allowances: ")))
            elif diplomat[i].lower() == "n":
                monthly_allowance.append(0) # monthly allowance is 0 as default in case of no diplomat
        elif disability[i].lower() == "y": 
            diplomat.append("n") # in case of disability diplomat value is set to 'n' 
            monthly_allowance.append(0) # in case of disability monthly allowance is set to '0'
        monthly_income.append(int(input("Enter your monthly income: ")))
        print("_________________________________\n")

#this function calculates the taxable income for possible deduction in insurance, allowances, gender and disability
def TaxableIncomeCalculation(number_of_customer): 
    for i in range(number_of_customer):
        annual_income.append(int(monthly_income[i] * 12)) 
        
        if marital_status[i] == "n":
            if disability[i].lower() == "y" and gender[i].lower() == "m" and insurance[i].lower() == "n":
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5)) # 50% is deducted for disablity
                finaltax.append(CalculateIndividual(taxable_income[i])) # stores the returned value from CalculateIndividual function
            elif disability[i].lower() == "y" and gender[i].lower() == "m" and insurance[i].lower() == "y":
                annual_income[i] = annual_income[i] - 25000 # annual insurance amount reduction
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5))
                finaltax.append(CalculateIndividual(taxable_income[i]))
            elif disability[i].lower() == "y" and gender[i].lower() == "f" and insurance[i].lower() == "n":
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5)) # 50% is deducted for disablity
                taxable_income[i] = round(taxable_income[i] - (taxable_income[i] * 0.1)) # additional 10% is deducted for being female
                finaltax.append(CalculateIndividual(taxable_income[i]))
            elif disability[i].lower() == "y" and gender[i].lower() == "f" and insurance[i].lower() =="y":
                annual_income[i] = annual_income[i] - 25000 # annual insurance amount reduction
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5))
                taxable_income[i] = round(taxable_income[i] - (taxable_income[i] * 0.1))
                finaltax.append(CalculateIndividual(taxable_income[i]))
            elif diplomat[i].lower() == "y" and insurance[i].lower() =="n":
                taxable_income.append(round(annual_income[i] + monthly_allowance[i] * 0.25 * 12)) # 75% amount of allowance is decucted from taxable income
                finaltax.append(CalculateIndividual(taxable_income[i]))    
            elif diplomat[i].lower() == "y" and insurance[i].lower() =="y":
                annual_income[i] = annual_income[i] - 25000 # annual insurance amount reduction
                taxable_income.append(round(annual_income[i] + monthly_allowance[i] * 0.25 * 12)) # 75% amount of allowance is decucted from taxable income
                finaltax.append(CalculateIndividual(taxable_income[i]))
            else:
                taxable_income.append(annual_income[i])
                finaltax.append(CalculateIndividual(taxable_income[i]))
        
        elif marital_status[i] == "y":
            if disability[i].lower() == "y" and gender[i].lower() == "m" and insurance[i].lower() == "n":
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5)) # 50% is deducted for disablity
                finaltax.append(CalculateIndividual(taxable_income[i])) # stores the returned value from CalculateCouple function
            elif disability[i].lower() == "y" and gender[i].lower() == "m" and insurance[i].lower() == "y":
                annual_income[i] = annual_income[i] - 25000 # annual insurance amount reduction
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5))
                finaltax.append(CalculateIndividual(taxable_income[i]))
            elif disability[i].lower() == "y" and gender[i].lower() == "f" and insurance[i].lower() == "n":
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5)) # 50% is deducted for disablity
                taxable_income[i] = round(taxable_income[i] - (taxable_income[i] * 0.1)) # additional 10% is deducted for being female
                finaltax.append(CalculateIndividual(taxable_income[i]))
            elif disability[i].lower() == "y" and gender[i].lower() == "f" and insurance[i].lower() =="y":
                annual_income[i] = annual_income[i] - 25000 # annual insurance amount reduction
                taxable_income.append(round(annual_income[i] - annual_income[i] * 0.5))
                taxable_income[i] = round(taxable_income[i] - (taxable_income[i] * 0.1))
                finaltax.append(CalculateIndividual(taxable_income[i]))
            elif diplomat[i].lower() == "y" and insurance[i].lower() =="n":
                taxable_income.append(round(annual_income[i] + monthly_allowance[i] * 0.25 * 12)) # 75% amount of allowance is decucted from taxable income
                finaltax.append(CalculateIndividual(taxable_income[i]))    
            elif diplomat[i].lower() == "y" and insurance[i].lower() =="y":
                annual_income[i] = annual_income[i] - 25000 # annual insurance amount reduction
                taxable_income.append(round(annual_income[i] + monthly_allowance[i] * 0.25 * 12)) # 75% amount of allowance is decucted from taxable income
                finaltax.append(CalculateIndividual(taxable_income[i]))
            else:
                taxable_income.append(annual_income[i])
                finaltax.append(CalculateIndividual(taxable_income[i]))

#function for single
def CalculateIndividual(y): # y refers to the returned value that is taxable_income
    if y<=400000:
        tax = 1/100*y
    elif y>400000 and y<=500000:
        tax1 = 4000 #tax for upto 400000
        additional = y - 400000 #extra amount greater than 400000 and less than or equal to 500000
        tax2 = 10/100*additional #tax for that extra amount that is greater than 400000
        tax = int(tax1 + tax2) #total tax 
    elif y>500000 and y<=700000:
        tax1 = 14000 #tax for upto 500000
        additional = y - 500000 #extra amount greater than 500000 and less than or equal to 700000
        tax2 = 20/100*additional #tax for that extra amount that is greater than 500000
        tax = int(tax1 + tax2) #total tax 
    elif y>700000 and y<=2000000:
        tax1 = 54000 #tax for upto 700000
        additional = y - 700000 #extra amount greater than 700000 and less than or equal to 2000000
        tax2 = 30/100*additional #tax for that extra amount that is greater than 700000
        tax = int(tax1 + tax2) #total tax 
    elif y>2000000:
        tax1 = 444000 #tax for upto 2000000
        additional = y - 2000000 #extra amount greater than 2000000
        tax2 = 36/100*additional #tax for that extra amount that is greater than 2000000
        tax = int(tax1 + tax2) #total tax 
    return tax

#function for married
def CalculateCouple(y): # y refers to the returned value that is taxable income
    if y<=450000:
       tax = int(1/100*y)
    elif y>450000 and y<=550000:
       tax1 = 4500 #tax for upto 450000
       additional = y - 450000 #extra amount greater than 450000 and less than or equal to 550000
       tax2 = 10/100*additional #tax for that extra amount that is greater than 450000
       tax = int(tax1 + tax2) #total tax 
    elif y>550000 and y<=750000:
        tax1 = 14500 #tax for upto 550000
        additional = y - 550000 #extra amount greater than 550000 and less than or equal to 750000
        tax2 = 20/100*additional #tax for that extra amount that is greater than 550000
        tax = int(tax1 + tax2) #total tax 
    elif y>750000 and y<=2000000:
        tax1 = 54500 #tax for upto 750000
        additional = y - 750000 #extra amount greater than 750000 and less than or equal to 2000000
        tax2 = 30/100*additional #tax for that extra amount that is greater than 750000
        tax = int(tax1 + tax2) #total tax 
    elif y>2000000:
        tax1 = 429500 #tax for upto 2000000
        additional = y - 2000000 #extra amount greater than 2000000
        tax2 = 36/100*additional #tax for that extra amount that is greater than 2000000
        tax = int(tax1 + tax2) #total tax 
    return tax

#function for display
def DisplayOutput(number_of_customers):
    StaticInformation()
    for i in range(number_of_customers):
        print("-----------------------------")
        print("Information for customer '{}':".format(i+1))
        print("-----------------------------")
        print("Name: {}".format(name[i]))
        print("Address: {}".format(address[i]))
        print("Age: {}".format(age[i]))
        print("Phone: {}".format(phone[i]))
        print("Marital Status: {}".format(marital_status[i]))
        print("Insurance: {}".format(insurance[i]))
        print("Disability: {}".format(disability[i]))
        print("Gender: {}".format(gender[i]))
        print("Diplomat: {}".format(diplomat[i]))
        print("Monthly Allowance: Rs. {}".format(monthly_allowance[i]))
        print("Monthly Income: Rs. {}".format(monthly_income[i]))
        print("-------------------------")
        print("Based on the information above your total tax payable is Rs. {}\n".format(int(finaltax[i])))

#function to write in a file
def FileWrite(number_of_customers):
    data = open("tax_info.txt", "w")
    for i in range(number_of_customers):
        data.write("Information for customer '{}':\n".format(i+1))
        data.write("-----------------------------\n")
        data.write("Name: {}\n".format(name[i]))
        data.write("Address: {}\n".format(address[i]))
        data.write("Age: {}\n".format(age[i]))
        data.write("Phone: {}\n".format(phone[i]))
        data.write("Marital Status: {}\n".format(marital_status[i]))
        data.write("Insurance: {}\n".format(insurance[i]))
        data.write("Disability: {}\n".format(disability[i]))
        data.write("Gender: {}\n".format(gender[i]))
        data.write("Diplomat: {}\n".format(diplomat[i]))
        data.write("Monthly Allowance: Rs. {}\n".format(monthly_allowance[i]))
        data.write("Monthly Income: Rs. {}\n".format(monthly_income[i]))
        data.write("-------------------------\n")
        data.write("Based on the information above your total tax payable is Rs. {}".format(int(finaltax[i])))

#main function definition
def main():
    StaticInformation()         
    noc = int(input("Enter number of customers: ")) # noc refers to number of customers in short
    EmployeeInformation(noc)
    TaxableIncomeCalculation(noc)
    DisplayOutput(noc)
    FileWrite(noc)
       
#main function call
main()