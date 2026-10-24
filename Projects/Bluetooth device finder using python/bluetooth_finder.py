# bluetooth_finder.py
devices = ["Redmi Buds", "boAt Rockerz", "Samsung Watch", "JBL Speaker", "My Phone"]

print("Bluetooth Device Finder")
name = input("Enter device name to find: ")

found = False
for d in devices:
    if name.lower() in d.lower():
        print("Device found:", d)
        found = True

if found == False:
    print("Device not found")