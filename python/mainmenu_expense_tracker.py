from datetime import datetime
from expense_tracker import Expense, ExpenseTracker

# Main program class
class main:
    # Create an instance of the ExpenseTracker
    tracker = ExpenseTracker()

    #Start an infinite loop to continuously show the menu until user decides to exit
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Filter By Date")
        print("4. Filter By Category")
        print("5. Summary")
        print("6. Exit")

        #Prompt the user to choose a menu option
        choice = input("Choose any option (1-6):").strip()

        if choice=='1':
            print("Add Expense")
            try:
                # Gather input details from the user
                date= input("\nEnter date (YYYY-MM-DD):")
                amount= input("\nEnter amount ($):")
                category= input("\nEnter category (A/B/C):")
                description= input("\nEnter description:")

                # Create an Expense object and add it to the tracker
                expense = Expense(date,amount,category,description)
                tracker.add_expense(expense)
                print("\nSucessfully Added")

            except ValueError:
                print("\nInvalid input. Please follow the correct format.")
                    
        elif choice=='2':
            # Display all the recorded expenses
            print("View Expense")
            tracker.view_expenses()
        
        elif choice=='3':
            print("Filter By Date")
            try:
                # Ask the user for a date range(start and end date) to filter
                start= input("\nEnter start date (YYYY-MM-DD):")
                end= input("\nEnter end date (YYYY-MM-DD):")
                # Filter expenses and display results 
                results= tracker.filter_by_date(start,end)
                if results:
                    print("Match found.")
                    for exp in results:
                        print(exp)
                else:
                    print("No expenses found for that date range.")
                    
            except ValueError:
                print("\nInvalid input.Please follow the correct format.")


        elif choice=='4':
            # Ask the user for a category to filter
            print("\nFilter By Category")
            filter_category= input("Enter category (A/B/C):")
            results= tracker.filter_by_category(filter_category)
            # Filter expenses and display results 
            if results:
                print("Match found.")
                for exp in results:
                    print(exp)
            else:
                print("No expenses found for that category.")    

        elif choice=='5':
            # Display category-wise expense along with total expense summary
            print("Summary")
            tracker.summary()
        
        elif choice=='6':
            # Exit the loop and terminate the program
            print("Goodbye!")
            break

        else:
            # Handle invalid choice from menu options
            print("Something was wrong. Please Try Again!!!!")

            


