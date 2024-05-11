import getpass

from cryptography.fernet import Fernet

from Encrypt.NewInfo.GenerateKeys.generate_keys import generate_key
from GenerateTool.generate_tool import generate_password


def password_generator():
    generate_new_password = input("You want to generate one password and use it ? (y/n) ").lower()
    if generate_new_password == "y":
        generated_password = generate_password()
        return generated_password
    elif generate_new_password == "n":
        generated_password = 0
        return generated_password


def z(var):
    f = Fernet(var)
    return f


def dictionnary_file_encryption():
    var = generate_key()
    keys = {}
    temp_var_keys = b""
    for items in var:

        if isinstance(items, int):
            items = bytes([items])

        if items == b"\n":

            if temp_var_keys:
                keys[len(keys) + 1] = temp_var_keys.decode()

            temp_var_keys = b""

        else:
            temp_var_keys += items

    if temp_var_keys:
        keys[len(keys) + 1] = temp_var_keys.decode()

    for key in keys:
        keys[key] = keys[key].replace("\n", "")

    return keys


def encrypt():
    global input_password
    print("ATTENTION ! PLEASE DON'T PRESS CTRL + C OR THE PROGRAM CRASHING !!")
    input_domain = input("For who website you want to register ? : ").encode()
    input_username = input("Username : ").encode()
    is_generated_password = password_generator()
    if is_generated_password == 0:
        input_password = getpass.getpass("Password : ").encode()
    else:
        input_password = is_generated_password.encode()

    dico = dictionnary_file_encryption()
    last_key_dico = str(list(dico.values())[-1])
    f = z(last_key_dico)

    encrypted_domain = f.encrypt(input_domain)
    encrypted_username = f.encrypt(input_username)
    encrypted_password = f.encrypt(input_password)

    return encrypted_username.decode(), encrypted_password.decode(), encrypted_domain.decode()
