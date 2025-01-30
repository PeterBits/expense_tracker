import os


import json
import os

JSON_FILE = "expenses.json"

def create_json_file():
    with open(JSON_FILE, "w") as file:
        json.dump([], file)

def print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))

def get_expense_list():
    try:
        list_dir = os.listdir('.')
        list_dir = [file for file in list_dir if file.endswith('.json')]
        if JSON_FILE not in list_dir:
            create_json_file()
            return []
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{JSON_FILE}' is not a valid JSON.")
        return []

def write_json(data):
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error writing to '{JSON_FILE}': {e}")

def add_new_expense(description, amount, category):
    expenses = get_expense_list()
    expense_data = {
        "description": description,
        "amount": amount,
        "category": category,
        "id": len(expenses) + 1
    }
    expenses.append(expense_data)
    write_json(expenses)
    print(f"Gasto añadido: {description} - Monto: {amount}" + (f" - Categoría: {category}" if category else ""))

def update_expense(id, description, amount, category):
    expenses = get_expense_list()
    for expense in expenses:
        if expense["id"] == id:
            expense["description"] = description
            expense["amount"] = amount
            expense["category"] = category
            break
    write_json(expenses)
    print(f"Gasto actualizado: {description} - Monto: {amount}" + (f" - Categoría: {category}" if category else ""))
    
def delete_expense(expense_id):
    expenses = get_expense_list()
    expenses_updated = list(filter( lambda x : x["id"] != expense_id, expenses ))
    write_json(expenses_updated)
    print(f"Gasto {expense_id} eliminado")
    
def show_expense_list():
    expenses = get_expense_list()
    print_json(expenses)
    
def show_summary():
    expenses = get_expense_list()
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total gastado: {total}")