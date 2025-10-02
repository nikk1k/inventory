from collections import Counter

dictionary = {'rope': 1, 'torch': 6, 'gold coins': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coins', 'dagger', 'gold coins', 'gold coins', 'dragon scale']

def display_inventory(inventory):
    print("Inventory")
    total = 0
    for i, j in inventory.items():
        print(f"{j} {i}")
        total += j

    print(f"Total number of items: {total}")

def add_to_inventory(inventory, added_items):
    inventory_counter = Counter(inventory)
    loot_counter = Counter(added_items)
    updated_inventory = inventory_counter + loot_counter
    return dict(updated_inventory)

dictionary = add_to_inventory(dictionary, dragon_loot)
display_inventory(dictionary)

