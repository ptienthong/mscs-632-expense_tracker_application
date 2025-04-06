from expense_tracker_dict import ExpenseTracker

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu (Dictionary-Based)")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Date Range")
        print("4. Filter by Category")
        print("5. Summary")
        print("6. Exit")

        choice = input("Choose an option (1–6): ").strip()

        if choice == '1':
            print("\nAdd Expense")
            try:
                date = input("Enter date (YYYY-MM-DD): ")
                amount = input("Enter amount: ")
                category = input("Enter category (A/B/C): ")
                description = input("Enter description: ")
                tracker.add_expense(date, amount, category, description)
                print("Expense successfully added.")
            except ValueError:
                print("Invalid input. Please follow the correct format.")

        elif choice == '2':
            print("\nView All Expenses")
            tracker.view_expenses()

        elif choice == '3':
            print("\nFilter by Date Range")
            try:
                start = input("Enter start date (YYYY-MM-DD): ")
                end = input("Enter end date (YYYY-MM-DD): ")
                results = tracker.filter_by_date(start, end)
                if results:
                    for exp in results:
                        print(f"{exp['date'].date()} | ${exp['amount']:.2f} | {exp['category']} | {exp['description']}")
                else:
                    print("No expenses found in that date range.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == '4':
            print("\nFilter by Category")
            category = input("Enter category (A/B/C): ")
            results = tracker.filter_by_category(category)
            if results:
                for exp in results:
                    print(f"{exp['date'].date()} | ${exp['amount']:.2f} | {exp['category']} | {exp['description']}")
            else:
                print("No expenses found for that category.")

        elif choice == '5':
            print("\nSummary")
            tracker.summary()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
