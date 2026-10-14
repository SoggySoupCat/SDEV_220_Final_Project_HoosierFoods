# Author: Drew Shields  
# Role: Project Manager 
# Project: Hoosier Hills Food Bank Inventory Management  

# Data Structures
# Dictionary to look up inventory items by their ID
inventory = {} 

# Lists to track overall transaction and donation histories
transaction_history = []
donor_history = []


# Core Classes
class Item:
    """Manages item details, quantities, and expiration dates."""
    def __init__(self, item_id, name, quantity, category, exp_date):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.category = category
        self.exp_date = exp_date

    def update_quantity(self, amount):
        """Adds or subtracts from the current quantity."""
        self.quantity += amount

    def __str__(self):
        return f"{self.item_id}: {self.name} ({self.category}) - Qty: {self.quantity}, Exp: {self.exp_date}"


class Donor:
    """Manages donor contact details and donation histories."""
    def __init__(self, donor_id, name, contact_info):
        self.donor_id = donor_id
        self.name = name
        self.contact_info = contact_info
        self.donations = [] # Tracks specific items donated by this donor

    def add_donation(self, item_id, quantity, date):
        """Logs a donation made by this donor."""
        donation_record = {"item_id": item_id, "quantity": quantity, "date": date}
        self.donations.append(donation_record)

    def __str__(self):
        return f"Donor {self.donor_id}: {self.name} - {self.contact_info}"


class Transaction:
    """Handles incoming donations and outgoing distributions."""
    def __init__(self, transaction_id, trans_type, item_id, quantity, date, partner_or_donor_id):
        self.transaction_id = transaction_id
        self.trans_type = trans_type # e.g., 'Incoming' or 'Outgoing'
        self.item_id = item_id
        self.quantity = quantity
        self.date = date
        self.partner_or_donor_id = partner_or_donor_id # Who gave it or who received it

    def log_transaction(self):
        """Appends this transaction to the global history list."""
        transaction_history.append(self)

    def __str__(self):
        return f"[{self.date}] {self.trans_type}: {self.quantity}x of Item {self.item_id} (Entity ID: {self.partner_or_donor_id})"


# Example Usage (For Testing)
if __name__ == "__main__":
    # Create a new item and add it to the inventory dictionary
    new_item = Item("ITM001", "Canned Beans", 50, "Canned Goods", "2027-12-31")
    inventory[new_item.item_id] = new_item
    
    # Create a donor
    new_donor = Donor("DNR100", "Local Grocery", "contact@localgrocery.com")
    donor_history.append(new_donor)
    
    # Log an incoming transaction
    new_trans = Transaction("TRX001", "Incoming", "ITM001", 50, "2026-10-14", "DNR100")
    new_trans.log_transaction()
    
    # Print tests
    print(inventory["ITM001"])
    print(transaction_history[0])