import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    dir = os.environ['HOMEPATH']
else:
    dir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(dir,'*')
pattern = "C:"+pattern
for fileName in glob.glob(pattern):
    size = os.path.getsize(fileName)
    if size > 0:
        print(os.path.basename(fileName),"-", size, "bytes")

