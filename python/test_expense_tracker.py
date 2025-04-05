from datetime import datetime

class Expense:
    """
    Represents a single expense entry with attributes for date, amount, category, and description.
    """
    def __init__(self,date, amount, category, description):
        # Convert string to datetime for consistent date operations
        self.date = datetime.strptime(date,"%Y-%m-%d")
        self.amount = float(amount)
        self.category = category.strip()
        self.description = description.strip()

    """
    Return a nicely formatted string representation of the expense.
    """
    def __str__(self):
        return f"{self.date.date()} | ${self.amount:.2f} | {self.category} | {self.description}"
    

class ExpenseTracker:
    """
    Manages a collection of Expense objects and provides operations to add, view, filter, and summarize expenses.
    """
    def __init__(self):
        self.expenses=[]

    """
    Add an Expense object to the list of tracked expenses.
    """
    def addExpense(self,expense):
        self.expenses.append(expense)

    """
    Display all recorded expenses.
    """
    def viewExpense(self,expense):
        for exp in self.expenses:
            print(exp)

    """
    Return a list of expenses within the specified date range (inclusive).
    """
    def filterByDate(self,startdate,enddate):
        start = datetime.strptime(startdate,"%Y-%m-%d")
        end = datetime.strptime(enddate,"%Y-%m-%d")
        filteredExpenses = [
            exp for exp in self.expenses
            if start <= exp.date <= end
        ] 
        return filteredExpenses
    
    """
    Return a list of expenses that match the specified category (case-insensitive).
    """
    def filterByCategory(self,category):
        category= category.lower().strip()
        filteredExpenses = [
            exp for exp in self.expenses
            if exp.category.exp == category
        ]
        return filteredExpenses
    
    """
    Print the total expenses and a breakdown by category.
    """
    def summary(self):
        total = 0.0
        categoryTotals = {}
        
        if not self.expenses:
            print("No expenses to summarize.")

        for exp in self.expenses:
            total += exp.amount
            cat = exp.category
            if cat in categoryTotals:
                categoryTotals[cat] += exp.amount
            else:
                categoryTotals[cat] = exp.amount
        
        print("Summary  by Category")
        for category,amount  in categoryTotals.items():
            print(f"- {category}: ${amount:.2f}")
        print(f"\nTotal Expenses Summary: ${total:.2f}")
        

