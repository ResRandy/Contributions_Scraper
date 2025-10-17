import fitz
import os

def create_txt_file():
    input_path = input("Enter PDF file name (e.g. example.pdf): ")
    output_filename = os.path.splitext(os.path.basename(input_path))[0] + ".txt" # gets the filename and changes extension to .txt


    # get the current folder (where this script is)
    project_folder = os.path.dirname(os.path.abspath(__file__))

    # open the PDF
    pdf_path = os.path.join(project_folder, input_path)
    pdf = fitz.open(pdf_path)

    # extract text
    text = ""
    for page in pdf:
        text += page.get_text()

    # save text file in the same folder
    output_path = os.path.join(project_folder, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print("PDF text saved to:", output_path)

create_txt_file()