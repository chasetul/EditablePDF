Author: 
Chase Tullar

Description: 
This project aims at creating an editable PDF file
in order for the TVA Analysts to insert text and eventually
images.

Use: 
To begin, run the program finalPDF.py by:
'python finalPdf.py'
The program will execute with the base pdf 'base.pdf' and add
layers with each editable section that is included as a new
pdf, resulting now in 'blank7.pdf' as the final file. The code includes functionality to remove 
extra 'blank_#.pdf' files.
Once the program has run, open the last pdf generated
by the programs output, in this case 'blank7.pdf'.
The pdf will have the initial hard-coded fields along
with editable text boxes (and eventually images), and
if the text boxes are changed the changes will save.

Further use:
The script 'finalPdf.py' matches slide 7 on the TVA report.
The script 'slide9.py' matches slide 9.
All further slide script names will match the slide number.

Other info:
A lot of scripts in this repo are for testing different
functionality, like 'flaskTrig.py', which is an attempt
at running a local flask server in order for the user
to click a button inside the generated PDF so they
can visit a local webpage to upload a photo. This is
complicated and probably not the way forward.
