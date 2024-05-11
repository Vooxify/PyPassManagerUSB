from cryptography.fernet import Fernet
from requiered_usb import get_usb_drive_info

path_to_secure_file = get_usb_drive_info()

path = f"{path_to_secure_file['label']}RESERVED\SECUREFILE"
def generate_key():
    key = Fernet.generate_key()

    with open(f"{path}\encryption.key", "ab") as a:
        a.write(key + b'\n')


    with open(f"{path}\encryption.key", "rb") as file:
        content = file.read()
    file.close()
    a.close()
    return content
