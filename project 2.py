expenses = []
total = 0

while True:
    expense = int(input("Enter expense (0 to stop): "))

    if expense == 0:
        break

    expenses.append(expense)
    total += expense

print("\nExpenses:")
for expense in expenses:
    print(expense)

print("\nTotal Expense:", total)