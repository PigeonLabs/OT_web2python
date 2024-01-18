#!/opt/homebrew/bin/python3
import os, shutil

if os.path.isdir('data') == True:
    shutil.rmtree('data')
shutil.copytree('default', 'data')

#Redirection
print("Location: index.py")
print()