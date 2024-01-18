#!/opt/homebrew/bin/python3
print("Content-Type: text/html")
print()

import cgi, os, view
from html_sanitizer import Sanitizer
sanitizer = Sanitizer()  # default configuration

form = cgi.FieldStorage()
if 'id' in form:
    pageid = form["id"].value
    article = open('data/'+pageid, 'r').read()
    article = sanitizer.sanitize(article)
    titleid = pageid
    if pageid == 'Samsung':
        titleid = 'Samsung electronics, MX division'
    if pageid == 'Apple':
        titleid = 'Apple, Engineering manager'
    if pageid == 'CEO':
        titleid = 'Startup, CEO'
else:
    titleid = '231217, The beginning of a legend'
    article = '''<br>I'm <strong>world <u>best</u></strong> FullStack Developer
<br>"I CAN DO ANYTHING"'''

print('''<!DOCTYPE html> <!--HyperText Markup Language-->
<html>
<head>
    <title>Hello world!</title>
    <meta charset="utf-8"> <!--meta characterset-->
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1><a href="index.py"><strong>Hello</strong> world!</a></h1>
    <ul> <!--ordered list-->
      {liststr}
    </ul>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="Title"></p>
        <p><textarea rows="4" name="description" placeholder="Description"></textarea></p>
        <p><input type="submit"></p>
    </form>    
</body>
</html>'''.format(title=titleid, description=article, liststr=view.getlist()))