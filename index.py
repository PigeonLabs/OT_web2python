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
    '''
    article = article.replace('<', '&lt;') # XSS Security patch
    article = article.replace('>', '&gt;') # XSS Security patch
    '''
    article = sanitizer.sanitize(article)
    titleid = pageid
    update_link = '<a href="edit.py?id={}">edit</a>'.format(pageid)
    default_action = '''
        <form action="process_default.py" method="post">
            <input type="hidden" name="pageid" value="{}">
            <input type="submit" value="default">
        </form>
    '''.format(pageid)
    del_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageid" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageid)
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
    update_link = ''
    default_action = ''
    del_action = ''

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
    {updatelink}
    {default_action}
    {del_action}
    <h2>{title}</h2>
    {description}
    
</body>
</html>'''.format(title=titleid, description=article, liststr=view.getlist(), updatelink=update_link, default_action=default_action, del_action=del_action))