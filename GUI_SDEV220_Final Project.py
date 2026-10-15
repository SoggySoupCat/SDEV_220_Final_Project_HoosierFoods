import tkinter as tk  
from tkinter import ttk, messagebox  
  
# Author: Ryan Musick  
# Role: GUI & Frontend Lead  
# Project: Hoosier Hills Food Bank Inventory Management  
  
class FoodBankApp(tk.Tk):  
    def __init__(self):  
        super().__init__()  
          
        # Configure layout geometry and window properties  
        self.title("Hoosier Hills Food Bank - Inventory Management")  
        self.geometry("800x600")  
        self.configure(padx=10, pady=10)  

        # Apply global styling 
        style = ttk.Style(self)
        style.theme_use('clam')  
        style.configure('TFrame', background='#f4f4f4')
        style.configure('TLabel', background='#f4f4f4', font=('Arial', 11))
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'), foreground='#333333')
        style.configure('TButton', font=('Arial', 10, 'bold'), padding=5)
        
        # Implement navigation using a Notebook (tabbed interface)  
        self.notebook = ttk.Notebook(self)  
        self.notebook.pack(expand=True, fill='both')  
         
        # Initialize the primary GUI sections  
        self.create_stock_frame()  
        self.create_donor_frame()  
        self.create_transaction_frame()  
        self.create_reporting_frame()  
         
    def create_stock_frame(self):  
        """Builds the stock entry and inventory management tab."""  
        stock_frame = ttk.Frame(self.notebook, padding="20 20 20 20")
        self.notebook.add(stock_frame, text="Stock Entry")  
        
        stock_frame.columnconfigure(1, weight=1) 
          
        # Grid layout for input fields
        ttk.Label(stock_frame, text="Add New Inventory", style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

        ttk.Label(stock_frame, text="Item Name:").grid(row=1, column=0, pady=10, sticky='e')  
        self.item_name_entry = ttk.Entry(stock_frame, width=40)  
        self.item_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')  
         
        ttk.Label(stock_frame, text="Quantity:").grid(row=2, column=0, pady=10, sticky='e')  
        self.qty_entry = ttk.Entry(stock_frame, width=40)  
        self.qty_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')  
         
        submit_btn = ttk.Button(stock_frame, text="Add Item", command=self.validate_and_submit_item)  
        submit_btn.grid(row=3, column=0, columnspan=2, pady=20)  

        # Treeview for data display
        ttk.Separator(stock_frame, orient='horizontal').grid(row=4, column=0, columnspan=2, sticky='we', pady=20)
        
        ttk.Label(stock_frame, text="Current Inventory", style='Header.TLabel').grid(row=5, column=0, columnspan=2, sticky='w')

        columns = ('item_name', 'quantity')
        self.tree = ttk.Treeview(stock_frame, columns=columns, show='headings', height=10)
        self.tree.heading('item_name', text='Item Name')
        self.tree.heading('quantity', text='Quantity')
        
        self.tree.column('item_name', width=300)
        self.tree.column('quantity', width=100, anchor='center')
        
        self.tree.grid(row=6, column=0, columnspan=2, sticky='nsew', pady=10)
        stock_frame.rowconfigure(6, weight=1)
         
    def create_donor_frame(self):  
        """Builds the donor management and donation logging tab."""  
        donor_frame = ttk.Frame(self.notebook, padding="20 20 20 20")  
        self.notebook.add(donor_frame, text="Donors")  
        
        # Configure grid column weights for responsive expansion
        donor_frame.columnconfigure(1, weight=1)
          
        # Header 
        ttk.Label(donor_frame, text="Log a New Donation", style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')  
         
        # Input fields 
        ttk.Label(donor_frame, text="Donor Name:").grid(row=1, column=0, pady=10, sticky='e')
        self.donor_name_entry = ttk.Entry(donor_frame, width=40)
        self.donor_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky='we')

        ttk.Label(donor_frame, text="Contact Info:").grid(row=2, column=0, pady=10, sticky='e')
        self.donor_contact_entry = ttk.Entry(donor_frame, width=40)
        self.donor_contact_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')

        ttk.Label(donor_frame, text="Item Donated:").grid(row=3, column=0, pady=10, sticky='e')
        self.donated_item_entry = ttk.Entry(donor_frame, width=40)
        self.donated_item_entry.grid(row=3, column=1, padx=10, pady=10, sticky='we')

        ttk.Label(donor_frame, text="Quantity:").grid(row=4, column=0, pady=10, sticky='e')
        self.donated_qty_entry = ttk.Entry(donor_frame, width=40)
        self.donated_qty_entry.grid(row=4, column=1, padx=10, pady=10, sticky='we')

        # Submit button
        log_donation_btn = ttk.Button(donor_frame, text="Log Donation", command=self.validate_and_log_donation)
        log_donation_btn.grid(row=5, column=0, columnspan=2, pady=30)
         
    def create_transaction_frame(self):  
        """Builds the incoming/outgoing distribution tab."""  
        trans_frame = ttk.Frame(self.notebook, padding="20 20 20 20")  
        self.notebook.add(trans_frame, text="Transactions")  
        
        # Configure grid column weights for responsive expansion
        trans_frame.columnconfigure(1, weight=1)

        # Header
        ttk.Label(trans_frame, text="Process a Transaction", style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')  
        
        # Input fields
        ttk.Label(trans_frame, text="Transaction Type:").grid(row=1, column=0, pady=10, sticky='e')
        self.trans_type_combo = ttk.Combobox(trans_frame, values=["Incoming", "Outgoing"], state="readonly", width=37)
        self.trans_type_combo.grid(row=1, column=1, padx=10, pady=10, sticky='we')
        self.trans_type_combo.set("Outgoing")  # Set default value

        ttk.Label(trans_frame, text="Item Name:").grid(row=2, column=0, pady=10, sticky='e')
        self.trans_item_entry = ttk.Entry(trans_frame, width=40)
        self.trans_item_entry.grid(row=2, column=1, padx=10, pady=10, sticky='we')

        ttk.Label(trans_frame, text="Quantity:").grid(row=3, column=0, pady=10, sticky='e')
        self.trans_qty_entry = ttk.Entry(trans_frame, width=40)
        self.trans_qty_entry.grid(row=3, column=1, padx=10, pady=10, sticky='we')

        ttk.Label(trans_frame, text="Partner/Donor Name:").grid(row=4, column=0, pady=10, sticky='e')
        self.trans_entity_entry = ttk.Entry(trans_frame, width=40)
        self.trans_entity_entry.grid(row=4, column=1, padx=10, pady=10, sticky='we')

        # Submit button
        process_btn = ttk.Button(trans_frame, text="Process Transaction", command=self.validate_and_process_transaction)
        process_btn.grid(row=5, column=0, columnspan=2, pady=30)
         
    def create_reporting_frame(self):  
        """Builds the reporting and activity history tab."""  
        report_frame = ttk.Frame(self.notebook, padding="20 20 20 20")  
        self.notebook.add(report_frame, text="Reporting")  
          
        ttk.Label(report_frame, text="System Reporting & Activity Logs", style='Header.TLabel').pack(pady=20)  

    def refresh_inventory_table(self):
        """Clears the Treeview and repopulates it from the backend inventory."""
        # Delete all existing rows in the display table
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        # Loop through the backend dictionary and insert current data
        for item in backend.inventory.values():
            self.tree.insert('', tk.END, values=(item.name, item.quantity))
         
    def validate_and_submit_item(self):  
        """Handles user input validation and passes data to backend."""  
        item_name = self.item_name_entry.get().strip()  
        qty = self.qty_entry.get().strip()  
         
        # Input validation checks  
        if not item_name:  
            messagebox.showerror("Input Error", "Item Name cannot be empty.")  
            return  
        if not qty.isdigit():  
            messagebox.showerror("Input Error", "Quantity must be a valid number.")  
            return  
         
        qty = int(qty)
        # Generate ID based on the backend dictionary length
        new_id = f"ITM{len(backend.inventory) + 1:03d}"
        
        # Instantiate backend Item and store it in the global inventory dictionary
        new_item = backend.Item(new_id, item_name, qty, "Uncategorized", "N/A")
        backend.inventory[new_id] = new_item
        
        # Update the visual Treeview using the refresh method
        self.refresh_inventory_table()
          
        # Clear fields 
        self.item_name_entry.delete(0, tk.END)  
        self.qty_entry.delete(0, tk.END)  
          
        messagebox.showinfo("Success", f"Item '{item_name}' added successfully.") 

    def validate_and_log_donation(self):
        """Handles user input validation for logging a donation and passes to backend."""
        donor_name = self.donor_name_entry.get().strip()
        contact_info = self.donor_contact_entry.get().strip()
        item_name = self.donated_item_entry.get().strip()
        qty = self.donated_qty_entry.get().strip()

        # Input validation checks
        if not donor_name or not item_name:
            messagebox.showerror("Input Error", "Donor Name and Item Donated cannot be empty.")
            return

        if not qty.isdigit() or int(qty) <= 0:
            messagebox.showerror("Input Error", "Quantity must be a valid positive number.")
            return

        qty = int(qty)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Manage the Donor via backend global list
        donor = next((d for d in backend.donor_history if d.name.lower() == donor_name.lower()), None)
        if not donor:
            donor_id = f"DNR{len(backend.donor_history) + 1:03d}"
            donor = backend.Donor(donor_id, donor_name, contact_info)
            backend.donor_history.append(donor)
        else:
            donor_id = donor.donor_id

        # Manage the Inventory Item via backend global dictionary
        found_item = next((i for i in backend.inventory.values() if i.name.lower() == item_name.lower()), None)
        if found_item:
            found_item.update_quantity(qty)
            item_id = found_item.item_id
        else:
            item_id = f"ITM{len(backend.inventory) + 1:03d}"
            new_item = backend.Item(item_id, item_name, qty, "Uncategorized", "N/A")
            backend.inventory[item_id] = new_item

        # Create Transaction, log it, and append to Donor history
        trans_id = f"TRX{len(backend.transaction_history) + 1:03d}"
        transaction = backend.Transaction(trans_id, "Incoming", item_id, qty, current_date, donor_id)
        
        transaction.log_transaction()
        donor.add_donation(item_id, qty, current_date)
        
        # Update the visual Treeview
        self.refresh_inventory_table()

        # Clear fields after successful entry
        self.donor_name_entry.delete(0, tk.END)
        self.donor_contact_entry.delete(0, tk.END)
        self.donated_item_entry.delete(0, tk.END)
        self.donated_qty_entry.delete(0, tk.END)

        messagebox.showinfo("Success", f"Donation from '{donor_name}' logged successfully.")

    def validate_and_process_transaction(self):
        """Handles user input validation and logs incoming/outgoing distributions."""
        trans_type = self.trans_type_combo.get()
        item_name = self.trans_item_entry.get().strip()
        qty = self.trans_qty_entry.get().strip()
        entity = self.trans_entity_entry.get().strip()

        # Input validation
        if not trans_type or not item_name or not entity:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        if not qty.isdigit() or int(qty) <= 0:
            messagebox.showerror("Input Error", "Quantity must be a positive number.")
            return

        qty = int(qty)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Find the item in the backend inventory
        found_item = next((i for i in backend.inventory.values() if i.name.lower() == item_name.lower()), None)

        if trans_type == "Outgoing":
            if not found_item:
                messagebox.showerror("Inventory Error", f"Item '{item_name}' does not exist in inventory.")
                return
            if found_item.quantity < qty:
                messagebox.showerror("Inventory Error", f"Not enough '{item_name}' in stock. Current quantity: {found_item.quantity}")
                return
            
            # Subtract stock using backend update_quantity method
            found_item.update_quantity(-qty)
            item_id = found_item.item_id
            
        elif trans_type == "Incoming":
            if found_item:
                found_item.update_quantity(qty)
                item_id = found_item.item_id
            else:
                # Create new item if it doesn't exist
                item_id = f"ITM{len(backend.inventory) + 1:03d}"
                new_item = backend.Item(item_id, item_name, qty, "Uncategorized", "N/A")
                backend.inventory[item_id] = new_item

        # Create and log transaction 
        trans_id = f"TRX{len(backend.transaction_history) + 1:03d}"
        transaction = backend.Transaction(trans_id, trans_type, item_id, qty, current_date, entity)
        transaction.log_transaction()

        # Instantly update the visual table on the Stock Entry tab
        self.refresh_inventory_table()

        # Clear fields
        self.trans_item_entry.delete(0, tk.END)
        self.trans_qty_entry.delete(0, tk.END)
        self.trans_entity_entry.delete(0, tk.END)

        messagebox.showinfo("Success", f"{trans_type} transaction for '{item_name}' processed successfully.")
         
if __name__ == "__main__":  
    app = FoodBankApp()  
    app.mainloop()
