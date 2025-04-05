#include "expense_tracker.hpp"
#include <gtest/gtest.h>
#include <chrono>
#include <string>
#include <memory>

//create a test fixture if you need shared setup
class ExpenseTrackerTest : public ::testing::Test {


    protected:
    ExpenseTracker tracker{"Test Tracker"};
    
    void SetUp() override {
        using namespace std::chrono;

        auto now = system_clock::now();
        tracker.addExpense(Expense('F', "Food", 20.5, now));
        tracker.addExpense(Expense('T', "Transport", 10.0, now));
        tracker.addExpense(Expense('F', "Dinner", 15.0, now));
    }
};

// Test: Expense initialization
TEST(ExpenseTest, InitializesCorrectly) {
    using namespace std::chrono;
    auto now = system_clock::now();

    Expense exp('H', "Hotel", 100.0, now);

    EXPECT_EQ(exp.getCategory(), 'H');
    EXPECT_EQ(exp.getDescription(), "Hotel");
    EXPECT_DOUBLE_EQ(exp.getAmount(), 100.0);
}

// Test: Add and view expenses
TEST_F(ExpenseTrackerTest, AddAndViewExpenses) {
    // The setup already adds 3 expenses
    testing::internal::CaptureStdout();
    tracker.view();
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("Food") != std::string::npos);
    EXPECT_TRUE(output.find("Transport") != std::string::npos);
}

// Test: Filter by category
TEST_F(ExpenseTrackerTest, FilterByCategory) {
    auto filtered = tracker.filterByCategory('F');
    ASSERT_EQ(filtered.size(), 2);
    EXPECT_EQ(filtered[0]->getCategory(), 'F');
}

// Test: Summary by category
TEST_F(ExpenseTrackerTest, SummaryByCategory) {
    testing::internal::CaptureStdout();
    tracker.summary('F');
    std::string output = testing::internal::GetCapturedStdout();

    EXPECT_TRUE(output.find("35.5") != std::string::npos);  // 20.5 + 15.0
}

// Test: Date filtering
TEST_F(ExpenseTrackerTest, FilterByDateRangeValid) {
    std::string today = "2025-04-05";  // Change to current date as needed

    auto results = tracker.filterByDateTime(today, today);
    EXPECT_FALSE(results.empty());
}