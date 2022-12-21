with open("day-1-input", "r") as my_input:
    # Init empty list to store elf inventories
    elf_inventories = []
    # Init empty list to store current block of input
    current_inventory = []

    # Iterate over file lines
    for line in my_input:
        # Remove leading and trailing white spaces
        line = line.strip()
        # Check if line is empty
        if len(line) == 0:
            # If line is empty, inventory ends
            # Initialize variable to store sum of calories
            inventory_calories = 0
            # Iterate over lines in current inventory
            for line in current_inventory:
                # Convert input from line to integer and add
                inventory_calories += int(line)
            # Append sum to list of elf inventories
            elf_inventories.append(inventory_calories)
            # Reset inventory
            current_inventory = []
        else:
            # If the line is not empty, add to current inventory
            current_inventory.append(line)
    # Add last inventory
    inventory_calories = 0
    for line in current_inventory:
        inventory_calories += int(line)
    elf_inventories.append(inventory_calories)

#highest_calories = max(elf_inventories)
#print(elf_inventories)
# print(highest_calories)

highest_value = -1
highest_value_index = -1
for i, value in enumerate(elf_inventories):
    if value > highest_value:
        highest_value = value
        highest_value_index = i

print("The highest calorie count is", highest_value, "carried by Elf #", highest_value_index+1)
