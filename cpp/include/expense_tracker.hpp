#ifndef EXPENSE_TRACKER_HPP
#define EXPENSE_TRACKER_HPP

#include <chrono>
#include <iostream>
#include <string>
#include <memory>
#include <vector>

class Expense {

public:
Expense(char category, std::string&& description, double amount, const std::chrono::time_point<std::chrono::system_clock>
 datetime = std::chrono::system_clock::now());

Expense() = delete;

private:
const std::chrono::time_point<std::chrono::system_clock> dayMonthYear_;
double amount_;
char category_;
std::string description_;

};

class ExpenseTracker {

public:
ExpenseTracker(const std::string& name);
ExpenseTracker() = delete;

void addExpense(Expense&& expense);
void view() const;
void view(const std::chrono::time_point<std::chrono::system_clock>& startDate, 
          const std::chrono::time_point<std::chrono::system_clock>& endDate) const;
void view(char category) const;
void summary() const;
void summary(const std::chrono::time_point<std::chrono::system_clock>& startDate, 
             const std::chrono::time_point<std::chrono::system_clock>& endDate) const;
void summary(char category) const;

private:
std::string name_;
std::vector<std::shared_ptr<Expense>> expenses_;

std::vector<std::shared_ptr<Expense>> filterByDateTime(
    const std::chrono::time_point<std::chrono::system_clock>& startDate, 
    const std::chrono::time_point<std::chrono::system_clock>& endDate) const;
std::vector<std::shared_ptr<Expense>> filterByCategory(char category) const;

};
#endif // EXPENSE_TRACKER_HPP