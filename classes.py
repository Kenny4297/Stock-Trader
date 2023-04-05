import random, json, questionary

class User:
    def __init__(self, name=None, wallet=0, user_stocks=[]):
        self.name = name
        self.wallet = wallet
        self.user_stocks = user_stocks

    def get_name(self):
        if self.name is None:
            self.name = input("What is your name? ")
    
    # A testing method used to check the users name and wallet amount
    def userStockInfo(self):
        """
        Prints to the user all the information regarding their stocks
        Example: Your stocks: [list of just the name of the stocks]
        """
        print(f"Your current data: {self.wallet}, {self.user_stocks}")

    def buyStock(self):
        pass
        # Get the list of stocks that are available for purchase
        todays_stocks = Stock.getTodaysStocks()

        # Get the company names ready
        company_names = [list(company.keys())[0] for company in todays_stocks]

        # Ask the user what company they would like to buy
        company_to_purchase = questionary.select(
            "What company would you like to buy?",
            choices=[company_names]
        ).ask()

        # Ask how many they would like to buy
        amount_to_purchase = int(input("How many would you like to purchase? "))

        # Get the stock price of the company they bought
        stock_price = None
        for company in todays_stocks:
            if list(company.keys())[0] == company_to_purchase:
                stock_price = todays_stocks[company_to_purchase]
                break

        # Create a new 'stock' object that will be added to the json file that contains the array of users stocks
        stock = {
            "name": company_to_purchase,
            "price": stock_price,
            "amount": amount_to_purchase
        }
        # Open the json file

        with open ('users.json', 'r') as file:
            users = json.load(file)
        
        # Loop through the json file to find the correct user
        for user in users:
            if user['name'] == self.name:
                if 'user_stocks':
                    user['user_stocks'].append(stock)
                else:
                    user['user_stocks'] = [stock]
                    break
        
        with open('users.json', 'w') as file:
            json.dump(user, file)
        
        print(f"{user}")
        

    def __str__(self):
        return f"Name: {self.name}, Wallet Balance: {self.wallet}, Stocks Purchased: {self.user_stocks}"
    

    

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
    


