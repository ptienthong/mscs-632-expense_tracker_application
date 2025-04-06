from datetime import datetime

class ExpenseTracker:
    """
    Tracks expenses using a list of dictionaries.
    Each expense is a dictionary with keys: date, amount, category, description.
    """
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):
        """
        Adds a new expense dictionary to the list.
        """
        expense = {
            "date": datetime.strptime(date, "%Y-%m-%d"),
            "amount": float(amount),
            "category": category.strip(),
            "description": description.strip()
        }
        self.expenses.append(expense)

    def view_expenses(self):
        """
        Prints all recorded expenses.
        """
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Date | Amount | Category | Description")
        for exp in self.expenses:
            print(f"{exp['date'].date()} | ${exp['amount']:.2f} | {exp['category']} | {exp['description']}")

    def filter_by_date(self, start_date, end_date):
        """
        Filters and returns expenses within the specified date range.
        """
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return [
            exp for exp in self.expenses
            if start <= exp["date"] <= end
        ]

    def filter_by_category(self, category):
        """
        Filters and returns expenses matching the given category.
        """
        category = category.lower().strip()
        return [
            exp for exp in self.expenses
            if exp["category"].lower() == category
        ]

    def summary(self):
        """
        Prints a total summary and category-wise breakdown.
        """
        if not self.expenses:
            print("No expenses to summarize.")
            return

        total = 0.0
        category_totals = {}

        for exp in self.expenses:
            total += exp["amount"]
            cat = exp["category"]
            category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

        print("Summary by Category:")
        for category, amount in category_totals.items():
            print(f"- {category}: ${amount:.2f}")
        print(f"\nTotal Expenses Summary: ${total:.2f}")
