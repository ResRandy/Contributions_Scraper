import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from matcher import findContributions
import tkinter as tk
from tkinter import filedialog, messagebox



def open_file_dialog():
    try:
        file_path = filedialog.askopenfilenames(
            title="Select PDF Files",
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

# center window
width = 900
height = 600

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

master.geometry(f"{width}x{height}+{x}+{y}")
master.title("Scientific Contributions Scraper")
master.configure(bg= "#242431")


top = tk.Frame(master, bg="#2F2F42")
top.pack(fill="x")

tk.Label(
    top,
    text="Please select the PDFs you want to scrape for scientific Contributions",
    font=("", 10, "bold"),
    bg="#2F2F42",
    fg="white"
).pack(pady=5)

findFileButton = tk.Button(
    top,
    text="open file explorer",
    command=open_file_dialog,
    font=("", 14, "bold"),
    bg="#242431",
    fg="white",
    bd=5,
    relief="ridge"
).pack(pady = 10)
#findFileButton.pack(pady=5)

text_area = tk.Text(
    master,
    wrap='word',
    height=10,
    bg = "#242424",
    font=("", 12),
    fg="white"
)
text_area.pack(pady=20, expand=True, fill='both')
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