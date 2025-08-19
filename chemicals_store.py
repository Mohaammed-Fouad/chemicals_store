import csv
import os

# Dictionary to store chemical data
Chemicals = {}

# CSV file name
file_name = "Chemical_data.csv"
fieldnames = ["Compound Name", "Compound Amount", "Compound Location"]

# Welcome message
print("Welcome to the Chemical Inventory System!")

# Function to load existing data from CSV
def load_existing_data():
    existing_compounds = {}
    if os.path.exists(file_name):
        with open(file_name, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_compounds[row["Compound Name"]] = {
                    "compound amount": int(row["Compound Amount"]),
                    "compound location": row["Compound Location"]
                }
    return existing_compounds

# Function to save data to CSV
def save_to_csv(compound, amount, location):
    file_exists = os.path.exists(file_name)
    with open(file_name, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "Compound Name": compound,
            "Compound Amount": amount,
            "Compound Location": location
        })

# Load existing data into Chemicals dictionary
Chemicals = load_existing_data()

# Infinite loop for running the program
usage_count = 0

while True:
    action = input("\nWrite an action: Add, Update, View, Exit ").lower()
    usage_count += 1
    
    # Adding a new compound
    if action == "add":
        cpd_name = input("What's the name of the compound? ").strip().capitalize()
        cpd_amount = int(input("Write the amount in grams: "))
        cpd_location = input("Where should I store it? ").strip().capitalize()
        
        if cpd_name in Chemicals:
            print(f"{cpd_name} already exists in the inventory. Use 'Update' to add more.")
        else:
            Chemicals[cpd_name] = {"compound amount": cpd_amount, "compound location": cpd_location}
            save_to_csv(cpd_name, cpd_amount, cpd_location)
            print(f"{cpd_name} added successfully!")

    # Updating the amount
    elif action == "update":
        cpd_name = input("What's the name of the compound? ").strip().capitalize()
        if cpd_name in Chemicals:
            added_amount = int(input("Write the added amount in grams: "))
            Chemicals[cpd_name]["compound amount"] += added_amount
            Chemicals[cpd_name]["compound location"] = Chemicals[cpd_name]["compound location"]
            
            # Update CSV
            save_to_csv(cpd_name, Chemicals[cpd_name]["compound amount"], Chemicals[cpd_name]["compound location"])
            print(f"The new amount of {cpd_name} is {Chemicals[cpd_name]['compound amount']} grams.")
        else:
            print(f"{cpd_name} is not found in the inventory. Use 'Add' to insert it first.")

    # Viewing the chemicals
    elif action == "view":
        if Chemicals:
            print("\nCurrent Inventory:")
            for name, details in Chemicals.items():
                print(f"{name}: {details['compound amount']} grams, stored at {details['compound location']}")
        else:
            print("The inventory is currently empty.")

    # Exiting the program
    elif action == "exit":
        print("Thanks for visiting our store!")
        break

    # Invalid action
    else:
        print("Invalid action, please try again.")

# Display usage count
print(f"\nYou have used the system {usage_count - 1} times. Goodbye!")
