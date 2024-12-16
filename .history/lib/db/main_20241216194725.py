import argparse
from lib.cli import create_user, list_users, create_project

# Step 1: Create an argument parser
parser = argparse.ArgumentParser(description="Phase 3 Project CLI")

# Step 2: Add subcommands
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Command: Add User
add_user_parser = subparsers.add_parser("add_user", help="Add a new user")
add_user_parser.add_argument("--name", required=True, help="Name of the user")
add_user_parser.add_argument("--email", required=True, help="Email of the user")

# Command: List Users
subparsers.add_parser("list_users", help="List all users")

# Command: Add Project
add_project_parser = subparsers.add_parser("add_project", help="Add a new project")
add_project_parser.add_argument("--user_id", type=int, required=True, help="ID of the user")
add_project_parser.add_argument("--title", required=True, help="Title of the project")
add_project_parser.add_argument("--description", required=True, help="Description of the project")

# Step 3: Parse the arguments
args = parser.parse_args()

# Step 4: Route to the correct function
if args.command == "add_user":
    create_user(args.name, args.email)
elif args.command == "list_users":
    list_users()
elif args.command == "add_project":
    create_project(args.user_id, args.title, args.description)
else:
    parser.print_help()
