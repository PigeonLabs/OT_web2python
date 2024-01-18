#!/opt/homebrew/bin/python3
import cgi
form = cgi.FieldStorage()
pageid = form["pageid"].value
title = form["title"].value
description = form["description"].value

opened_file = open("data/"+pageid,"w")
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()