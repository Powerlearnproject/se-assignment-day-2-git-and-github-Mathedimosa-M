import tkinter as tk 
from tkinter import ttk, messagebox

class CyclistRegistrationApp: 
    def __init__(self, root): self.root = root 
    #self.root.title("Cyclist Registration") 
    self.cyclists = []  # type: ignore

        # Create GUI widgets
    self.name_label = tk.Label(root, text="Name:")  # type: ignore
    self.name_label.grid(column=0, row=0) # type: ignore
    self.name_entry = tk.Entry(root)  # type: ignore
    self.name_entry.grid(column=1, row=0)  # type: ignore

    self.surname_label = tk.Label(root, text="Surname:")  # type: ignore

    self.surname_label.grid(column=0, row=1)  # type: ignore
    self.surname_entry = tk.Entry(root)  # type: ignore
    self.surname_entry.grid(column=1, row=1)  # type: ignore

    self.gender_label = tk.Label(root, text="Gender:")  # type: ignore
    self.gender_label.grid(column=0, row=2)  # type: ignore
    self.gender_var = tk.StringVar() # type: ignore
    self.gender_combo = ttk.Combobox(root, textvariable=self.gender_var)  # type: ignore
    self.gender_combo['values'] = ('Male', 'Female', 'Other')  # type: ignore
    self.gender_combo.grid(column=1, row=2)  # type: ignore

    self.add_button = tk.Button(root, text="Add Cyclist", command=self.add_cyclist)  # type: ignore
    self.add_button.grid(column=1, row=3)  # type: ignore

    self.edit_button = tk.Button(root, text="Edit Cyclist", command=self.edit_cyclist)  # type: ignore
    self.edit_button.grid(column=1, row=4) # type: ignore
        
    self.delete_button = tk.Button(root, text="Delete Cyclist", command=self.delete_cyclist)  # type: ignore
    self.delete_button.grid(column=1, row=5)  # type: ignore
    self.list_label = tk.Label(root, text="Registered Cyclists:")  # type: ignore
    self.list_label.grid(column=0, row=6)  # type: ignore
    self.cyclist_list = tk.Text(root)  # type: ignore
    self.cyclist_list.grid(column=0, row=7, columnspan=2) # type: ignore
         
    def add_cyclist(self): name = self.name_entry.get() 
    surname = self.surname_entry.get()  # type: ignore
    gender = self.gender_var.get()  # type: ignore
    if name and surname and gender: # type: ignore
            self.cyclists.append((name, surname, gender))  # type: ignore
            self.update_list()  # type: ignore
            self.clear_entries()  # type: ignore
    else: 
            messagebox.showerror("Error", "Please fill in all fields.") 

def edit_cyclist(self):
    try:                            
        index = int(self.cyclist_list.get('1.0', tk.END).split('\n').index(self.name_entry.get() + ' ' + self.surname_entry.get() + ' (' + self.gender_var.get() + ')')) - 1 
        self.cyclists[index] = (self.name_entry.get(), self.surname_entry.get(), self.gender_var.get()) 
        self.update_list() 
        self.clear_entries()
    except ValueError: 
                
        messagebox.showerror("Error", "Cyclist not found.")
  
def delete_cyclist(self):
    
    try:
        index = int(self.cyclist_list.get('1.0', tk.END).split('\n').index(self.name_entry.get() + ' ' + self.surname_entry.get() + ' (' + self.gender_var.get() + ')')) - 1
         
        del self.cyclists[index] 
        self.update_list() 
        self.clear_entries() 
    except ValueError: 

        messagebox.showerror("Error", "Cyclist not found.") 

        def update_list(self): 
            self.cyclist_list.delete('1.0', tk.END) 
        for cyclist in self.cyclists: 

            self.cyclist_list.insert(tk.END, f"{cyclist[0]} {cyclist[1]} ({cyclist[2]})\n")
  
    def clear_entries(self): 
        self.name_entry.delete(0, tk.END) 
        self.surname_entry.delete(0, tk.END) 
        self.gender_var.set('') 

if __name__ == "__main__":
    root = "(link unavailable)"() 
    app = CyclistRegistrationApp(root)
    root.mainloop() 
