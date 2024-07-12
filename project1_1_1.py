import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import floor

# Define the inverter dictionary (same as in your code)
inverters = {
    'SUN2000-3KTL-M1': {
        'Recommended max power': '4500Wp',
        'Max. output current': '5.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-4KTL-M1': {
        'Recommended max power': '6000Wp',
        'Max. output current': '6.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-5KTL-M1': {
        'Recommended max power': '7500Wp',
        'Max. output current': '8.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-6KTL-M1': {
        'Recommended max power': '9000Wp',
        'Max. output current': '10.1A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-8KTL-M1': {
        'Recommended max power': '12000Wp',
        'Max. output current': '13.5A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    'SUN2000-10KTL-M1': {
        'Recommended max power': '15000Wp',
        'Max. output current': '16.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-980'
    },
    #---
    'SUN2000-12KTL-M5': {
        'Recommended max power': '18000Wp',
        'Max. output current': '17.3A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-15KTL-M5': {
        'Recommended max power': '22500Wp',
        'Max. output current': '23.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-17KTL-M5': {
        'Recommended max power': '25500Wp',
        'Max. output current': '27.1A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-20KTL-M5': {
        'Recommended max power': '30000Wp',
        'Max. output current': '31.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-25KTL-M5': {
        'Recommended max power': '37500Wp',
        'Max. output current': '39.9A/400Vac',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #---------------
    'SUN2000-2KTL-L1': {
        'Recommended max power': '3000Wp',
        'Max. output current': '10A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-3KTL-L1': {
        'Recommended max power': '4500Wp',
        'Max. output current': '15A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-3.68KTL-L1': {
        'Recommended max power': '5520Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-4KTL-L1': {
        'Recommended max power': '6000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-4.6KTL-L1': {
        'Recommended max power': '6900Wp',
        'Max. output current': '23A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-5KTL-L1': {
        'Recommended max power': '7500Wp',
        'Max. output current': '25A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    'SUN2000-6KTL-L1': {
        'Recommended max power': '9000Wp',
        'Max. output current': '27.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '90-560'
    },
    #-------------------------------
    'NAC4K-DS': {
        'Recommended max power': '6000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    'NAC5K-DS': {
        'Recommended max power': '7500Wp',
        'Max. output current': '25A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    'NAC6K-DS': {
        'Recommended max power': '9000Wp',
        'Max. output current': '27.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '100-550'
    },
    #-------
    'R1-1K1-SS': {
        'Recommended max power': '1400Wp',
        'Max. output current': '5A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-1K6-SS': {
        'Recommended max power': '2400Wp',
        'Max. output current': '7.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-2K2-SS': {
        'Recommended max power': '2800Wp',
        'Max. output current': '9.6A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-2K7-SS': {
        'Recommended max power': '3500Wp',
        'Max. output current': '12.3A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-3K3-SS': {
        'Recommended max power': '4200Wp',
        'Max. output current': '15A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    'R1-3K7-SS': {
        'Recommended max power': '4800Wp',
        'Max. output current': '16A',
        'Grid connection': 'Single phase',
        'Operating voltage range': '50-500'
    },
    #------------------------
    'R3-4K-DT': {
        'Recommended max power': '6000Wp',
        'Max. output current': '6.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-5K-DT': {
        'Recommended max power': '7500Wp',
        'Max. output current': '8.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-6K-DT': {
        'Recommended max power': '9000Wp',
        'Max. output current': '10A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-8K-DT': {
        'Recommended max power': '12000Wp',
        'Max. output current': '13.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-10K-DT': {
        'Recommended max power': '15000Wp',
        'Max. output current': '16.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-12K-DT': {
        'Recommended max power': '18000Wp',
        'Max. output current': '20A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    'R3-15K-DT': {
        'Recommended max power': '22500Wp',
        'Max. output current': '22.7A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '140-950'
    },
    #---------------------------
    'R3-30K-G5': {
        'Recommended max power': '45000Wp',
        'Max. output current': '47.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-33K-G5': {
        'Recommended max power': '49500Wp',
        'Max. output current': '52.6A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-36K-G5': {
        'Recommended max power': '54000Wp',
        'Max. output current': '57.3A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'R3-40K-G5': {
        'Recommended max power': '60000Wp',
        'Max. output current': '63.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    #---------------------
    'SUN2000-30KTL-M3': {
        'Recommended max power': '30000Wp',
        'Max. output current': '47.9A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-36KTL-M3': {
        'Recommended max power': '36000Wp',
        'Max. output current': '58.0A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
    'SUN2000-40KTL-M3': {
        'Recommended max power': '40000Wp',
        'Max. output current': '63.8A',
        'Grid connection': 'Three phase',
        'Operating voltage range': '200-1000'
    },
}

# Function to calculate and display suitable inverters
def calculate_inverters():
    try:
        conso = int(entry_consumption.get())
        p1 = conso / 1600
        if p1 > 4:
            number_panels = floor(p1 / 0.590)
            p_f = number_panels * 590
        else:
            number_panels = floor(p1 / 0.420)
            p_f = number_panels * 420

        suitable_inverters = []
        for inverter, specs in inverters.items():
            max_power = int(specs['Recommended max power'].replace('Wp', ''))
            ratio = p_f / max_power
            if 0.9 < ratio < 1.3:
                suitable_inverters.append((inverter, specs))

        results_text.config(state=tk.NORMAL)
        results_text.delete('1.0', tk.END)
        results_text.insert(tk.END, f"Number of panels required: {number_panels}\n")
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

# Create main window
root = tk.Tk()
root.title("Solar Inverter Selector")

# Create and place widgets with improved styling
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_consumption = tk.Label(frame, text="Enter your consumption in W:", font=("Arial", 12))
label_consumption.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

entry_consumption = tk.Entry(frame, width=10, font=("Arial", 12))
entry_consumption.grid(row=0, column=1, padx=10, pady=5)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_inverters, font=("Arial", 12), bg='#4CAF50', fg='white')
calculate_button.grid(row=1, columnspan=2, pady=10)

results_text = tk.Text(frame, height=15, width=60, font=("Arial", 12), wrap=tk.WORD)
results_text.grid(row=2, columnspan=2, pady=10, padx=10)
results_text.config(state=tk.DISABLED)

# Start the main loop
root.mainloop()