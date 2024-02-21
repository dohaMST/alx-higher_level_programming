#!/usr/bin/python3
"""defining the function"""
import os
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    listAr = []
    for arg in sys.argv[1:]:
        listAr.append(arg)

    f_name = 'add_item.json'

    if not os.path.exists(f_name):
        with open(f_name, 'w') as file:
            file.write("[]")

    existing_data = load_from_json_file(f_name)
    existing_data.extend(listAr)

    save_to_json_file(existing_data, f_name)

    load_from_json_file(f_name)


if __name__ == "__main__":
    main()
