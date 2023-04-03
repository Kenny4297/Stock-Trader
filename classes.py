import random, json, questionary

class User:
    def __init__(self, name=None, wallet=0, user_stocks=[]):
        self.name = name
        self.wallet = wallet
        self.user_stocks = user_stocks

    def get_name(self):
        if self.name is None:
            self.name = input("What is your name? ")
    
    def buyStock(self):
        # do here















    # def buyStock(self):
    #     todays_stocks = Stock.getTodaysStocks()
    #     print(todays_stocks)

    #     company_to_buy = questionary.select(
    #         "What company would you like to buy?",
    #         choices=[list(company.keys())[0] for company in todays_stocks]
    #     ).ask()

    #     # Find the selected company in the todays_stocks list and get its price
    #     current_price = None
    #     for company in todays_stocks:
    #         if list(company.keys())[0] == company_to_buy:
    #             current_price = list(company.values())[0]
    #             break

    #     number_of_stocks_to_buy = input("How many stocks would you like to buy")

    #     self.user_stocks.append({
    #         "company": company_to_buy,
    #         "price": current_price,
    #         "stocks purchased": number_of_stocks_to_buy
    #     })

        print(f"{self.user_stocks}")





    # A testing method used to check the users name and wallet amount
    def userStockInfo(self):
        """
        Prints to the user all the information regarding their stocks
        Example: Your stocks: [list of just the name of the stocks]
        """
        print(f"Your current data: {self.wallet}, {self.user_stocks}")


    def __str__(self):
        return f"Name: {self.name}, Wallet Balance: {self.wallet}"
    

class Stock:
    def __init__(self):
        pass

    def getTodaysStocks():
        """
        This return the stocks that are available for purchasing today in an object array, from 'list_of_companies.
        Return Example: [{'Altria Group': 405}, {'Danaher': 359}] 
        """
        with open ('list_of_companies.json', 'r') as list_of_companies:
            # Don't forget to load the companies themselves! You can't loop though 'list_of_companies!
            data = json.load(list_of_companies)

            todays_stocks = []

            # Loop through the list of stocks and randomly select 5 of them
            while len(todays_stocks) < 5:
                company, stock_value = random.choice(list(data.items()))

                todays_stocks.append({company: stock_value})
        
        return todays_stocks  
        # Return Example: [{'Altria Group': 405}, {'Danaher': 359}] 
    


