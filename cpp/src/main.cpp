#include "expense_tracker.hpp"
#include <iostream>


int main(){
    auto tracker = ExpenseTracker("John Doe");

    while (true)
    {
        std::cout << "Expense Tracker Menu:\n";
        std::cout << "1. Add Expense\n";
        std::cout << "2. View Expenses\n";
        std::cout << "3. View Expenses by Date\n";
        std::cout << "4. View Expenses by Category\n";
        std::cout << "5. Summary\n";
        std::cout << "6. Exit\n";

        std::cout << "Choose an option (1-6): ";
        int choice;
        std::cin >> choice;

        if (choice == 1) {
            char category;
            std::string description;
            double amount;

            std::cout << "Enter category (A/B/C): ";
            std::cin >> category;
            std::cout << "Enter description: ";
            std::cin.ignore(); // Ignore the newline character left in the buffer
            std::getline(std::cin, description);
            std::cout << "Enter amount ($): ";
            std::cin >> amount;

            tracker.addExpense(Expense(category, std::move(description), static_cast<double>(amount)));
        } else if (choice == 2) {
            tracker.view();
        } else if (choice == 3) {
            // Implement date range input and view
            std::cout << "Enter start date (YYYY-MM-DD): ";
            std::cin.ignore();
            std::string startDate;
            std::getline(std::cin, startDate);
            std::cout << "Enter end date (YYYY-MM-DD): ";
            std::string endDate;
            std::getline(std::cin, endDate);
            tracker.view(startDate, endDate);

        } else if (choice == 4) {
            char category;
            std::cout << "Enter category (A/B/C): ";
            std::cin >> category;
            tracker.view(category);
        } else if (choice == 5) {
            tracker.summary();
        } else if (choice == 6) {
            std::cout << "Exiting...\n";
            break;
        } else {
            std::cout << "Invalid choice. Please try again.\n";
            std::cout << "Choose an option (1-6): ";
            std::cin >> choice;
        }
        std::cout << "\n";
        std::cout << "---------------------------------\n";
    }
    


    return 0;
}