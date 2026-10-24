# business_name_generator.py
import random

prefixes = ["Nova", "Blue", "Swift", "Prime", "Urban", "Bright"]
suffixes = ["Hub", "Labs", "Works", "Studio", "Nest", "Tech"]

print("Business Name Generator")
industry = input("Enter your industry (example: food, tech): ")

for i in range(5):
    name = random.choice(prefixes) + industry.capitalize() + random.choice(suffixes)
    print(name)