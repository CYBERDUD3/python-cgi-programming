#!"D:\Program Files\Python\Python37-32\python.exe"

# Copyright (C) 2018 Abhijith Sudhakar - All Rights Reserved
# You may use, distribute and modify this code only for educational purpose
# Python 3.7.1
# For any queries feel free to contact abhijith@cyberdude.com

from http import cookies

c = cookies.SimpleCookie()
c['myCookie'] = ''
c['myCookie']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

# print the header, starting with the cookie
print(c)
print("Content-type: text/html\r\n\r\n")

# to verify cookie has been deleted run the retrieving_cookie.py again in the browser
print('''
<html>
<head>
    <title>Setting Cookies | Python CGI Programming</title>
</head>
<body>
<center>
    <h1>Cookie has been Set to Expire</h1>
</center>
</body>
</html>
''')

