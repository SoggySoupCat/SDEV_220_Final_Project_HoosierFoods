import tkinter as tk
from tkinter import ttk, messagebox

# Author: Ryan A Musick
# Role: GUI & Frontend Lead
# Project: Hoosier Hills Food Bank Inventory Management

class FoodBankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure layout geometry and window properties
        self.title("Hoosier Hills Food Bank - Inventory Management")
        self.geometry("800x600")
        self.configure(padx=10, pady=10)

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
        stock_frame = ttk.Frame(self.notebook)
        self.notebook.add(stock_frame, text="Stock Entry")
        
        # Grid layout for input fields
        ttk.Label(stock_frame, text="Item Name:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.item_name_entry = ttk.Entry(stock_frame, width=30)
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(stock_frame, text="Quantity:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.qty_entry = ttk.Entry(stock_frame, width=30)
        self.qty_entry.grid(row=1, column=1, padx=10, pady=10)

        # Event binding for user input validation and submission
        submit_btn = ttk.Button(stock_frame, text="Add Item", command=self.validate_and_submit_item)
        submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

    def create_donor_frame(self):
        """Builds the donor management tab."""
        donor_frame = ttk.Frame(self.notebook)
        self.notebook.add(donor_frame, text="Donors")
        
        # Placeholder layout for Thomas to connect the Donor class
        ttk.Label(donor_frame, text="Donor Contact & History Management", font=('Helvetica', 14, 'bold')).pack(pady=20)

    def create_transaction_frame(self):
        """Builds the incoming/outgoing distribution tab."""
        trans_frame = ttk.Frame(self.notebook)
        self.notebook.add(trans_frame, text="Transactions")
        
        # Placeholder layout for Thomas to connect the Transaction class
        ttk.Label(trans_frame, text="Process Incoming & Outgoing Distributions", font=('Helvetica', 14, 'bold')).pack(pady=20)

    def create_reporting_frame(self):
        """Builds the reporting and activity history tab."""
        report_frame = ttk.Frame(self.notebook)
        self.notebook.add(report_frame, text="Reporting")
        
        ttk.Label(report_frame, text="System Reporting & Activity Logs", font=('Helvetica', 14, 'bold')).pack(pady=20)

    def validate_and_submit_item(self):
        """Handles user input validation before passing data to the backend."""
        item_name = self.item_name_entry.get().strip()
        qty = self.qty_entry.get().strip()

        # Input validation checks
        if not item_name:
            messagebox.showerror("Input Error", "Item Name cannot be empty.")
            return
        
        if not qty.isdigit():
            messagebox.showerror("Input Error", "Quantity must be a valid number.")
            return

        # Placeholder for instantiating Thomas's Item class and storing in the dictionary
        print(f"Success: Ready to instantiate Item('{item_name}', {qty}) and add to dictionary lookup.")
        
        # Clear fields after successful entry
        self.item_name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        
        messagebox.showinfo("Success", f"Item '{item_name}' added successfully.")

if __name__ == "__main__":
    app = FoodBankApp()
    app.mainloop()