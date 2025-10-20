import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog, messagebox
import pymupdf
# from matcher import findContributions



def select_open_selection():
    new_window = tk.Toplevel(master)
    new_window.geometry("400x200")
    new_window.title("This is test")
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)
    entry_var = tk.StringVar()
    entry = tk.Entry(new_window, textvariable=entry_var)
    entry.pack()

def open_file_dialog():
    try:
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
        )
        print(f"Selected file: {file_path}")

        if not file_path:
            print("No file selected.")
            return
        
        # Open and read the PDF
        pdf_document = pymupdf.open(file_path)
        text_content = ""
        
        # Extract text from all pages
        for page in pdf_document:
            text_content += page.get_text()
        
        # Clear existing text and insert new content
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, text_content)
        
        # Close the PDF
        pdf_document.close()

    except FileNotFoundError:
        messagebox.showerror("Error", "The selected file was not found.")
    except UnicodeDecodeError:
        messagebox.showerror("Error", "Unable to decode the selected file.")
    except Exception as e:
        messagebox.showerror("Error", f"\nAn unexpected error occurred:\n" + str(e))

master = tk.Tk()
master.geometry("400x200")
master.title("Main window")
text_area = tk.Text(master, wrap='word', height=10)
text_area.pack(pady=10,expand=True, fill='both')


#create menue
menubar = tk.Menu(master)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file_dialog)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)

master.config(menu=menubar)


Label(master, text="This is the main window").pack(pady=20)
Button(master, text="Open new window", command=select_open_selection).pack(side=tk.TOP, pady=10)


master.mainloop()
