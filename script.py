import os
import img2pdf

with open("imgpdf.pdf","wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir("../img_to_pdf") if i.endswith('.jpg')]))