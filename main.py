import tkinter as tk
from grammar import print_cyk as cyk  # Import the CYK function from the grammar module


# Function to check if the input string is accepted by the grammar
def check():
    result = cyk(entry.get())  # Get the string from the entry widget and check it using CYK
    if result == "wrong":  # If the string contains symbols not in the terminals
        label_result.config(text="The string contains symbols not in the terminals.")
    elif result:  # If the string is accepted by the grammar
        label_result.config(text="The input string is accepted.")
    else:  # If the string is not accepted by the grammar
        label_result.config(text="The input string is not accepted.")


# Initialize the main window
root = tk.Tk()
root.title("CYK Parser")  # Set the window title
root.geometry("420x180")  # Set the window size

# Label for the string entry
label = tk.Label(root, text="String", width=10)
label.pack(pady=10)  # Add padding for better spacing

# Entry widget for the user to input the string
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to trigger the check function
button = tk.Button(root, text="Check", command=check)
button.pack(pady=5)

# Label to display the result
label_result = tk.Label(root, width=40, height=4, font=('Times New Roman', 14, 'bold'))
label_result.pack(pady=10)

# Start the main event loop
root.mainloop()
