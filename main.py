import argparse
from methods import (
    add_new_expense,
    update_expense,
    delete_expense,
    show_expense_list
    )

# Configurar argparse
parser = argparse.ArgumentParser(description="Expense Tracker - Añade y gestiona tus gastos.")
subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

# add command
add_parser = subparsers.add_parser("add", help="Añadir un nuevo gasto")
add_parser.add_argument("--description", type=str, required=True, help="Descripción del gasto")
add_parser.add_argument("--amount", type=float, required=True, help="Monto del gasto")
add_parser.add_argument("--category", type=str, required=False, help="Categoría del gasto")
    
    
    
# update command
update_parser = subparsers.add_parser("update", help="Actualizar un gasto")
update_parser.add_argument("--id", type=int, required=True, help="ID del gasto a actualizar")
update_parser.add_argument("--description", type=str, required=True, help="Descripción del gasto")
update_parser.add_argument("--amount", type=float, required=True, help="Monto del gasto")
update_parser.add_argument("--category", type=str, required=False, help="Categoría del gasto")

# delete expense
delete_parser = subparsers.add_parser("delete", help="Eliminar un gasto")
delete_parser.add_argument("--id", type=int, required=True, help="ID del gasto a eliminar")

show_expenses = subparsers.add_parser("list", help="Mostrar todos los gastos")


# Parsear los argumentos
args = parser.parse_args()


# Ejecutar la acción correspondiente
if args.command == "add":
    add_new_expense(args.description, args.amount, args.category)
elif args.command == "update":
    update_expense(args.id, args.description, args.amount, args.category)
elif args.command == "delete":
    delete_expense(args.id)
elif args.command == "list":
    show_expense_list()
else:
    parser.print_help()

