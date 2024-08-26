# @codeGeex_disable
import csv
from datetime import datetime
from colorama import Fore, Back, Style, init
import os
import argparse as ap

init(autoreset=True)


class ExpenseTracker:
    def __init__(self, filename='m_expenses.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Index', 'Date', 'Description', 'Amount', "Category"])

    def add_expense(self, description, amount, category):
        expense_length = len(self.load_expenses())
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(
                [expense_length, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), description, amount, category])
        print(f'id-{expense_length}', datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
              f', {description}, {amount}, {category} ', Fore.RED + 'added')

    def modify_expense(self, index, date=None, description=None, amount=None, category=None):
        expenses = (self.load_expenses())
        if 0 < index < len(expenses):
            if date:
                expenses[index][1] = date
            if description:
                expenses[index][2] = description
            if amount:
                expenses[index][3] = amount
            if category:
                expenses[index][4] = category
            # expenses[index] = [index, date, description, amount, category]
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(expenses)
        else:
            print('Invalid index')

    def delete_expense(self, index):
        expenses = self.load_expenses()
        if 0 < index < len(expenses):
            del expenses[index]
            # Reassign indexes to maintain correct order
            for i, expense in enumerate(expenses[1:], start=1):
                expense[0] = i
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(expenses)
            print(Fore.RED + f"Expense at index {index} deleted successfully!")
        else:
            print(f"No expense found at index {index}.")

    def view_expenses(self):
        for expense in self.load_expenses():
            print(
                "#{:<10} {:<20} {:<10} {:<10} {:<10}".
                format(expense[0], expense[1], expense[2], expense[3], expense[4]))

    def summarize_expenses(self):
        expenses = self.load_expenses(header=False)
        total_expenses = sum(float(expense[3]) for expense in expenses)
        print(f"Total expenses: {total_expenses}")

    def load_expenses(self, header=True):
        if header:
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                # next(reader)
                return list(reader)
        else:
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                return list(reader)


def arg_parse():
    parser = ap.ArgumentParser(description='Expense Tracker')

    subparser = parser.add_subparsers(dest='command')
    add_parser = subparser.add_parser('add', help='Add a new expense')
    add_parser.add_argument('description', help='Description of the expense')
    add_parser.add_argument('amount', help='Amount of the expense')
    add_parser.add_argument('category', help='Category of the expense')

    modify_parser = subparser.add_parser('modify', help='Modify an existing expense')
    modify_parser.add_argument('--index',type=int, help='Index of the expense to modify')
    modify_parser.add_argument('--date', help='New date of the expense')
    modify_parser.add_argument('--description', help='New description of the expense')
    modify_parser.add_argument('--amount', help='New amount of the expense')
    modify_parser.add_argument('--category', help='New category of the expense')

    args = parser.parse_args()
    return args


def main():
    args = arg_parse()

    expense_tracker = ExpenseTracker()
    if args.command == 'add':
        expense_tracker.add_expense(args.description, args.amount, args.category)
    if args.command == 'modify':
        expense_tracker.modify_expense(args.index, date=args.date, description=args.description, amount=args.amount,
                                       category=args.category)

    # expense_tracker = ExpenseTracker('demo_expenses.csv')
    # expense_tracker.add_expense('dinner', 100, 'dinner')
    # expense_tracker.add_expense('cigarette', 50, 'cigarette')
    # expense_tracker.add_expense('coffee', 20, 'coffee')
    # expense_tracker.add_expense('groceries', 200, 'groceries')
    # expense_tracker.view_expenses()
    # print()
    expense_tracker.modify_expense(1, amount='150')
    # expense_tracker.view_expenses()
    # print()
    # expense_tracker.delete_expense(2)
    # expense_tracker.view_expenses()
    # expense_tracker.summarize_expenses()

    # parser = ap.ArgumentParser(description='Expense Tracker')
    # parser.add_argument('filename', help='Filename to store expenses')
    # args = parser.parse_args()
    # ExpenseTracker(args.filename)
    # # Add more functionality here
    # # For example, you could add a command to add a new expense
    # # or


if __name__ == '__main__':
    main()
