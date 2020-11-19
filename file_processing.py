import os

print(os.getcwd())

#os.mkdir('mydir')
#os.rmdir('mydir')

import tempfile
print(tempfile.gettempdir())

print(os.getenv("Path"))

print(os.getenv("MYVAR"))

print(os.listdir())

print(os.path.exists('c:\\Users'))

print(os.path.isdir('c:\\Users'))

print(os.path.getsize('t.txt'))

