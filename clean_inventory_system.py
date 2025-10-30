"""
Inventory Management System

This module provides functions to manage inventory stock data,
including adding, removing, and tracking items.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.

    Args:
        item (str): The name of the item to add
        qty (int): The quantity to add
        logs (list): Optional list to append log messages

    Returns:
        None
    """
    if logs is None:
        logs = []
    if not item or not isinstance(item, str):
        return
    if not isinstance(qty, int) or qty < 0:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove an item from the inventory.

    Args:
        item (str): The name of the item to remove
        qty (int): The quantity to remove

    Returns:
        None
    """
    try:
        if item not in stock_data:
            print(f"Item '{item}' not found in inventory")
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except (KeyError, TypeError) as e:
        print(f"Error removing item: {e}")


def get_qty(item):
    """
    Get the quantity of an item in inventory.

    Args:
        item (str): The name of the item

    Returns:
        int: The quantity of the item, or 0 if not found
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): The path to the JSON file

    Returns:
        None
    """
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): The path to the JSON file

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2)


def print_data():
    """
    Print the current inventory report.

    Returns:
        None
    """
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """
    Check for items with quantity below threshold.

    Args:
        threshold (int): The minimum quantity threshold

    Returns:
        list: List of items below the threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate inventory system usage.

    Returns:
        None
    """
    add_item("apple", 10)
    add_item("banana", 5)
    # Removed invalid type calls
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    # Removed dangerous eval() call


if __name__ == "__main__":
    main()
