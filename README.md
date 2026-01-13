# Budget App

A Python-based budget application that tracks spending across different categories and visualizes expenditure percentages using a bar chart.


## Features


### 1. Category Manager
The `Category` class allows you to instantiate different budget buckets (e.g., Food, Clothing).
- **Deposit**: Add funds to the category.
- **Withdraw**: Remove funds (if balance permits).
- **Transfer**: Move funds between categories.
- **Check Funds**: Verify if a transaction is possible.
- **Print Ledger**: Printing the object displays a formatted receipt of all transactions.


### 2. Spend Chart
The `create_spend_chart` function takes a list of categories and produces a text-based bar chart representing the percentage of total spending derived from each category.


## Example Output
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
***********Clothing***********
Transfer from Food       50.00
                        -25.55
Total: 24.45
*************Auto*************
initial deposit        1000.00
                        -15.00
Total: 985.00
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
```

## Tech Stack

* Python 3

## Usage

Run the main script to see the output:

```bash
python main.py
```

## License

This project is licensed under the [MIT License](LICENSE).
