

#C001 | 00 | * | 0100, 0101 ;
#example stores C001 as (20, binary)

#C004 | 03 | == | C002, C003 :
#alternate example returns true(if statement)

#aleternate examples that still need to be implimented
'''
function to find area of triangle
C005 | 00 | ! | A001 , A002 :
D001 | 01 | * | A001 , A002 ;
D002 | 01 | / | D001 , 0010 ;
0000 | 01 | # | D002, DEC ; DEC tells the console to print result in decimal form other forms are HEX, BIN, and BOOL

usage: 0000 | 00 | C005 | 0100 , 0010 ;
'''

def DecToBin(num):
    return bin(num).replace("0b", "")
def BinToDec(num):
    return int(num,2)

cattr = ('==', '!=', '>=', '>', '<=', '<')

class system:
    def __repr__(self):
        return '< System 0000 >'
    def output(self,text, format):
        if format == 'DEC':
            print()

class line:
    def stateofval(self):
        s = True
        if type(self.val) == bool:
            self.format = 'BOOL'
        else:
            for i in range(len(self.val)):
                if s == True:
                    if self.val[i] in '10':
                        s =  True
                    else:
                        s = False
                    self.format = 'BIN'
                else: 
                    if self.val == hex(self.val):
                        self.format = 'HEX'
                    else:
                        self.format = 'DEC'
            
            
    def __init__(self, text):
        '''
        idcode = ex. C001 namespace/variable name
        indent = ex. 00 replacement for indentation of python language
        op = ex. + operation for binary operation
        '''
        self.idcode, self.indent, self.op, self.ints = text.split(' | ')
        self.text = text
        #leaves room for preference in whitespaces
        try:
            self.i1, self.i2 = self.ints.split(', ')
        except: 
            self.i1, self.i2 = self.ints.split(',')
        self.i2, self.endp = self.i2.split(' ')

        #return to decimal state for calulations
        #may not work: try to use i1 variable to call the class that was found
        try:
            self.i1d = BinToDec(self.i1)
        except:
            i1 = self.i1
            
            self.i1d = i1.val
        try:
            self.i2d = BinToDec(self.i2)
        except:
            i2 = self.i2
            print('w')
            self.i2d = i2.val


        #next step is to create a function definition 
        #also make sure variables can be passed for i1 and i2
        if ':' in self.endp:
            if self.op != '!' and self.op not in cattr:
                if self.indent != '00':
                    print('An error has occured')
                    raise Exception("function definition is either nested or on the wrong indentation")
                else:
                    pass
                    
            else:
                
                #if statement definition 
                #super annoying eval() didn't work so I had to write all the statements out
                #find a way to limit this to one nested statement
                if self.op == '==':
                    if (int(self.i1d) == int(self.i2d)) == True:
                        self.val = True
                    else:
                        self.val = False
                elif self.op == '!=':
                    if (int(self.i1d) != int(self.i2d)) == True:
                        self.val = True
                    else:
                        self.val = False
                elif self.op == '>=':
                    if (int(self.i1d) >= int(self.i2d)) == True:
                        self.val = True
                    else:
                        self.val = False
                elif self.op == '>':
                    if (int(self.i1d) > int(self.i2d)) == True:
                        self.val = True
                    else:
                        self.val = False
                elif self.op == '<=':
                    if (int(self.i1d) <= int(self.i2d)) == True:
                        self.val = True
                    else:
                        self.val = False
                elif self.op == '<':
                    if (int(self.i1d) < int(self.i2d)) == True:
                        self.val = True
                    else:
                        self.val = False
        self.stateofval()
