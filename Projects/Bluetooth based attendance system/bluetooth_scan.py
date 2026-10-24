# OPTIONAL: real Bluetooth scanning for attendance_system.py
#
# Install once:  pip install bleak
# (If the install fails on your laptop, ignore this file. The attendance
#  system still works in demo mode.)
#
# Before using it:
#   1. Turn Bluetooth ON in Windows.
#   2. Every student turns Bluetooth ON and keeps the phone's Bluetooth name
#      the same as the name saved in students.csv (for example Aarav-Phone).
#
# The lines with async and await are a fixed pattern. Just copy them as they are.

import asyncio
from bleak import BleakScanner


def scan_nearby(seconds=8):
    async def run():
        return await BleakScanner.discover(timeout=seconds)

    devices = asyncio.run(run())

    names = []
    for device in devices:
        if device.name:
            names.append(device.name)
    return names
