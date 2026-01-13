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
        output = title + items + "Total: " + f"{total:.2f}"
        return output


def create_spend_chart(categories):
    """
    Create a bar chart string showing percentage spent by category.
    """
    # 1. Calculate spending for each category
    spend = []
    for cat in categories:
        total_cat_spend = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                total_cat_spend += abs(item['amount'])
        spend.append(total_cat_spend)

    # 2. Calculate percentages (rounded down to nearest 10)
    total_spend = sum(spend)
    if total_spend > 0:
        percentages = [(amount / total_spend) * 100 for amount in spend]
    else:
        percentages = [0 for _ in spend]
    
    # Floor to nearest 10 (e.g., 29 -> 20)
    percentages = [int(p // 10) * 10 for p in percentages]

    # 3. Build the chart string
    output = "Percentage spent by category\n"
    
    # Vertical bars (100 down to 0)
    for i in range(100, -1, -10):
        # Format "100| ", " 90| ", etc.
        output += f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                output += "o  "
            else:
                output += "   "
        output += "\n"

    # 4. Horizontal dash line
    # 4 spaces indent, plus 3 dashes per category, plus 1 extra dash
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Vertical names
    # Find longest name to determine number of rows
    max_length = max([len(cat.name) for cat in categories])
    names = [cat.name for cat in categories]

    for i in range(max_length):
        output += "     " # 5 spaces indent for names
        for name in names:
            if i < len(name):
                output += f"{name[i]}  "
            else:
                output += "   "
        
        # Add newline only if it's not the last line
        if i < max_length - 1:
            output += "\n"

    return output


# --- Driver Code (for testing Phase 2) ---
if __name__ == "__main__":
    # Setup categories
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    
    auto = Category('Auto')
    auto.deposit(1000, 'initial deposit')
    auto.withdraw(15)

    # Print individual categories (Phase 1 check)
    print(food)
    print(clothing)
    print(auto)

    # Print the chart (Phase 2 check)
    print(create_spend_chart([food, clothing, auto]))