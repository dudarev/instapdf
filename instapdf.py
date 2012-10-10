"""
python instapdf.pdf

Takes first 6 jpg images in the directory and puts them into 10x15 cm canvas in PDF.
"""

# based on
# http://code.activestate.com/recipes/576717-pdf-a-directory-of-images-using-reportlab/

import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


i_max = 1
j_max = 2

image_width = 4.25 * cm
image_height = 4.25 * cm

padding_x = 0.5 * cm
padding_y = 0.5 * cm

x0 = 0.5 * cm
y0 = 0.75 * cm

page_width = 10 * cm
page_height = 15 * cm


def pdfDirectory(imageDirectory, outputPDFName):
    dirim = str(imageDirectory)
    output = str(outputPDFName)
    c = canvas.Canvas(output, pagesize=(page_width, page_height))
    
    i = 0
    j = 0

    try:
        for root, dirs, files in os.walk(dirim):
            for name in files:
                lname = name.lower()
                if lname.endswith(".jpg") or lname.endswith(".gif") or lname.endswith(".png"):

                    filepath = os.path.join(root, name)
                    x = x0 + i * (image_width + padding_x)
                    y = y0 + j * (image_height + padding_y)
                    c.drawImage(filepath, x, y, image_width, image_height)

                    if i < i_max:
                        i += 1
                    else:
                        i = 0
                        if j < j_max:
                            j += 1
                        else:
                            break

            c.save()
        print "PDF of Image directory created"
    except:
        print "Failed creating PDF"

if __name__ == '__main__':
    pdfDirectory('.', 'out.pdf')
