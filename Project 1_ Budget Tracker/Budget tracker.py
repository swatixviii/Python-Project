import pandas as pd

# Initialize a DataFrame to store income and expenses
data = pd.DataFrame(columns=['Type', 'Amount', 'Description'])

# Function to add an entry (income or expense)
def add_entry(entry_type, amount, description):
    global data
    new_entry = pd.DataFrame({'Type': [entry_type], 'Amount': [amount], 'Description': [description]})
    data = pd.concat([data, new_entry], ignore_index=True)

# Function to display the current budget summary
def show_summary():
    if data.empty:
        print("No entries yet.")
        return

    total_income = data[data['Type'] == 'Income']['Amount'].sum()
    total_expenses = data[data['Type'] == 'Expense']['Amount'].sum()
    balance = total_income - total_expenses

    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

# Function to display all entries
def show_entries():
    if data.empty:
        print("No entries yet.")
    else:
        print("\n--- All Entries ---")
        print(data)

# Main menu loop
def main_menu():
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Show All Entries")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            add_entry('Income', amount, description)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            add_entry('Expense', amount, description)
        elif choice == '3':
            show_summary()
        elif choice == '4':
            show_entries()
        elif choice == '5':
            print("Exiting the budget tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the budget tracker main menu
if __name__ == "__main__":
    main_menu()
