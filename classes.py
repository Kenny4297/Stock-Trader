import random, json

class User:
    def __init__(self, name=None, wallet=0):
        self.name = name
        self.wallet = wallet

    def get_name(self):
        if self.name is None:
            self.name = input("What is your name? ")
    
    def buyStock():
        # Asks the user what company they want to buy from

        # Asks the user how many stocks they want to buy

        # 
        numberOfStocks = int(input("How many stocks would you like to buy?"))


    # A testing method used to check the users name and wallet amount
    def userStockInfo():
        """
        Prints to the user all the information regarding their stocks
        Example: Your stocks: [list of just the name of the stocks]
        """


    def __str__(self):
        return f"Name: {self.name}, Wallet Balance: {self.wallet}"
    

class Stock:
    def __init__(self):
        pass

    def getTodaysStocks():
        """
        This return the stocks that are available for purchasing today in an object array, from 'list_of_companies
        Example: [{'Altria Group': 405}, {'Danaher': 359}] 
        """
        with open ('list_of_companies.json', 'r') as list_of_companies:
            # Don't forget to load the companies themselves! You can't loop though 'list_of_companies!
            data = json.load(list_of_companies)

            todays_stocks = []

            # Loop through the list of stocks and randomly select 5 of them
            while len(todays_stocks) <= 5:
                company, stock_value = random.choice(list(data.items()))

                todays_stocks.append({company: stock_value})
        
        return todays_stocks  
    


print(getStocks())


