from expense import Expenses
import calendar
import datetime

def main():
    print("Start...")
    expense_file_path = "expenses.csv"
    budget = 100000

    expense = total_expense()
    file_save(expense,expense_file_path)
    summarize_expense(expense_file_path,budget)

def total_expense():
    print("Total Expense...")
    expense_name = input("Expense name: ")
    expense_amount = float(input("Enter amount: "))
    print(f"Expense name is {expense_name} , {expense_amount}")

    expense_category = ["Food","Home","Work","Fun","Transport"]
    
    while True:
        print("Kes Category ma Kharcha kar rahay hu batayo...")
        for i,category_name in enumerate(expense_category):
            print(f"{i+1}.{category_name}")
        value_range = f"[1-{len(expense_category)}]"
        selected_index = int(input(f"Category batayo::{value_range}: "))-1
        
        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            print(selected_category)

            new_expense = Expenses(name = expense_name , category = selected_category , amount = expense_amount)
            return new_expense
        else:
            print("Invalid Category") 

def file_save(expense:Expenses,expense_file_path):
    print(f"Expense save in file : {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path,budget):
    print("Summary of user Expenses")
    expenses = []
    with open(expense_file_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            expense_name,expense_amount,expense_category = line.strip().split(",")
            print(f"{expense_name} {expense_category} {expense_amount}")
            line_expense = Expenses(name=expense_name,amount=float(expense_amount),category=expense_category)
            # print(line_expense)
            expenses.append(line_expense)
            print(expenses)

    amount_by_category = {}
    for expense in expenses: 
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount    
    print("Category wise Expense")
    for key,amount in amount_by_category.items():
        print(f"{key} : {amount}") 

    total_spent = sum([x.amount for x in expenses])  
    print(f"Total Kharcha: {total_spent:.2f}")  

    remaining_budget = budget - (total_spent)
    print(f"Remainig Budget : {remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaning_days = days_in_month - now.day
    print(f"Remaining Days : {remaning_days}")

    daily_budget = remaining_budget/remaning_days
    print(f"Daily Budget : {daily_budget}")
    
if __name__ == "__main__":
   main()