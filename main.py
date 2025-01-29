import argparse
from methods import add_new_expense

# Configurar argparse
parser = argparse.ArgumentParser(description="Expense Tracker - Añade y gestiona tus gastos.")
subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

# add command
add_parser = subparsers.add_parser("add", help="Añadir un nuevo gasto")
add_parser.add_argument("--description", type=str, required=True, help="Descripción del gasto")
add_parser.add_argument("--amount", type=float, required=True, help="Monto del gasto")
add_parser.add_argument("--category", type=str, required=False, help="Monto del gasto")
    
# Parsear los argumentos
args = parser.parse_args()


# Ejecutar la acción correspondiente
if args.command == "add":
    add_new_expense(args.description, args.amount, args.category)
else:
    parser.print_help()

