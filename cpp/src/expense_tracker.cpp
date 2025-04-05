#include "expense_tracker.hpp"
#include <iostream>
#include <ctime>
#include <string_view>
#include <ranges>

// Expense Class Methods

//Constructor for Expense Class
// It initilizes the fields with vlaues passed in, using move semantics for description
Expense::Expense(char category, std::string&& description, double amount, const std::chrono::time_point<std::chrono::system_clock> datetime)
    : dayMonthYear_(datetime), amount_(amount), category_(category), description_(std::move(description)) {
}

//Constructor for ExpenseTracker, intializes the name an prints the message
ExpenseTracker::ExpenseTracker(const std::string& name) : name_(name) {
    std::cout << "Expense Tracker created for: " << name_ << '\n';
}

//add a new expense to the tracker by using shared_ptr to manage the memory safely and efficiently
void ExpenseTracker::addExpense(Expense&& expense) {
    categories_.insert(expense.getCategory());
    expenses_.emplace_back(std::make_shared<Expense>(std::move(expense)));
    std::cout << "Expense added for " << name_ << '\n';
}

//Display all the expenses recorded so far
void ExpenseTracker::view() const {
    std::cout << "Viewing all expenses for " << name_ << '\n';
    for (const auto& expense : expenses_) {

        //convert chronological time_point to tm for human-readable date
        const std::time_t t_c = std::chrono::system_clock::to_time_t(expense->getDateTime());
        const std::tm* ptm = std::localtime(&t_c);
        
        int year  = ptm->tm_year + 1900; // tm_year is years since 1900
        int month = ptm->tm_mon + 1;     // tm_mon is 0-based (0 = January)
        int day   = ptm->tm_mday;

        //print formatted expense details
        std::cout << "YYYY-MM-DD: "<< year << "-" << month << "-" << day << 
                     ", Category: " << expense->getCategory() << 
                     ", Description: " << expense->getDescription() << 
                     ", Amount: " << expense->getAmount() << '\n';
    }
}

//view expenses by date range
void ExpenseTracker::view(std::string& startDate, 
                           std::string& endDate) const {
    std::cout << "Viewing expenses for " << name_ << " between specified dates" << "\n";
    auto filteredExpenses = filterByDateTime(startDate, endDate);
    if (filteredExpenses.empty()) {
        std::cout << "No expenses found in this date range.\n";
        return;
    }
    for (const auto& expense : filteredExpenses) {
        const std::time_t t_c = std::chrono::system_clock::to_time_t(expense->getDateTime());
        const std::tm* ptm = std::localtime(&t_c);
        
        int year  = ptm->tm_year + 1900; // tm_year is years since 1900
        int month = ptm->tm_mon + 1;     // tm_mon is 0-based (0 = January)
        int day   = ptm->tm_mday;

        std::cout << "YYYY-MM-DD: "<< year << "-" << month << "-" << day << 
                     ", Category: " << expense->getCategory() << 
                     ", Description: " << expense->getDescription() << 
                     ", Amount: " << expense->getAmount() << '\n';
    }

}

//view expenses by category
void ExpenseTracker::view(char category) const {
    std::cout << "Viewing expenses for " << name_ << " in category: " << category << '\n';
    auto filteredExpenses = filterByCategory(category);
    if (filteredExpenses.empty()) {
        std::cout << "No expenses found in this category.\n";
        return;
    }
    for (const auto& expense : filteredExpenses) {
        const std::time_t t_c = std::chrono::system_clock::to_time_t(expense->getDateTime());
        const std::tm* ptm = std::localtime(&t_c);
        
        int year  = ptm->tm_year + 1900; // tm_year is years since 1900
        int month = ptm->tm_mon + 1;     // tm_mon is 0-based (0 = January)
        int day   = ptm->tm_mday;

        std::cout << "YYYY-MM-DD: "<< year << "-" << month << "-" << day << 
                     ", Category: " << expense->getCategory() << 
                     ", Description: " << expense->getDescription() << 
                     ", Amount: " << expense->getAmount() << '\n';
    }
}

//summary of all expenses
void ExpenseTracker::summary() const {
    
    for (const char& category : categories_) {
        summary(category);
    }

    double total = 0;
    for (const auto& expense : expenses_) {
        total += expense->getAmount();
    }
    std::cout << "Total amount spent: " << total << "$" << '\n';
}

//summary of all expenses within a given date range
void ExpenseTracker::summary(std::string& startDate, 
                              std::string& endDate) const {
    std::cout << "Total expenses for " << name_ << " between specified dates << \n";
    auto filteredExpenses = filterByDateTime(startDate, endDate);
    double total = 0;
    for (const auto& expense : filteredExpenses) {
        total += expense->getAmount();
    }
    std::cout << "Total amount spent: " << total << '\n';
}

//summary of all expenses in a category
void ExpenseTracker::summary(char category) const {
    auto filteredExpenses = filterByCategory(category);
    if (filteredExpenses.empty()) {
        std::cout << "No expenses found in this category.\n";
        return;
    }
    double total = 0;
    for (const auto& expense : filteredExpenses) {
        total += expense->getAmount();
    }
    std::cout << category << ": " << total << "$" <<'\n';
}

//helper method to filter expenses by date range
std::vector<std::shared_ptr<Expense>> ExpenseTracker::filterByDateTime(
    std::string startDate, 
    std::string endDate) const {
    
    // try and catch block to check if the date is in the correct format
    try {
        auto isValidDate = [](const std::string& date) {
            if (date.size() != 10) throw std::invalid_argument("Invalid date length");
            if (!std::isdigit(date[0]) || !std::isdigit(date[1]) || 
                !std::isdigit(date[2]) || !std::isdigit(date[3])) throw std::invalid_argument("Invalid year format");
            if (date[4] != '-') throw std::invalid_argument("Missing '-' after year");
            if (!std::isdigit(date[5]) || !std::isdigit(date[6])) throw std::invalid_argument("Invalid month format");
            if (date[7] != '-') throw std::invalid_argument("Missing '-' after month");
            if (!std::isdigit(date[8]) || !std::isdigit(date[9])) throw std::invalid_argument("Invalid day format");
            return true;
        };

        isValidDate(startDate);
        isValidDate(endDate);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: Invalid date format. " << e.what() << " Expected format is YYYY-MM-DD.\n";
        return {};
    }
    // extract year of start date and end date
    std::tm startTm = {}, endTm = {};

    auto splitDate = [](const std::string& date) {
        std::vector<int> parts;
        size_t start = 0, end = 0;
        while ((end = date.find('-', start)) != std::string::npos) {
            parts.push_back(std::stoi(date.substr(start, end - start)));
            start = end + 1;
        }
        parts.push_back(std::stoi(date.substr(start)));
        return parts;
    };

    auto startParts = splitDate(startDate);
    auto endParts = splitDate(endDate);

    startTm.tm_year = startParts[0]; // Year since 1900
    startTm.tm_mon = startParts[1];     // Month is 0-based
    startTm.tm_mday = startParts[2];
    auto startday = startTm.tm_mday;
    auto startmonth = startTm.tm_mon;
    auto startyear = startTm.tm_year;

    endTm.tm_year = endParts[0] ; // Year since 1900
    endTm.tm_mon = endParts[1];     // Month is 0-based
    endTm.tm_mday = endParts[2];
    auto endday = endTm.tm_mday;
    auto endmonth = endTm.tm_mon;
    auto endyear = endTm.tm_year;
    
    std::vector<std::shared_ptr<Expense>> filteredExpenses;
    for (const auto& expense : expenses_) {
        
        // extract datetime from getDateTime() the year, month, and day
        const std::time_t t_c = std::chrono::system_clock::to_time_t(expense->getDateTime());
        const std::tm* ptm = std::localtime(&t_c);
        
        int year  = ptm->tm_year + 1900; // tm_year is years since 1900
        int month = ptm->tm_mon + 1;     // tm_mon is 0-based (0 = January)
        int day   = ptm->tm_mday;
        
        std::cout << year << " " << month << " " << day << "\n";
        //check if date is within the given range
        if (year >= startyear && year <= endyear) {
            if (month >= startmonth && month <= endmonth) {
                if (day >= startday && day <= endday) {
                    filteredExpenses.push_back(expense);
                }
            }
            
        }
    }
    return filteredExpenses;
}

//helper method to filter expenses by category
std::vector<std::shared_ptr<Expense>> ExpenseTracker::filterByCategory(char category) const {
    std::vector<std::shared_ptr<Expense>> filteredExpenses;
    for (const auto& expense : expenses_) {
        if (expense->getCategory() == category) {
            filteredExpenses.push_back(expense);
        }
    }
    return filteredExpenses;
}

