import os


import json
import os

JSON_FILE = "expenses.json"

def create_json_file():
    with open(JSON_FILE, "w") as file:
        json.dump([], file)

def read_json():
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
    print(f"Añadiendo gasto: {description} - Monto: {amount}" + (f" - Categoría: {category}" if category else ""))
    expense_data = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses = read_json()
    expenses.append(expense_data)
    write_json(expenses)