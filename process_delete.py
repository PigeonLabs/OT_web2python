#!/opt/homebrew/bin/python3
import cgi, os
form = cgi.FieldStorage()
pageid = form["pageid"].value

os.remove('data/'+pageid)

#Redirection
print("Location: index.py")
print()