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
        trans_frame = ttk.Frame(self.notebook)  
        self.notebook.add(trans_frame, text="Transactions")  
          
        ttk.Label(trans_frame, text="Process Incoming & Outgoing Distributions", style='Header.TLabel').pack(pady=20)  
         
    def create_reporting_frame(self):  
        """Builds the reporting and activity history tab."""  
        report_frame = ttk.Frame(self.notebook)  
        self.notebook.add(report_frame, text="Reporting")  
          
        ttk.Label(report_frame, text="System Reporting & Activity Logs", style='Header.TLabel').pack(pady=20)  
         
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

    def validate_and_log_donation(self):
        """Handles user input validation for logging a donation before passing to backend."""
        donor_name = self.donor_name_entry.get().strip()
        item = self.donated_item_entry.get().strip()
        qty = self.donated_qty_entry.get().strip()

        # Input validation checks
        if not donor_name or not item:
            messagebox.showerror("Input Error", "Donor Name and Item Donated cannot be empty.")
            return

        if not qty.isdigit():
            messagebox.showerror("Input Error", "Quantity must be a valid number.")
            return

        # Placeholder for instantiating Thomas's Donor and Transaction classes
        print(f"Success: Ready to create Transaction for {donor_name} donating {qty} of '{item}'.")
        
        # Clear fields after successful entry
        self.donor_name_entry.delete(0, tk.END)
        self.donor_contact_entry.delete(0, tk.END)
        self.donated_item_entry.delete(0, tk.END)
        self.donated_qty_entry.delete(0, tk.END)

        messagebox.showinfo("Success", f"Donation from '{donor_name}' logged successfully.")
         
if __name__ == "__main__":  
    app = FoodBankApp()  
    app.mainloop()
