import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import floor
from tkinter import filedialog


# Define the inverter dictionary (same as in your code)
inverters = {
    'SUN2000-3KTL-M1': {
        'Output Power': '3000Wp',
        'Max. output current': '5.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-4KTL-M1': {
        'Output Power': '4000Wp',
        'Max. output current': '6.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-5KTL-M1': {
        'Output Power': '5000Wp',
        'Max. output current': '8.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-6KTL-M1': {
        'Output Power': '6000Wp',
        'Max. output current': '10.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-8KTL-M1': {
        'Output Power': '8000Wp',
        'Max. output current': '13.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-10KTL-M1': {
        'Output Power': '10000Wp',
        'Max. output current': '16.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    #---
    'SUN2000-12KTL-M5': {
        'Output Power': '12000Wp',
        'Max. output current': '17.3A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-15KTL-M5': {
        'Output Power': '15000Wp',
        'Max. output current': '23.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-17KTL-M5': {
        'Output Power': '17000Wp',
        'Max. output current': '27.1A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-20KTL-M5': {
        'Output Power': '20000Wp',
        'Max. output current': '31.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-25KTL-M5': {
        'Output Power': '25000Wp',
        'Max. output current': '39.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #---------------
    'SUN2000-2KTL-L1': {
        'Output Power': '2000Wp',
        'Max. output current': '10A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-3KTL-L1': {
        'Output Power': '3000Wp',
        'Max. output current': '15A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-3.68KTL-L1': {
        'Output Power': '3680Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-4KTL-L1': {
        'Output Power': '4000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-4.6KTL-L1': {
        'Output Power': '4600Wp',
        'Max. output current': '23A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-5KTL-L1': {
        'Output Power': '5000Wp',
        'Max. output current': '25A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-6KTL-L1': {
        'Output Power': '6000Wp',
        'Max. output current': '27.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    #-------------------------------
    'NAC4K-DS': {
        'Output Power': '4000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    'NAC5K-DS': {
        'Output Power': '5000Wp',
        'Max. output current': '25A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    'NAC6K-DS': {
        'Output Power': '6000Wp',
        'Max. output current': '27.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    #-------
    'R1-1K1-SS': {
        'Output Power': '1000Wp',
        'Max. output current': '5A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-1K6-SS': {
        'Output Power': '1000Wp',
        'Max. output current': '7.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-2K2-SS': {
        'Output Power': '2000Wp',
        'Max. output current': '9.6A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-2K7-SS': {
        'Output Power': '2000Wp',
        'Max. output current': '12.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-3K3-SS': {
        'Output Power': '3000Wp',
        'Max. output current': '15A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-3K7-SS': {
        'Output Power': '3000Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    #------------------------
    'R3-4K-DT': {
        'Output Power': '4000Wp',
        'Max. output current': '6.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-5K-DT': {
        'Output Power': '5000Wp',
        'Max. output current': '8.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-6K-DT': {
        'Output Power': '6000Wp',
        'Max. output current': '10A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-8K-DT': {
        'Output Power': '8000Wp',
        'Max. output current': '13.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-10K-DT': {
        'Output Power': '10000Wp',
        'Max. output current': '16.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-12K-DT': {
        'Output Power': '12000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-15K-DT': {
        'Output Power': '15000Wp',
        'Max. output current': '22.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    #---------------------------
    'R3-30K-G5': {
        'Output Power': '30000Wp',
        'Max. output current': '47.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-33K-G5': {
        'Output Power': '33000Wp',
        'Max. output current': '52.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-36K-G5': {
        'Output Power': '36000Wp',
        'Max. output current': '57.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-40K-G5': {
        'Output Power': '40000Wp',
        'Max. output current': '63.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #---------------------
    'SUN2000-30KTL-M3': {
        'Output Power': '30000Wp',
        'Max. output current': '47.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-36KTL-M3': {
        'Output Power': '36000Wp',
        'Max. output current': '58.0A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-40KTL-M3': {
        'Output Power': '40000Wp',
        'Max. output current': '63.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
}

# Function to calculate and display suitable inverters
def calculate_inverters():
    try:
        client_name = entry_client_name.get().strip()
        conso = int(entry_consumption.get())
        p1 = conso / 1600
        if p1 > 4.2:
            number_panels = floor(p1 / 0.590)
            p_f = number_panels * 590
        else:
            number_panels = floor(p1 / 0.420)
            p_f = number_panels * 420

        suitable_inverters = []
        for inverter, specs in inverters.items():
            max_power = int(specs['Output Power'].replace('Wp', ''))
            ratio = p_f / max_power
            if 0.9 < ratio < 1.3:
                suitable_inverters.append((inverter, specs))
            if p1 > 4:
                panel_wattage = 590
            else:
                panel_wattage = 420
        results_text.config(state=tk.NORMAL)
        results_text.delete('1.0', tk.END)
        results_text.insert(tk.END, f"Client's Name: {client_name}\n")
        results_text.insert(tk.END, f"Number of panels required: {number_panels}\n")
        results_text.insert(tk.END, f"You have to use {panel_wattage}W panel.\n")
        results_text.insert(tk.END, f"Total power from panels: {p_f}W\n\n")


        if suitable_inverters:
            results_text.insert(tk.END, "Suitable Inverters:\n")
            results_text.insert(tk.END, "-------------------\n")
            for inverter, specs in suitable_inverters:
                results_text.insert(tk.END, f"Inverter Model: {inverter}\n")
                for key, value in specs.items():
                    results_text.insert(tk.END, f"  {key}: {value}\n")
                results_text.insert(tk.END, "\n")
        else:
            results_text.insert(tk.END, "No suitable inverters found.\n")
        
        results_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for consumption.")

# Function to save results to a file
def save_results():
    try:
        client_name = entry_client_name.get().strip()
        filename = filedialog.asksaveasfilename(
            defaultextension='.txt', 
            filetypes=[('Text files', '*.txt'), ('All files', '*.*')],
            initialfile=f"{client_name}_results.txt" if client_name else "results.txt"
        )
        if filename:
            with open(filename, 'w') as f:
                f.write(results_text.get('1.0', tk.END))
            messagebox.showinfo("Success", "Results saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save results: {e}")

# Create main window
root = tk.Tk()
root.title("Solar Inverter Selector")

# Colors for improved user interface
primary_color = '#4CAF50'  # Green
secondary_color = '#008CBA'  # Blue
accent_color = '#f44336'  # Red
background_color = '#E0F7FA'  # Light Blue

# Create and place widgets with improved styling
main_frame = tk.Frame(root, padx=20, pady=20, bg=background_color)  # Light blue background
main_frame.pack(fill=tk.BOTH, expand=True)

# Header label
header_label = tk.Label(main_frame, text="Solar Inverter Selector", font=("Arial", 20), bg=background_color)  # Light blue background
header_label.pack(pady=(0, 20))

# Client name input
client_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
client_frame.pack()

label_client_name = tk.Label(client_frame, text="Client Name:", font=("Arial", 12), bg=background_color)
label_client_name.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

entry_client_name = tk.Entry(client_frame, width=30, font=("Arial", 12))
entry_client_name.grid(row=0, column=1, padx=10, pady=10)

# Input frame
input_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
input_frame.pack()

label_consumption = tk.Label(input_frame, text="Enter your consumption in W:", font=("Arial", 12), bg=background_color)  # Light blue background
label_consumption.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

entry_consumption = tk.Entry(input_frame, width=10, font=("Arial", 12))
entry_consumption.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(input_frame, text="Calculate", command=calculate_inverters, font=("Arial", 12), bg=primary_color, fg='white')
calculate_button.grid(row=0, column=2, padx=10, pady=10)

# Results frame
results_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
results_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

results_text = tk.Text(results_frame, height=15, width=80, font=("Arial", 12), wrap=tk.WORD)
results_text.pack(padx=20, pady=20)

# Buttons frame
buttons_frame = tk.Frame(main_frame, bg=background_color)  # Light blue background
buttons_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

save_button = tk.Button(buttons_frame, text="Save Results", command=save_results, font=("Arial", 12), bg=secondary_color, fg='white')
save_button.pack(side=tk.LEFT, padx=20, pady=10)

exit_button = tk.Button(buttons_frame, text="Exit", command=root.quit, font=("Arial", 12), bg=accent_color, fg='white')
exit_button.pack(side=tk.RIGHT, padx=20, pady=10)

# Start the main loop
root.mainloop()