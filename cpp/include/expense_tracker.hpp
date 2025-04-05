// This header file defines the data model and core class interfaces for the C++ version of the Expense Tracker Application.
#ifndef EXPENSE_TRACKER_HPP
#define EXPENSE_TRACKER_HPP

#include <chrono>
#include <iostream>
#include <string>
#include <memory>
#include <vector>

// Expense class: represents a single expense with category, description, amount, and time.
// Default time is set to current if not provided.
class Expense {

public:
Expense(char category, std::string&& description, double amount, const std::chrono::time_point<std::chrono::system_clock>
 datetime = std::chrono::system_clock::now());

Expense(Expense&&) = default;

Expense() = delete;

double getAmount() const { return amount_; }
std::string getDescription() const { return description_; }
char getCategory() const { return category_; }
std::chrono::time_point<std::chrono::system_clock> getDateTime() const { return dayMonthYear_; }

private:
const std::chrono::time_point<std::chrono::system_clock> dayMonthYear_;
double amount_;
char category_;
std::string description_;

};

//Class : ExpenseTracker
// This class stores and manages a collection of Expense objects.
// It provides functions for viewing, filtering, and summerizing the expenses.
class ExpenseTracker {

public:
ExpenseTracker(const std::string& name);
ExpenseTracker() = delete;

void addExpense(Expense&& expense);
void view() const;
void view(std::string& startDate, 
          std::string& endDate) const;
void view(char category) const;
void summary() const;
void summary(std::string& startDate, 
             std::string& endDate) const;
void summary(char category) const;

private:
std::string name_;
std::vector<std::shared_ptr<Expense>> expenses_;

std::vector<std::shared_ptr<Expense>> filterByDateTime(
    std::string startDate, 
    std::string endDate) const;
std::vector<std::shared_ptr<Expense>> filterByCategory(char category) const;

};
#endif // EXPENSE_TRACKER_HPP
