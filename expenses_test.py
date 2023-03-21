import unittest

from expenses import *


class Expenses_Test(unittest.TestCase):

    def setUp(self):
        """The setUp function runs before every test function."""

        # create expenses dictionary and populate with data
        self.expenses = {'food': 5.0, 'coffee': 12.4, 'rent': 825.0, 'clothes': 45.0,
                         'entertainment': 135.62, 'music': 324.0, 'family': 32.45}

    def test_import_expenses(self):
        # import expenses files
        expenses = {}
        import_expenses(expenses, 'expenses.txt')
        import_expenses(expenses, 'expenses_2.txt')

        # test existing total expenses
        self.assertAlmostEqual(45, expenses['clothes'])
        self.assertAlmostEqual(12.40, expenses['coffee'])
        self.assertAlmostEqual(135.62, expenses['entertainment'])

    def test_get_expense(self):
        # test getting expenses based on expense type
        self.assertAlmostEqual(12.40, get_expense(self.expenses, "coffee"))

        # test non-existing expense types
        self.assertEqual(None, get_expense(self.expenses, "phone"))

        # test non-existing expenses type
        self.assertEqual(None, get_expense(self.expenses, "investment"))

        # test existing expenses type
        self.assertAlmostEqual(825.00, get_expense(self.expenses, "rent"))


    def test_add_expense(self):
        # test adding a new expense
        add_expense(self.expenses, "fios", 84.5)
        self.assertAlmostEqual(84.5, self.expenses.get("fios"))

        # test adding expense to  existing expenses
        add_expense(self.expenses,"rent", 50)
        self.assertAlmostEqual(875, self.expenses.get("rent"))

        # test adding a new expense
        add_expense(self.expenses, "phone", 50)
        self.assertAlmostEqual(50, self.expenses.get("phone"))

    def test_deduct_expense(self):
        # test deducting from expense
        deduct_expense(self.expenses, "coffee", .99)
        self.assertAlmostEqual(11.41, self.expenses.get("coffee"))

        # test deducting from expense
        deduct_expense(self.expenses, "entertainment", 100)
        self.assertAlmostEqual(35.62, self.expenses.get("entertainment"))

        # test deducting too much from expense
        with self.assertRaises(RuntimeError):
            deduct_expense(self.expenses, "rent", 830)

        # test deducting from non-existing expense
        deduct_expense(self.expenses, "investment", 50)
        self.assertEqual(None, get_expense(self.expenses, "investment"))

    def test_update_expense(self):
        # test updating an expense
        update_expense(self.expenses, "clothes", 19.99)
        self.assertAlmostEqual(19.99, get_expense(self.expenses, "clothes"))

        # test deducting from non-existing expense
        update_expense(self.expenses, "investment", 50)
        self.assertEqual(None, get_expense(self.expenses, "investment"))

        # test deducting from existing expense
        update_expense(self.expenses, "rent", 200)
        self.assertAlmostEqual(200.00, get_expense(self.expenses, "rent"))

    def test_sort_expenses(self):
        # test sorting expenses by 'expense_type'
        expense_type_sorted_expenses = [('clothes', 45.0),
                                        ('coffee', 12.40),
                                        ('entertainment', 135.62),
                                        ('family', 32.45),
                                        ('food', 5.0),
                                        ('music', 324.0),
                                        ('rent', 825.0)]

        self.assertListEqual(expense_type_sorted_expenses, sort_expenses(self.expenses, "expense_type"))

        # test sorting expenses by 'amount'
        amount_sorted_expenses = [('rent', 825.0),
                                  ('music', 324.0),
                                  ('entertainment', 135.62),
                                  ('clothes', 45.0),
                                  ('family', 32.45),
                                  ('coffee', 12.40),
                                  ('food', 5.0)]

        self.assertListEqual(amount_sorted_expenses, sort_expenses(self.expenses, "amount"))

    def test_export_expenses(self):
        export_expenses(self.expenses, ['coffee', 'clothes'], 'export1.txt')
        export_expenses(self.expenses, ['coffee', 'home'], 'export2.txt')

if __name__ == '__main__':
    unittest.main()
