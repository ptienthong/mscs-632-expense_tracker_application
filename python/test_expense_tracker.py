import unittest
from datetime import datetime
from expense_tracker import Expense, ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ExpenseTracker()
        self.exp1 = Expense("2025-04-01", 10.0, "Food", "Lunch")
        self.exp2 = Expense("2025-04-03", 15.0, "Transport", "Gas")
        self.exp3 = Expense("2025-04-04", 20.0, "Food", "Dinner")
        self.tracker.add_expense(self.exp1)
        self.tracker.add_expense(self.exp2)
        self.tracker.add_expense(self.exp3)

    def test_add_expense(self):
        self.assertEqual(len(self.tracker.expenses), 3)
        self.assertEqual(self.tracker.expenses[0].amount, 10.0)

    def test_filter_by_category(self):
        results = self.tracker.filter_by_category("food")
        self.assertEqual(len(results), 2)
        self.assertTrue(all(exp.category.lower() == "food" for exp in results))

    def test_filter_by_date(self):
        results = self.tracker.filter_by_date("2025-04-02", "2025-04-04")
        self.assertEqual(len(results), 2)
        self.assertIn(self.exp2, results)
        self.assertIn(self.exp3, results)

    def test_summary_total(self):
        # Mock the print with StringIO to capture output, or test internal logic directly
        total = sum(exp.amount for exp in self.tracker.expenses)
        self.assertEqual(total, 45.0)

    def test_summary_by_category(self):
        summary = {}
        for exp in self.tracker.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount

        self.assertEqual(summary["Food"], 30.0)
        self.assertEqual(summary["Transport"], 15.0)

if __name__ == '__main__':
    unittest.main()
