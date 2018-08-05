# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:57:18 2018

@author: nagae
"""

import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
text = form.getfirst("text")
n = form.getfirst("number")
sequence_list = []

print('Content-type: text/html\nAccess-Control-Allow-Origin: *\n')
print("<p>送信された数字: {}</p>".format("None" if n is None else int(n)))
print("<p>送信されたテキスト: {}</p>".format(text))