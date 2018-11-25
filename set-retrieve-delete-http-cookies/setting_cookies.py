#!"D:\Program Files\Python\Python37-32\python.exe"

# Copyright (C) 2018 Abhijith Sudhakar - All Rights Reserved
# You may use, distribute and modify this code only for educational purpose
# Python 3.7.1
# For any queries feel free to contact abhijith@cyberdude.com

from http import cookies

# create a cookie and assign it a value
c = cookies.SimpleCookie()
c['myCookie'] = "it is my first cookie"

# cookie expiration time represented in milliseconds
c['myCookie']['expires'] = 1 * 1 * 3 * 60 * 60

# print the header, starting with the cookie
print(c)
print("Content-type: text/html\r\n\r\n")
print('''
<html>
<head>
    <title>Setting Cookies | Python CGI Programming</title>
</head>
<body>
<center>
    <h1>Cookie has been Set</h1>
</center>
</body>
</html>
''')
