# -*- coding: utf-8 -*-
"""
Console Bot helper.
For add, change, get phone numbers
"""
import re


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts, additional='added'):
    try:
        name, phone = args
        reg_phone = ''.join(re.findall(r'[\+\(]?[1-9]', phone))
        if additional == "updated" and name not in contacts:
            return f"Contact '{name}' is not in contact list"
        if reg_phone:
            contacts[name] = reg_phone
        else:
            return f"Looks like your phone number '{phone}' in incorrect format try one more time"
    except ValueError:
        return "Please add phone in correct format 'NAME PHONE' "
    return f"Contact {additional}."


def get_phone_number(args, contacts):
    try:
        phone = contacts[args]
    except ValueError:
        return f"Phone for {args} not found"
    return f"Phone number for {args} is {phone}"


def get_all(contacts):
    if contacts:
        return '\n'.join([f"{k}: {v}" for k, v in contacts.items()])
    else:
        return "Data is empty, nothing to show"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(add_contact(args, contacts, "updated"))
        elif command == "phone":
            print(get_phone_number(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
