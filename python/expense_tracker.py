from datetime import datetime

class Expense:
    """
    Represents a single expense entry with attributes for date, amount, category, and description.
    """
    def __init__(self, date, amount, category, description):
        # Convert string to datetime for consistent date operations
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = float(amount)
        self.category = category.strip()
        self.description = description.strip()

    def __str__(self):
        """
        Return a nicely formatted string representation of the expense.
        """
        return f"{self.date.date()} | ${self.amount:.2f} | {self.category} | {self.description}"


class ExpenseTracker:
    """
    Manages a collection of Expense objects and provides operations to add, view, filter, and summarize expenses.
    """
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """
        Add an Expense object to the list of tracked expenses.
        """
        self.expenses.append(expense)

    def view_expenses(self):
        """
        Display all recorded expenses.
        """
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for exp in self.expenses:
                print(exp)

    def filter_by_date(self, start_date, end_date):
        """
        Return a list of expenses within the specified date range (inclusive).
        """
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        filtered_expenses = [
            exp for exp in self.expenses
            if start <= exp.date <= end
        ]
        return filtered_expenses

    def filter_by_category(self, category):
        """
        Return a list of expenses that match the specified category (case-insensitive).
        """
        category = category.lower().strip()
        filtered_expenses = [
            exp for exp in self.expenses
            if exp.category.lower() == category
        ]
        return filtered_expenses

    def summary(self):
        """
        Print the total expenses and a breakdown by category.
        """
        if not self.expenses:
            print("No expenses to summarize.")
            return

        total = 0.0
        category_totals = {}

        for exp in self.expenses:
            total += exp.amount
            cat = exp.category
            if cat in category_totals:
                category_totals[cat] += exp.amount
            else:
                category_totals[cat] = exp.amount

        print("Summary by Category:")
        for category, amount in category_totals.items():
            print(f"- {category}: ${amount:.2f}")
        print(f"\nTotal Expenses Summary: ${total:.2f}")

