import os
def find_pdf_size(top):
    pdf_size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.lower().endswith(".pdf"):
                pdf_size += os.path.getsize(os.path.join(root, name))
    return pdf_size
top = input()
print("PDF files in {} directory take {} bytes".format(top, find_pdf_size(top)))
