import os
from Decrypt.ReadLines.read_lines import read_lines
from requiered_usb import requiered_usb

usb_letter, usb_label = requiered_usb()


def datas_extraction():
    values_and_keys = {}

    # Specify the directory to store encrypted_datas.key
    pass_directory = "C:\\Pass"

    # Create the directory if it doesn't exist
    if not os.path.exists(pass_directory):
        os.makedirs(pass_directory)

    # Construct file paths
    encrypted_datas_path = os.path.join(pass_directory, "encrypted_datas.key")
    encryption_key_path = os.path.join(f"{usb_letter}\\RESERVED\\SECUREFILE\\encryption.key")

    # Check if the files exist before attempting to read them
    if not os.path.exists(encrypted_datas_path):
        print(f"File not found: {encrypted_datas_path}")
        return values_and_keys

    if not os.path.exists(encryption_key_path):
        print(f"File not found: {encryption_key_path}")
        return values_and_keys

    lines_values = read_lines(encrypted_datas_path)
    lines_keys = read_lines(encryption_key_path)

    while len(lines_values) >= 3 and lines_keys:
        cle = lines_keys.pop(0)
        values = lines_values[:3]
        values_and_keys[cle] = values
        lines_values = lines_values[3:]
    print(values_and_keys)
    return values_and_keys


