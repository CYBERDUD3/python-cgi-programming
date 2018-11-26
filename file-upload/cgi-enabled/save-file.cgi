#!"D:\Program Files\Python\Python37-32\python.exe"

# Copyright (C) 2018 Abhijith Sudhakar - All Rights Reserved
# You may use, distribute and modify this code only for educational purpose
# Python 3.7.1
# For any queries feel free to contact abhijith@cyberdude.com

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['myfile']

# Test if the file was uploaded
if fileitem.file:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('tmp/' + fn, 'wb').write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

print("Content-type: text/html\r\n\r\n")
print('''
<html>
<html>
<body>
   <p>%s</p>
</body>
</html>
''' % (message,))
