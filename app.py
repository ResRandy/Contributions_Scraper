import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from matcher import findContributions
import tkinter as tk
from tkinter import filedialog, messagebox
import os



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
        
        # clear old containers from previous runs
        for child in results_frame.winfo_children():
            child.destroy()

        # list of text blocks, one per PDF (from matcher.py)
        blocks = findContributions(file_path)

        # create one container per PDF
        for path, block in zip(file_path, blocks):
            filename = ("File Name: " + os.path.basename(path))

            container = tk.Frame(results_frame, bd=5, relief="ridge", bg="#080011")
            container.pack(fill="both", expand=True, padx=10, pady=(0,10))
            

            # header with filename
            title_label = tk.Label(
                container,
                text=filename,
                font=("", 10, "bold"),
                bg="#2F2F42",
                fg="#FFFFFF",
                anchor="w"
            )
            title_label.pack(fill="x")

            # text widget for this PDF’s content
            text_widget = tk.Text(
                container,
                wrap="word",
                bg="#242424",
                font=("", 13),
                fg="#E6E6E6",
                height=5,
                padx=5,
                pady=5
            )
            text_widget.pack(expand=True, fill="both")

            text_widget.insert("1.0", block)
            text_widget.config(state="normal")

            # configure bold font
            bold_font = ("", 13, "bold")
            text_widget.tag_configure("bold", font=bold_font, foreground="#1D9200")

            # configure error font
            error_font = ("", 13, "bold")
            text_widget.tag_configure("error", font=error_font, foreground="#FF7171")

            # list of keywords for bolding
            keywords = ["File Name:", "Zoo/Aquarium detected:", "Methods", "Contribution", "Findings"]

            for word in keywords:
                start = "1.0"
                while True:
                    pos = text_widget.search(word, start, stopindex="end")
                    if not pos:
                        break
                    end = f"{pos}+{len(word)}c"
                    text_widget.tag_add("bold", pos, end)
                    start = end

            # error font for no zoo/aquarium detected
            fail_phrases = ["No Zoo/Aquarium detected",
                            "Seahorses not mentioned",
            ]
            for phrase in fail_phrases:
                start = "1.0"
                while True:
                    pos = text_widget.search(phrase, start, stopindex="end")
                    if not pos:
                        break
                    end = f"{pos}+{len(phrase)}c"
                    text_widget.tag_add("error", pos, end)
                    start = end

            # lock it again
            text_widget.config(state="disabled")

        # scroll bar jumps back to the top after new selection
        master.update_idletasks()
        results_canvas.configure(scrollregion=results_canvas.bbox("all"))
        results_canvas.yview_moveto(0)
        
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
master.configure(bg= "#1C1C25")

top = tk.Frame(master, bg="#2F2F42")
top.pack(fill="x", pady=(0,10))

tk.Label(
    top,
    text="Please select the PDFs you want to scrape for scientific Contributions",
    font=("", 10, "bold"),
    bg="#2F2F42",
    fg="#E6E6E6"
).pack(pady=5)

button_border = tk.Frame(top, bg="#242431", bd=4)
button_border.pack(pady=10)

findFileButton = tk.Button(
    button_border,
    text="open file explorer",
    command=open_file_dialog,
    font=("", 14, "bold"),
    bg="#404050",
    fg="#E6E6E6",
    bd=0  
)
findFileButton.pack()

# scrollable results area
results_canvas = tk.Canvas(master, bg="#1C1C25", highlightthickness=0)
results_canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(master, orient="vertical", command=results_canvas.yview)
scrollbar.pack(side="right", fill="y")

results_canvas.configure(yscrollcommand=scrollbar.set)

results_frame = tk.Frame(results_canvas, bg="#1C1C25")
results_window = results_canvas.create_window((0, 0), window=results_frame, anchor="nw")


def on_frame_configure(event):
    bbox = results_canvas.bbox("all")
    if not bbox:
        return

    x0, y0, x1, y1 = bbox
    content_height = y1 - y0
    canvas_height = results_canvas.winfo_height()

    # if content shorter than canvas, lock scrollregion to canvas height
    if content_height < canvas_height:
        y1 = y0 + canvas_height

    results_canvas.configure(scrollregion=(x0, y0, x1, y1))


results_frame.bind("<Configure>", on_frame_configure)


def on_canvas_configure(event):
    results_canvas.itemconfig(results_window, width=event.width)


results_canvas.bind("<Configure>", on_canvas_configure)


def _on_mousewheel(event):
    results_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


results_canvas.bind_all("<MouseWheel>", _on_mousewheel)



master.mainloop()