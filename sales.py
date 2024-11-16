import random

def daily_sales(available_items, inventory_records, current_day):
    '''
    Updates sales for a given day, generating random sales on non-restocking days.
    
    Parameters:
    available_items (int): T-shirts available from the previous day.
    inventory_records (list): List of inventory records until the previous day.
    current_day (int): Day number to be updated.

    Returns:
    int: Updated number of available items.
    '''
    
    # Basic check for valid input
    if available_items <= 0:
        available_items = 0
        sold_units = 0
        # Record the day with no sales
        inventory_records.append({
            'day': current_day,
            'sold_units': sold_units,
            'restocked_units': 0,
            'available_units': available_items
        })
        return available_items

    # Handle negative days
    if current_day < 0:
        print("Warning: current_day is negative, check input.")
        return available_items

    # Random sales on non-restocking days (not multiples of 7)
    if current_day % 7 != 0:
        sold_units = random.randint(1, min(available_items, 200))  
        available_items -= sold_units  
    else:
        sold_units = 0  # No sales on restocking days

    # Update records with sales data
    inventory_records.append({
        'day': current_day,
        'sold_units': sold_units,
        'restocked_units': 0,
        'available_units': available_items
    })

    return available_items