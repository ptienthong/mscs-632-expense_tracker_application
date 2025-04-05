from datetime import datetime
from expense_tracker import Expense, ExpenseTracker

class main:
    tracker = ExpenseTracker()



    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Filter By Date")
        print("4. Filter By Category")
        print("5. Summary")
        print("6. Exit")

        
        choice = input("Choose any option (1-6):").strip()

        if choice=='1':
            print("Add Expense")
            try:
                date= input("\n Enter date (YYYY-MM-DD):")
                amount= input("\n Enter amount ($):")
                category= input("\nEnter category (A,B,C,D):")
                description= input("\nEnter description:")

                expense = Expense(date,amount,category,description)
                tracker.add_expense(expense)
                print("\nSucessfully Added")

            except ValueError:
                print("\n Invalid input.")
                    
        elif choice=='2':
            print("View Expense")
            tracker.view_expenses()
        
        elif choice=='3':
            print("Filter By Date")
            try:
                start= input("\n Enter date (YYYY-MM-DD):")
                end= input("\n Enter date (YYYY-MM-DD):")
                results= tracker.filter_by_date(start,end)
                if results:
                    for exp in results:
                        print(exp)
                else:
                    print("No expenses found for that date range.")
                    
            except ValueError:
                print("\n Invalid input")


        elif choice=='4':
            
            print("\nFilter By Category")
            filter_category= input("Enter category (A,B,C,D):")
            results= tracker.filter_by_category(filter_category)
            if results:
                for exp in results:
                    print(exp)
            else:
                print("No expenses found for that category.")    


        elif choice=='5':
            print("Summary")
            tracker.summary()
        
        elif choice=='6':
            print("Goodbye!")
            break

        else:
            print("Something was wrong. Please Try Again!!!!")

            


