import tkinter as tk

def check_reaction():
    user_input = ""
    for entry_var in entry_vars:
        user_input += entry_var.get()
    if user_input == original_atoms:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect. Try again.")

def create_reaction_window(reaction):
    root = tk.Tk()
    root.title("Chemical Reaction Guessing Game")

    global original_atoms
    original_atoms = ''.join([char if char.isalpha() else ' ' for char in reaction])

    # Create labels and entry widgets for the user to input their guesses
    global entry_vars
    entry_vars = []
    for char in reaction:
        if char.isalpha():
            entry_var = tk.StringVar()
            entry = tk.Entry(root, textvariable=entry_var, width=2)
            entry.grid(row=0, column=len(entry_vars), padx=2, pady=5)
            entry_vars.append(entry_var)
        else:
            label = tk.Label(root, text=char)
            label.grid(row=0, column=len(entry_vars), padx=2, pady=5)

    # Submit button to check user's guesses
    submit_button = tk.Button(root, text="Submit", command=check_reaction)
    submit_button.grid(row=1, column=0, columnspan=len(original_atoms), pady=10)

    # Label to display the result of the guess
    global result_label
    result_label = tk.Label(root, text="")
    result_label.grid(row=2, column=0, columnspan=len(original_atoms), pady=5)

    root.mainloop()

# Example usage:
reaction = "2H2O -> 2H2 + O2"
create_reaction_window(reaction)
