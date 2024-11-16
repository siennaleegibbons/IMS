def restock_inventory(available_items, inventory_records, current_day):
    """
    Updates stock for the current day based on restocking schedule.
    
    Parameters:
    available_items (int): Items available from the previous day.
    inventory_records (list): List of records up to the previous day.
    current_day (int): Day number to update.

    Returns:
    int: Updated available items.
    """
    
    # Check if today is a restocking day
    if current_day == 0 or current_day % 7 == 0:
        restocked_units = 2000 - available_items  # Calculate restocked units
        available_items = 2000  # Set stock to max
        
        # Record restocking
        inventory_records.append({
            'day': current_day,
            'sold_units': 0,
            'restocked_units': restocked_units,
            'available_units': available_items
        })
    else:
        # Not a restocking day
        inventory_records.append({
            'day': current_day,
            'sold_units': 0,
            'restocked_units': 0,
            'available_units': available_items
        })

    return available_items