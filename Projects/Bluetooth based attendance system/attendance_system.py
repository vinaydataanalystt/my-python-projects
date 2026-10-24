# Bluetooth Based Attendance System (Python Automation project)
# Run:  python attendance_system.py
#
# No install needed for the main program.
# (Real Bluetooth scanning needs one extra library. It is optional. See bluetooth_scan.py)
#
# Idea: every student registers the Bluetooth name of their phone.
# When the program scans and finds that name nearby, the student is marked PRESENT.

import csv
import os
import random
from datetime import datetime

STUDENTS_FILE = "students.csv"
ATTENDANCE_FILE = "attendance.csv"

# Try to load the real Bluetooth scanner. If it is not available, we use demo mode.
try:
    from bluetooth_scan import scan_nearby
    bluetooth_ready = True
except ImportError:
    bluetooth_ready = False


# ---------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------

def create_sample_students():
    # Make the student list the first time the program runs
    students = [
        ["101", "Aarav Mehta", "Aarav-Phone"],
        ["102", "Priya Nair", "Priya-Phone"],
        ["103", "Rohan Das", "Rohan-Phone"],
        ["104", "Sneha Iyer", "Sneha-Phone"],
        ["105", "Karthik Rao", "Karthik-Phone"],
        ["106", "Divya Menon", "Divya-Phone"],
        ["107", "Arjun Patel", "Arjun-Phone"],
        ["108", "Meera Singh", "Meera-Phone"],
        ["109", "Vikram Joshi", "Vikram-Phone"],
        ["110", "Ananya Rao", "Ananya-Phone"],
    ]
    file = open(STUDENTS_FILE, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["roll_no", "name", "device_name"])
    writer.writerows(students)
    file.close()


def load_students():
    file = open(STUDENTS_FILE, newline="")
    students = list(csv.DictReader(file))
    file.close()
    return students


def load_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        return []
    file = open(ATTENDANCE_FILE, newline="")
    records = list(csv.DictReader(file))
    file.close()
    return records


def ask_date():
    # Ask for a date. Enter = today.
    text = input("Date (YYYY-MM-DD, press Enter for today): ")
    if text == "":
        return datetime.now().strftime("%Y-%m-%d")
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return text
    except ValueError:
        print("That is not a valid date. Example: 2026-10-20")
        return ""


def show_table(rows):
    print("\nRoll No | Name            | Status  | Time")
    print("-" * 46)
    for row in rows:
        print(row["roll_no"].ljust(7), "|", row["name"].ljust(15), "|", row["status"].ljust(7), "|", row["time"])


def take_attendance(found_devices):
    # Compare the devices found with the registered devices of the students
    date = ask_date()
    if date == "":
        return

    old_records = load_attendance()
    for record in old_records:
        if record["date"] == date:
            print("Attendance for", date, "is already taken. Choose option 3 to see it.")
            return

    students = load_students()
    found_lower = []
    for device in found_devices:
        found_lower.append(device.strip().lower())

    now = datetime.now().strftime("%H:%M:%S")
    new_rows = []
    for student in students:
        if student["device_name"].strip().lower() in found_lower:
            status = "Present"
        else:
            status = "Absent"
        new_rows.append({"date": date, "roll_no": student["roll_no"], "name": student["name"], "status": status, "time": now})

    # Save to the attendance file
    new_file = not os.path.exists(ATTENDANCE_FILE)
    file = open(ATTENDANCE_FILE, "a", newline="")
    writer = csv.DictWriter(file, fieldnames=["date", "roll_no", "name", "status", "time"])
    if new_file:
        writer.writeheader()
    writer.writerows(new_rows)
    file.close()

    present = 0
    for row in new_rows:
        if row["status"] == "Present":
            present = present + 1

    print("\nAttendance for", date)
    show_table(new_rows)
    print("\nPresent:", present, "| Absent:", len(new_rows) - present, "| Saved in", ATTENDANCE_FILE)


def real_scan():
    # Scan for real Bluetooth devices (needs bluetooth_scan.py and the bleak library)
    if not bluetooth_ready:
        print("The Bluetooth library is not installed on this computer.")
        print("Use option 2 (demo mode) instead, or see the notes in bluetooth_scan.py.")
        return
    print("Scanning for Bluetooth devices... please wait 8 seconds.")
    try:
        devices = scan_nearby(8)
    except Exception as error:
        print("Bluetooth scan failed:", error)
        print("Check that Bluetooth is ON, or use option 2 (demo mode).")
        return
    print("Devices found:", len(devices))
    for device in devices:
        print(" -", device)
    take_attendance(devices)


def demo_scan():
    # Pretend to scan: about 80 percent of the students are "nearby"
    students = load_students()
    found = []
    for student in students:
        if random.random() < 0.8:
            found.append(student["device_name"])
    found.append("JBL-Speaker")        # some other devices that are not students
    found.append("Unknown-Watch")
    print("DEMO MODE: pretending to scan Bluetooth...")
    print("Devices found:", ", ".join(found))
    take_attendance(found)


def show_one_day():
    date = ask_date()
    if date == "":
        return
    rows = []
    for record in load_attendance():
        if record["date"] == date:
            rows.append(record)
    if len(rows) == 0:
        print("No attendance saved for", date)
    else:
        print("\nAttendance for", date)
        show_table(rows)


def percentage_report():
    records = load_attendance()
    if len(records) == 0:
        print("No attendance saved yet. Take attendance first.")
        return

    dates = []
    for record in records:
        if record["date"] not in dates:
            dates.append(record["date"])

    print("\nATTENDANCE REPORT (" + str(len(dates)) + " days)")
    print("Roll No | Name            | Present | Percentage | Remark")
    print("-" * 62)
    for student in load_students():
        present = 0
        for record in records:
            if record["roll_no"] == student["roll_no"] and record["status"] == "Present":
                present = present + 1
        percent = round(present / len(dates) * 100)
        if percent < 75:
            remark = "LOW (below 75%)"
        else:
            remark = "OK"
        print(student["roll_no"].ljust(7), "|", student["name"].ljust(15), "|", str(present).ljust(7), "|", (str(percent) + "%").ljust(10), "|", remark)


def add_student():
    roll = input("Roll number: ").strip()
    for student in load_students():
        if student["roll_no"] == roll:
            print("This roll number already exists.")
            return
    name = input("Student name: ").strip()
    device = input("Bluetooth device name of the student's phone: ").strip()
    if roll == "" or name == "" or device == "":
        print("Nothing was saved. Please fill all three.")
        return
    file = open(STUDENTS_FILE, "a", newline="")
    csv.writer(file).writerow([roll, name, device])
    file.close()
    print("Student added:", name)


# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------

if not os.path.exists(STUDENTS_FILE):
    create_sample_students()
    print("Sample student list created:", STUDENTS_FILE)

print("=== BLUETOOTH ATTENDANCE SYSTEM ===")
if bluetooth_ready:
    print("Bluetooth scanner: ready")
else:
    print("Bluetooth scanner: not installed (demo mode is available)")

while True:
    print("\n1. Take attendance with Bluetooth scan")
    print("2. Take attendance in demo mode (no Bluetooth needed)")
    print("3. Show attendance for a date")
    print("4. Attendance percentage report")
    print("5. Add a new student")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        real_scan()
    elif choice == "2":
        demo_scan()
    elif choice == "3":
        show_one_day()
    elif choice == "4":
        percentage_report()
    elif choice == "5":
        add_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Please enter a number from 1 to 6.")
