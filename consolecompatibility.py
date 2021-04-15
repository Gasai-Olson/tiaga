import sys
from base import newline

'''
files will be classified under .tiaga

'''

class file:
    def __init__(self, filename): 
        #define location and file
        self.rows = list()
        self.filename = filename
        #terminal alias malfunction
        self.filename = self.filename[1]
        with open(self.filename, 'r') as fi:
            for row in fi:
                self.rows.append(row)
        for i in range(len(self.rows)):
            self.rows[i] = self.rows[i].rstrip()
            newline(self.rows[i])
#allows for console debugging without getting overloaded with overlapping errors from the python debugger
try:    
    current_file = file(sys.argv) 
except Exception as e:
    print(e)
#to run this more effiecently I recommend creating an alias for the python file using alias tiaga="python3.8 Path/to/file/filerecog.py "
#then use tiaga file.tiaga
