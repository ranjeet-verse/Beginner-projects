"""
Personal Expense Tracker
A beginner-friendly Python project to track daily expenses
"""

# Store expenses in a list
expenses = []

def show_menu():
    """Display the main menu options"""
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Expenses by Category")
    print("5. Exit")
    print("=" * 32)

def add_expense():
    """Add a new expense to the tracker"""
    print("\n--- Add New Expense ---")
    
    # Get expense details from user
    item = input("Item name: ")
    
    # Keep asking until we get a valid number
    while True:
        try:
            amount = float(input("Amount ($): "))
            if amount <= 0:
                print("Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    category = input("Category (food/transport/entertainment/other): ").lower()
    
    # Store the expense as a dictionary
    expense = {
        "item": item,
        "amount": amount,
        "category": category
    }
    
    expenses.append(expense)
    print(f"✓ Added: {item} - ${amount:.2f}")

def view_expenses():
    """Display all expenses"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['item']:20s} ${expense['amount']:8.2f} ({expense['category']})")

def view_total():
    """Calculate and display total spending"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    total = sum(expense['amount'] for expense in expenses)
    print(f"\n--- Total Spending ---")
    print(f"Total: ${total:.2f}")
    print(f"Number of expenses: {len(expenses)}")

def view_by_category():
    """Show expenses grouped by category"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return
    
    # Create a dictionary to store totals by category
    category_totals = {}
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    print("\n--- Expenses by Category ---")
    for category, total in category_totals.items():
        print(f"{category.capitalize():15s}: ${total:.2f}")

def main():
    """Main program loop"""
    print("Welcome to your Personal Expense Tracker!")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            print("\nThank you for using Expense Tracker! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()