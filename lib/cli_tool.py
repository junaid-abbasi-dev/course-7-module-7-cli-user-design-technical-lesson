# NOTE: This starter code is intentionally incomplete so all tests fail.
# Students will need to define the parser, subcommands, and handlers.

import argparse

def add_task(args):
    print(f"✅ Task added: {args.description}")


def list_tasks(args):
    print("📋 Listing tasks...")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task")
    add_parser.set_defaults(func=add_task)

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=list_tasks)

    args = parser.parse_args()

    # Handle missing command
    if hasattr(args, "func"):
       args.func(args)
    else:
       parser.print_help()