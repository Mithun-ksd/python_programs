import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os

def initialize_csv():
    """Initialize the CSV file if it doesn't exist"""
    if not os.path.exists('batsman_scores.csv'):
        try:
            with open('batsman_scores.csv', 'w') as file:
                file.write("Batsman,2017,2018,2019,2020")
        except Exception as e:
            print(f"Error initializing file: {e}")

def add_data():
    try:
        batsman = batsman_entry.get().strip()
        if not batsman:
            messagebox.showerror("Input Error", "Please enter a batsman name.")
            return
            
        scores = [
            int(score_entry_2017.get()), 
            int(score_entry_2018.get()),
            int(score_entry_2019.get()), 
            int(score_entry_2020.get())
        ]
        
        with open('batsman_scores.csv', 'a') as file:
            file.write(f"\n{batsman},{','.join(map(str, scores))}")
            
        messagebox.showinfo("Success", "Data saved successfully!")
        
        # Clear all fields
        batsman_entry.delete(0, 'end')
        score_entry_2017.delete(0, 'end')
        score_entry_2018.delete(0, 'end')
        score_entry_2019.delete(0, 'end')
        score_entry_2020.delete(0, 'end')
        
        batsman_entry.focus_set() 
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer scores.")

def plot_graph():
    try:
        data = pd.read_csv('batsman_scores.csv')
        
        if len(data) == 0:
            messagebox.showerror("No Data", "Please add data before plotting.")
            return
        
        batsmen = data['Batsman']
        scores = data.drop('Batsman', axis=1).values.tolist()
        years = list(data.columns[1:])
        
        x = range(len(years))
        width = 0.75 
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        for i, batsman_scores in enumerate(scores):
            pos = [p + i * width / len(scores) for p in x] 
            ax.bar(pos, batsman_scores, width/len(scores), label=batsmen[i])
            
        ax.set_xticks([p + 0.5 * width / len(scores) for p in x])
        ax.set_xticklabels(years)
        ax.set_ylabel('Score', fontweight='bold', fontsize=15)
        ax.set_xlabel('Year', fontweight='bold', fontsize=15)
        ax.set_title('Scores by Batsman', fontweight='bold', fontsize=15)
        ax.legend()
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        messagebox.showerror("File Error", "No data file found. Please add data first.")
    except Exception as e:
        messagebox.showerror("Plot Error", f"Could not plot graph: {e}")


# Initialize CSV file on startup
initialize_csv()

root = tk.Tk()
root.title("Batsman Scores")

batsman_label = ttk.Label(root, text="Batsman:")
batsman_label.grid(row=0, column=0, padx=5, pady=5)
batsman_entry = ttk.Entry(root)
batsman_entry.grid(row=0, column=1, padx=5, pady=5)

score_label = ttk.Label(root, text="Scores:")
score_label.grid(row=1, column=0, padx=5, pady=5)

score_entry_2017 = ttk.Entry(root)
score_entry_2017.grid(row=1, column=1, padx=5, pady=5)
score_2017_label = ttk.Label(root, text="2017")
score_2017_label.grid(row=2, column=1, padx=5, pady=5)

score_entry_2018 = ttk.Entry(root)
score_entry_2018.grid(row=1, column=2, padx=5, pady=5)
score_2018_label = ttk.Label(root, text="2018")
score_2018_label.grid(row=2, column=2, padx=5, pady=5)

score_entry_2019 = ttk.Entry(root)
score_entry_2019.grid(row=1, column=3, padx=5, pady=5)
score_2019_label = ttk.Label(root, text="2019")
score_2019_label.grid(row=2, column=3, padx=5, pady=5)

score_entry_2020 = ttk.Entry(root)
score_entry_2020.grid(row=1, column=4, padx=5, pady=5)
score_2020_label = ttk.Label(root, text="2020")
score_2020_label.grid(row=2, column=4, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Data", command=add_data)
add_button.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

plot_button = ttk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

root.mainloop()
