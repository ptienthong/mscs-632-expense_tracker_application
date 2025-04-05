import unittest
from datetime import datetime
from expense_tracker import Expense, ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    """
    Unit tests for the ExpenseTracker class and its associated Expense objects.
    """
    def setUp(self):
        """
        Set up a new ExpenseTracker instance and add sample expenses before each test.
        This ensures that all test cases operate on a known, consistent dataset.
        """
        self.tracker = ExpenseTracker()
        self.exp1 = Expense("2025-04-01", 10.0, "A", "Lunch")
        self.exp2 = Expense("2025-04-03", 15.0, "B", "Gas")
        self.exp3 = Expense("2025-04-04", 20.0, "A", "Dinner")
        self.tracker.add_expense(self.exp1)
        self.tracker.add_expense(self.exp2)
        self.tracker.add_expense(self.exp3)

    def test_add_expense(self):
        """
        Test whether expenses are added correctly to the tracker.
        Checks that the total count is correct and the first entry matches expected data.
        """
        self.assertEqual(len(self.tracker.expenses), 3)
        self.assertEqual(self.tracker.expenses[0].amount, 10.0)

    def test_filter_by_category(self):
        """
        Test filtering by category.
        Should return two expenses with category 'A' (case-insensitive).
        """
        results = self.tracker.filter_by_category("a")
        self.assertEqual(len(results), 2)
        self.assertTrue(all(exp.category.lower() == "a" for exp in results))

    def test_filter_by_date(self):
        """
        Test filtering expenses between two dates (inclusive).
        Should return expenses from April 3 and April 4.
        """
        results = self.tracker.filter_by_date("2025-04-02", "2025-04-04")
        self.assertEqual(len(results), 2)
        self.assertIn(self.exp2, results)
        self.assertIn(self.exp3, results)

    def test_summary_total(self):
        """
        Test that the total of all expenses is calculated correctly.
        10 + 15 + 20 = 45.0
        """
        total = sum(exp.amount for exp in self.tracker.expenses)
        self.assertEqual(total, 45.0)

    def test_summary_by_category(self):
        """
        Test that the total expenses are correctly aggregated by category.
        Category 'A' should total 30.0, 'B' should total 15.0.
        """
        summary = {}
        for exp in self.tracker.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount

        self.assertEqual(summary["A"], 30.0)
        self.assertEqual(summary["B"], 15.0)

# Run all test cases when this file is executed directly
if __name__ == '__main__':
    unittest.main()
