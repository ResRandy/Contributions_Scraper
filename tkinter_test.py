import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from matcher import findContributions



def select_open_selection():
    new_window = tk.Toplevel(master)
    new_window.geometry("900x600")
    new_window.title("This is test")
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)
    entry_var = tk.StringVar()
    entry = tk.Entry(new_window, textvariable=entry_var)
    entry.pack()

def open_file_dialog():
    try:
        file_path = filedialog.askopenfilenames(
            title="Select a file",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
            multiple=True
        )

        if not file_path:
            print(f"{file_path}, Is not a file.")
            return
        
        text_content = findContributions(file_path)
        

        text_area.config(state='normal')
            
        # Clear existing text and insert new content
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, text_content)

        text_area.config(state='disabled')
        

    except FileNotFoundError:
        messagebox.showerror("Error", "The selected file was not found.")
    except UnicodeDecodeError:
        messagebox.showerror("Error", "Unable to decode the selected file.")
    except Exception as e:
        messagebox.showerror("Error", f"\nAn unexpected error occurred:\n" + str(e))


master = tk.Tk()
master.geometry("900x600")
master.title("Main window")
Label(master, text="Click the button to select a file and the results shall appear in the box below").pack(pady=7)
findFileButton = tk.Button(master, text="open file explorer", command=open_file_dialog).pack(pady=5)
text_area = tk.Text(master, wrap='word', height=10)
text_area.pack(pady=20,expand=True, fill='both')
text_area.config(state='disabled')


# #create menue
# menubar = tk.Menu(master)
# filemenu = tk.Menu(menubar, tearoff=0)
# filemenu.add_command(label="Open", command=open_file_dialog())
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=master.quit)
# menubar.add_cascade(label="File", menu=filemenu)

# master.config(menu=menubar)


master.mainloop()