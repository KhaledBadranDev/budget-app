class Category:
    def __init__(self, name: str):
        """
        Initialize the Category with a name and an empty ledger.
        """
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description: str = ""):
        """
        Add a deposit to the ledger.
        Default description is an empty string.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        """
        Withdraw an amount if funds are available.
        Stored as a negative number in the ledger.
        Returns True if successful, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        """
        Return the current balance of the budget category.
        """
        total_balance = 0
        for item in self.ledger:
            total_balance += item["amount"]
        return total_balance

    def transfer(self, amount: float, category) -> bool:
        """
        Transfer funds from this category to another category.
        Returns True if successful, False otherwise.
        """
        # We must check if we have enough funds first
        if self.check_funds(amount):
            # Withdraw from current category
            self.withdraw(amount, f"Transfer to {category.name}")
            # Deposit to target category
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        """
        Check if the amount is less than or equal to the current balance.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Return a formatted string representation of the ledger.
        """
        # 1. Title line: 30 chars, centered with *
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        
        for item in self.ledger:
            # 2. Description: Left aligned, max 23 chars
            # 3. Amount: Right aligned, 2 decimal places, max 7 chars
            description = f"{item['description'][:23]:<23}"
            amount = f"{item['amount']:>7.2f}"
            items += f"{description}{amount}\n"
            total += item["amount"]
            
        # 4. Total line
        output = title + items + "Total: " + str(total)
        return output

# --- Driver Code (for testing Phase 1) ---
if __name__ == "__main__":
    # This matches the example usage in the plan
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    
    print(food)
    print(clothing)