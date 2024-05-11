import os
import sys

from Decrypt.decrypt_file import run as decrypt_run
from Desing.Loading.loading import Loading
from Encrypt.NewInfo.EncryptedDatas.write_encrypted_datas import add_encrypted_datas
from requiered_usb import requiered_usb

readme_message = ('PLEASE READ THIS DOCUMENT !\n'
                  'The script has created 2 new folders: "RESERVED" and "SAFEFILE"\n'
                  '\n'
                  '\n[----_----_----_----_----_----_----_----_----_----_----_----]\n'
                  '\n'
                  '\n'
                  'IMPORTANT!\n'
                  'If you format your key, you lose your secure file and after,'
                  'you will no longer be able to read your personal infos\n'
                  'This file is very important, SAVE IT!\n'
                  '\n'
                  '\n'
                  'The Creator.,.')

loading_usb_plugged = Loading(type_load=[
    "USB device detected",
    "Analyzing",
    "Reading and modifying"
])

loading_generate_secure_infos = Loading(type_load=[
    "Generating a new key",
    "Adding domain(s)",
    "Adding username(s)",
    "Adding password(s)",
    "Crypting",
    "Finishing"
])


def create_securefile_directory(letter):
    securefile_path = os.path.join(letter, "RESERVED", "SECUREFILE")
    try:
        os.makedirs(securefile_path)
    except FileExistsError:
        pass
    return securefile_path


def see_datas():
    see_datas = input("Do you want to see all data(s)? (y/n): ").lower()
    if see_datas == "y":
        decrypt_run()
    elif see_datas == "n":
        pass



def add_new_data():
    add_new_data = input("Do you want to add data(s)? (y/n): ").lower()
    if add_new_data == "y":
        add_encrypted_datas()

    elif add_new_data != "y":
        sys.exit()



def run():
    see_datas()
    add_new_data()

    while True:
        continue_while = input("You want to add another data ? (y/n) : ").lower()
        if continue_while == "n":
            loading_generate_secure_infos.animate_loading()
            break
        else:
            add_encrypted_datas()


if __name__ == "__main__":
    # Continue checking for USB key until it is inserted
    usb_letter, _ = requiered_usb()
    loading_usb_plugged.animate_loading()

    # Create the securefile directory
    securefile_path = create_securefile_directory(usb_letter)

    # Write the README file
    main_path, readme = usb_letter, os.path.join(usb_letter, "RESERVED", "SECUREFILE", "README.txt")
    # noinspection PyPackageRequirements
    with open(readme, "w") as readme_file:
        readme_file.write(readme_message)

    # Execute the main functionality
    run()
input("PAUSE")