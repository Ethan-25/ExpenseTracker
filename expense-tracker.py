# @codeGeex_disable
import csv
from datetime import datetime
import os
import argparse as ap


class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Index', 'Date', 'Description', 'Amount', "Category"])

    def add_expense(self, description, amount, category):
        expense_length = len(self.load_expenses())
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(
                [expense_length, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), description, amount, category])
        print(f'id-{expense_length }', datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
              f', {description}, {amount}, {category} added')

    def modify_expense(self, index, date, description, amount, category):
        data = (self.load_expenses())
        if 0 < index < len(data):
            data[index] = [index, date, description, amount, category]
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        else:
            print('Invalid index')

    # def delete_expense(self, date, description):

    def view_expenses(self):
        for expense in self.load_expenses():
            print(
                "#{:<10} {:<20} {:<10} {:<10} {:<10}".
                format(expense[0], expense[1], expense[2], expense[3], expense[4]))

            # def summarize_expenses(self):

    def load_expenses(self):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f)
            # next(reader)
            return list(reader)


def main():
    expense_tracker = ExpenseTracker('demo_expenses.csv')
    expense_tracker.add_expense('dinner', 100, 'dinner')
    expense_tracker.add_expense('lunch', 50, 'lunch')
    expense_tracker.add_expense('coffee', 20, 'coffee')
    expense_tracker.add_expense('groceries', 200, 'groceries')
    expense_tracker.view_expenses()
    print()
    expense_tracker.modify_expense(1, '2022-01-01 12:00:00', 'lunch', 60, 'lunch')
    expense_tracker.view_expenses()


# parser = ap.ArgumentParser(description='Expense Tracker')
# parser.add_argument('filename', help='Filename to store expenses')
# args = parser.parse_args()
# ExpenseTracker(args.filename)
# # Add more functionality here
# # For example, you could add a command to add a new expense
# # or


if __name__ == '__main__':
    main()
