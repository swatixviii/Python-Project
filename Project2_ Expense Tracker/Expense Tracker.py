import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Initialize an empty DataFrame to store expense data
        self.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])
        
    def add_expense(self, amount: float, category: str, description: str):
        """Add an expense entry."""
        date = datetime.now().strftime('%Y-%m-%d')  # Record today's date
        new_expense = pd.DataFrame([[date, category, amount, description]], columns=self.expenses.columns)
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)

    def generate_report(self):
        """Generate a report of total expenses and breakdown by category and month."""
        # Total spending
        total_spending = self.expenses['Amount'].sum()
        
        # Spending by category
        spending_by_category = self.expenses.groupby('Category')['Amount'].sum().reset_index()
        
        # Spending by month
        self.expenses['Month'] = pd.to_datetime(self.expenses['Date']).dt.to_period('M')
        spending_by_month = self.expenses.groupby('Month')['Amount'].sum().reset_index()
        
        # Displaying the reports
        print(f"Total Spending: ${total_spending:.2f}\n")
        print("Spending by Category:")
        print(spending_by_category)
        print("\nSpending by Month:")
        print(spending_by_month)

    def save_data(self, file_name: str):
        """Save the expense data to a CSV file."""
        self.expenses.to_csv(file_name, index=False)
        print(f"Data saved to {file_name}")

    def load_data(self, file_name: str):
        """Load expense data from a CSV file."""
        self.expenses = pd.read_csv(file_name)
        print(f"Data loaded from {file_name}")

# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()

    # Add some expenses
    tracker.add_expense(50.75, 'Food', 'Lunch at cafe')
    tracker.add_expense(100.50, 'Entertainment', 'Movie tickets')
    tracker.add_expense(20.00, 'Food', 'Groceries')

    # Generate and print the report
    tracker.generate_report()

    # Save the data to a CSV file
    tracker.save_data('expenses.csv')

    # Load the data back
    tracker.load_data('expenses.csv')
