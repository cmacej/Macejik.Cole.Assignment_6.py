"""Created By: Cole Macejik
ICT-4370 Section: 1
Assignment # 6
Created: 05/10/2020
This program pulls from two files, one for stock information and one for bond
    information. Using the data from those two files the program writes 
    Bob Smith's stock ownership information and his bond ownership information 
    to a text file. Using classes for the stock, bond, and investor. 
    Calculations are made in the methods of the stock class. Bond Class
    inherits methods and attributes from stock class."""

#Import date time function for yearly calculations.
from datetime import datetime

#Stock class with stock information attributes.
class Stock():
    #Represents the information for the Stock ownership.
    def __init__(self, purchase_ID, symbol, quantity, purchase_price, \
                current_price, purchase_date):
        #Initialize stock attributes.
        self.purchase_ID = purchase_ID
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date
        
#Method for earnings gained or lossed.
    def calculate_earnings_loss(self):
            #Calculation made for earnings made or lost. 
            earnings_loss = (self.current_price - self.purchase_price) * self.quantity
            return earnings_loss
        
#Method for calculating the annual earnings gained or lost.  
    def annual_earnings_calculation(self):
            #Represents formatted variables for calculation.     
            date_of_purchase = datetime.strptime(self.purchase_date, '%m/%d/%Y')
            days_owned = ((datetime.today() - date_of_purchase).days)
            years_owned = (days_owned / 365)
            
            #Calculation made for yearly earnings or loss percentage.
            calculated_yearly_earnings_loss_percent = round(((( 
            self.current_price - self.purchase_price) / self.purchase_price) 
            / years_owned) * 100, 2)
            return calculated_yearly_earnings_loss_percent

#Sub class of the Stock class.
class Bond(Stock):
    #Represents the information for the Bond ownership. 
    def __init__(self, purchase_ID, symbol, quantity, purchase_price, \
                current_price, purchase_date, coupon, bond_yield):
        #Initialization of the Stock class attributes.
        super().__init__(purchase_ID, symbol, quantity, purchase_price,\
                        current_price, purchase_date)
        #Initialization of additional Bond class attributes.
        self.coupon = coupon
        self.bond_yield = bond_yield

#Investor class with investor information attributes.                  
class Investor():
    #Initialization of the investor attributes.
    def __init__(self, investor_ID, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        
#Investor variable created with the inputs of investor information into the Investor class.
investor = Investor(1, 'Bob Smith', '207 South 9th Street', '123-454-1234')

filename_bond = 'Lesson6_Data - Bond.txt'
filename_stock = 'Lesson6_Data - Stocks.txt'

stock_list = []
bond_list = []
stock_information_dictionary = {}
bond_information_dictionary = {}
try:
    with open(filename_stock, 'r') as f_obj:
        lines = f_obj.read()
#If the file is not available let user know the wrong file name was input
except FileNotFoundError:
    print("sorry we don't have your file")
else:
    # Remove the new line charater out each line and store in a new list
    stock_list = lines.split("\n")
    
    purchase_ID = 1
    stock_list_index = 5
    stock_key_index = 0
    while stock_key_index < 8:
        while stock_list_index < len(stock_list):
            stock_information_dictionary['companies_stock_information_' + str(stock_key_index)] \
            = {'ID': purchase_ID, 
            stock_list[0]:stock_list[stock_list_index],
            stock_list[1]: int(stock_list[stock_list_index + 1]),
            stock_list[2]: float(stock_list[stock_list_index + 2]), 
            stock_list[3]: float(stock_list[stock_list_index + 3]), 
            stock_list[4]: stock_list[stock_list_index + 4]}
    
            purchase_ID += 1
            stock_list_index += 5
            stock_key_index += 1

try:
    with open(filename_bond, 'r') as f_obj:
        lines = f_obj.read()
#If the file is not available let user know the wrong file name was input
except FileNotFoundError:
    #Message produced if the file is not found.
    print("Sorry, please input valid file path.")
else:
    # Remove the new line charater out each line and store in a new list
    bond_list = lines.split("\n")
    
    purchase_ID = 10
    bond_list_index = 7
    
    if bond_list_index < len(stock_list):
        bond_information_dictionary['company_bond_information'] = {
        'ID': purchase_ID, bond_list[0]: bond_list[bond_list_index],
        bond_list[1]: int(bond_list[bond_list_index + 1]),
        bond_list[2]: float(bond_list[bond_list_index + 2]), 
        bond_list[3]: float(bond_list[bond_list_index + 3]), 
        bond_list[4]: bond_list[bond_list_index + 4],
        bond_list[5]: bond_list[bond_list_index+5], 
        bond_list[6]: bond_list[bond_list_index + 6]}
        
        purchase_ID += 1
        stock_list_index += 7    

# Initializes the filename that the file will be written to
filename = "Macejik.Cole.Assignment-report-6.txt"
# Open file in write mode creating the file and writing to the txt file
with open(filename, 'w') as f_obj:
# Major Heading displaying Bob Smith stock ownership information using columns.
    f_obj.write("Stock ownership for " + investor.name + "\n")
    f_obj.write("----------------------------------------\n")
    f_obj.write("STOCK		SHARE#		EARNING/LOSS            YEARLY%EARNINGS/LOSS\n")
    f_obj.write("----------------------------------------------------------------------------\n")
    # Loop through the stock information dictionary created earlier.
    for information_of_stock in stock_information_dictionary:
        #Looping through the stock information dictionary and
        # writing the stock information to text file named above.
        # The calculations are made from the Stock class methods for calculations
        portfolio = Stock(stock_information_dictionary[information_of_stock]['ID'],
        stock_information_dictionary[information_of_stock]['SYMBOL'], 
        stock_information_dictionary[information_of_stock]['NO_SHARES'],
        stock_information_dictionary[information_of_stock]['PURCHASE_PRICE'], 
        stock_information_dictionary[information_of_stock]['CURRENT_VALUE'],
        stock_information_dictionary[information_of_stock]['PURCHASE_DATE'])
        f_obj.write(portfolio.symbol + "\t\t" + str(portfolio.quantity) + "\t\t $" +
            str(round(portfolio.calculate_earnings_loss(),2)) + "\t\t" +
            str(round(portfolio.annual_earnings_calculation(),2)) + "%\n" )



#Major Heading displaying Bob Smith bond ownership information using columns.
    f_obj.write("\nBond ownership for " + investor.name + "\n")
    f_obj.write("----------------------------------------\n")
    f_obj.write("BOND		QUANTITY		EARNING/LOSS        YEARLY%EARNINGS/LOSS\n")
    f_obj.write("--------------------------------------------------------------------------------\n")
    for information_of_bond in bond_information_dictionary:
    # Looping through the bond information dictionary and
        # writing the bond information to text file named above.
        # The calculations are made from the Bond class methods for calculations
        bond_portfolio = Bond(bond_information_dictionary[information_of_bond]['ID'], 
        bond_information_dictionary[information_of_bond]['SYMBOL'], 
        bond_information_dictionary[information_of_bond]['NO_SHARES'], 
        bond_information_dictionary[information_of_bond]['PURCHASE_PRICE'],
        bond_information_dictionary[information_of_bond]['CURRENT_VALUE'],
        bond_information_dictionary[information_of_bond]['PURCHASE_DATE'],
        bond_information_dictionary[information_of_bond]['Coupon'],
        bond_information_dictionary[information_of_bond]['Yield'])
        f_obj.write(bond_portfolio.symbol + "\t\t" + str(bond_portfolio.quantity) +
        "\t\t\t" + str(round(bond_portfolio.calculate_earnings_loss(), 2)) +
        "\t\t\t" + str(round(bond_portfolio.annual_earnings_calculation(),2))
        + "%\n")



