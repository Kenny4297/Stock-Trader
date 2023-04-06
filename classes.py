import random, json, questionary

class User:
    def __init__(self, name=None, wallet=0, user_stocks=None):
        if user_stocks is None:
            user_stocks = []
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

        # First we need to get Today's available stocks. Remember that this returns a JSON object.
        todays_stocks = Stock.getTodaysStocks()

        # Now we need to have the user select, from the stocks, the name of the company they would like to purchase
        company_to_buy = questionary.select(
            "Which company would you like to buy?",
            # loop through the 'todays_stocks' and print out the keys as the choices
            # Again, the [0] is targeting the companies 'name', which is the first key in the object
            choices=[list(companies.keys())[0] for companies in todays_stocks]
        ).ask()

        amount_to_buy = int(input("How many stocks would you like to buy?"))

        # Now that a company is selected, we need to get its value

        company_value = None
        for company in todays_stocks:
            # The [0] here refers to the first key in the dictionary object, which is the company name
            if list(company.keys())[0] == company_to_buy:
                company_value = company[company_to_buy]
                break
        
        # Create the object that will be added to the 'user_stocks'
        stock = {
            "name": company_to_buy,
            "price": company_value,
            "amount": amount_to_buy
        }

        # Open the 'users.json' file 
        with open('users.json', 'r') as file:
            users = json.load(file)

        # Find the correct user to add the user_stocks to
        for user in users:
            if user['name'] == self.name:

                # Check if the user already has user_stocks
                if 'user_stocks' in user:
                    user['user_stocks'].append(stock)
                else:
                    user['user_stocks'] = [stock]
                break
            
        with open('users.json', 'w') as file:
            json.dump(users, file)

        print(f"{user}")
    
    def sellStock(self):
        # Open the 'users.json' file 
        with open('users.json', 'r') as file:
            users = json.load(file)

        # Find the correct user in the json file
        for user in users:
            if user['name'] == self.name:
                # Check if the user has any stocks to sell
                if 'user_stocks' not in user:
                    print("You have no stocks to sell!")
                    return

                # Prompt the user to select which stock they want to sell
                stock_choices = [stock['name'] for stock in user['user_stocks']]
                stock_to_sell = questionary.select(
                    "Which stock do you want to sell?",
                    choices=stock_choices
                ).ask()

                # Display the current number of shares the user owns
                current_shares = next(stock['amount'] for stock in user['user_stocks'] if stock['name'] == stock_to_sell)
                print(f"You currently own {current_shares} shares of {stock_to_sell}.")

                # Prompt the user to enter how many shares they want to sell
                stock_amount = questionary.text(
                    f"How many shares of {stock_to_sell} do you want to sell?"
                ).ask()

                # Check if the user has enough shares to sell
                for stock in user['user_stocks']:
                    if stock['name'] == stock_to_sell:
                        if stock['amount'] < int(stock_amount):
                            print("You don't have enough shares to sell!")
                            return

                # Update the user's wallet and stocks
                for stock in user['user_stocks']:
                    if stock['name'] == stock_to_sell:
                        stock_value = stock['price'] * int(stock_amount)
                        user['wallet'] += stock_value
                        stock['amount'] -= int(stock_amount)
                        if stock['amount'] == 0:
                            user['user_stocks'].remove(stock)

                # Save the changes to the json file
                with open('users.json', 'w') as file:
                    json.dump(users, file)

                print(f"You have sold {stock_amount} shares of {stock_to_sell} for {stock_value} dollars.")

                return
        print("User not found in users.json.")

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
    


