#!/usr/bin/env python3
"""
Author : haoruic <haorui1997@gmail.com>
Date   : 2022-06-08
Purpose: Chapter 4 - Jump The Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    
    jump_dict = {'1':'9',
                '2':'8',
                '3':'7',
                '4':'6',
                '5':'0',
                '6':'4',
                '7':'3',
                '8':'2',
                '9':'1',
                '0':'5'}

    jumped_list = [jump_dict.get(ch, ch) for ch in text_arg]
    jumped_str = "".join(jumped_list)

    print(f'{jumped_str}')
    return jumped_str

# --------------------------------------------------
if __name__ == '__main__':
    main()
