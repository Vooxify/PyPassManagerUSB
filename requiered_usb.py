# requiered_usb.py
import os
import time
import psutil


def get_usb_drive_info():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("Please insert a USB key for safety ...!\n"
          "USB you insert is used to secure your personal information.\n"
          "Please remove all other USB keys that are plugged into your PC!\n")
    time.sleep(2)

    drives = psutil.disk_partitions()
    for drive in drives:
        if 'removable' in drive.opts or 'cdrom' in drive.opts:
            return {
                'letter': os.path.splitdrive(drive.device)[0],
                'label': drive.mountpoint
            }

def requiered_usb():
    usb_info = get_usb_drive_info()
    while not usb_info:
        print("No USB key detected. Please insert a USB key.")
        usb_info = get_usb_drive_info()

    return usb_info['letter'], usb_info['label']
