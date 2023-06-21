fileHandler = open('phpstan.neon.dist', 'r+')

line: str
for line in fileHandler:
    # line = line.rstrip()
    # line = line.lstrip()
    line = line.rstrip().lstrip()
    if line.endswith('-'):
        print(line)
        
fileHandler.close()
