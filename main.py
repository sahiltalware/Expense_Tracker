# expense_tracker.py

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

# To add new expense tracker
    def add_expense(self, date, category, goods_or_service, amount):
        """
        Add a new expense to the tracker.

        Parameters:
        - date (str): Date of the expense.
        - category (str): Category of the expense.
        - Goods_Or_Service(str): type of goods
        - amount (float): Amount of the expense.
        """
        expense = {
            'date': date,
            'category': category,
            'goods_or_service': goods_or_service,
            'amount': amount
        }
        self.expenses.append(expense)
        print("Expense added successfully!")

# To View all expenses in the tracker.
    def view_expenses(self):
        """
        View all expenses in the tracker.
        """
        if not self.expenses:
            print("No expenses to display.")
        else:
            print("Date\t\tCategory\tGoods_or_Service\tAmount")
            print("----------------------------------")
            for expense in self.expenses:
                print(f"{expense['date']}\t{expense['category']}\t\t{expense['goods_or_service']}"                          
                      f"\t\t{expense['amount']}")


# Main Function To Run The Program
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            goods_or_service = input("Enter the type of Goods or service:")
            amount = float(input("Enter amount: "))
            tracker.add_expense(date, category, goods_or_service, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
