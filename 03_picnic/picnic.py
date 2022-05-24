#!/usr/bin/env python3
"""
Author : haoruic <haorui1997@gmail.com>
Date   : 2022-05-23
Purpose: Chapter 03: Working with lists
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("item", metavar="str", help="Item(s) to bring", nargs="+")

    parser.add_argument(
        "-s", "--sorted", help="Sort the items", default=False, action="store_true"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    item_list = args.item
    sorted_arg = args.sorted

    # Sort items if sorted argument specified
    if sorted_arg:
        item_list.sort()
    else:
        pass

    # Convert items from list to sentence
    if len(item_list) == 1:
        items = item_list[0]
    elif len(item_list) == 2:
        items = f"{item_list[0]} and {item_list[1]}"
    else:
        last_item = item_list[-1]
        item_list[-1] = f"and {last_item}"
        items = ", ".join(item_list)

    print(f"You are bringing {items}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
