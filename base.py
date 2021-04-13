# data types: BOOL, DEC, BIN, HEX, OBJ

#C001 | 00 | * | 0100, 0101 ;
#example stores C001 as (20, binary)

#find a way to answer if statements with following line

#aleternate examples that still need to be implimented
'''
function to find area of triangle
C005 | 00 | ! | A001 , A002 :
D001 | 01 | * | A001 , A002 ;
D002 | 01 | / | D001 , 0010 ;
0000 | 01 | # | D002, DEC ;

usage: 0000 | 00 | C005 | 0100 , 0010 ;
'''
booltointerror = 'Can not convert numeric value to boolean'

cattr = ('==', '!=', '>=', '>', '<=', '<')
datatypes = ('BOOL','DEC', 'BIN', 'HEX', 'OBJ')

def formatcheck(num):
    s = True
    if type(num) == bool:
        return 'BOOL'
    elif type(num) == int:
        return 'DEC'

    for i in range(len(num)):
        if num[i] not in '10':
            return 'HEX'
    return 'BIN'


def splitline(text):
    idcode, indent, op, ints = text.split(' | ')
    try:
        i1, i2 = ints.split(', ')
    except: 
        i1, i2 = ints.split(',')
    i2, endp = i2.split(' ')
    return idcode, indent, op, i1, i2, endp

def newline(text):
    idcode, indent, op, i1, i2, endp = splitline(text)
    #PRO GAMER MOVE
    globals()[idcode] = line(text)

def DecToBin(num):
    return bin(num).replace("0b", "")
def BinToDec(num):
    return int(num,2)
def HexToDec(num):
    return int(num, 16)
def HexToBin(num):
    x = int(num, 16)
    return bin(x).replace("0b", "")
def DecToHex(num):
    return hex(num)
def BinToHex(num):
    x = BinToDec(num)
    return DecToHex(x)


class System:
    def __repr__(self):
        return '< System 0000 >'

    def output(self,text, format):
        idcode, indent, op, i1, i2, endp = splitline(text)
        try:
            objectformat = eval(i1 + '.format')
            if format == 'DEC':
                if objectformat == 'BIN':
                    output = BinToDec(eval(i1 + '.val'))
                elif objectformat == 'DEC':
                    output = eval(i1 + '.val')
                elif objectformat == 'HEX':
                    output = HexToDec(eval(i1 + '.val'))
                elif objectformat == 'BOOL':
                    x = eval(i1 + '.val')
                    if x == True:
                        output = 1
                    elif x == False:
                        output = 0
            elif format == 'BIN':
                if objectformat == 'BIN':
                    output = (eval(i1 + '.val'))
                elif objectformat == 'DEC':
                    output = DecToBin(eval(i1 + '.val'))
                elif objectformat == 'HEX':
                    output = HexToBin(eval(i1 + '.val'))
                elif objectformat == 'BOOL':
                    raise Exception(booltointerror)
            elif format == 'HEX':
                if objectformat == 'BIN':
                    output = BinToHex(eval(i1 + '.val'))
                elif objectformat == 'DEC':
                    output = DecToHex(eval(i1 + '.val'))
                elif objectformat == 'HEX':
                    output = (eval(i1 + '.val'))
                elif objectformat == 'BOOL':
                    raise Exception(booltointerror)
            elif format == 'BOOL':
                if objectformat == 'BOOL':
                    output = eval(i1 + '.val')
                else:
                    raise Exception(booltointerror)
            else:
                raise Exception('Unknown format under self.format')
            print(output)

        except:
            objectformat = formatcheck(i1)
            #copy and paste try: format but change i1.val to i1
        
tiaga = System()

class line:
    def stateofval(self):
        s = True
        if type(self.val) == bool:
            self.format = 'BOOL'
        else:
            for i in range(len(self.val)):
                if s == True:
                    if self.val[i] in '10':
                        s = True
                    else:
                        s = False
                    self.format = 'BIN'
                else: 
                    if self.val == hex(self.val):
                        self.format = 'HEX'
                    else:
                        self.format = 'DEC'
    def stateofints(self):
        s = True
        if type(self.i1) == bool:
            if self.i1 == True:
                self.i1d = 1
            else:
                self.i1d = 0
        else:
            for i in range(len(self.i1)):
                if s == True:
                    if self.i1[i] in '10':
                        s = True
                    else:
                        s = False
                    try:
                        self.i1d = BinToDec(self.i1)
                    except:
                        pass
                else: 
                    if self.i1 == hex(self.i1):
                        self.i1d = HexToDec(self.i1)
                    else:
                        try:
                            self.i1 = int(self.i1)
                            self.i1d = self.i1
                        except:
                            x = eval(self.i1 + '.format')
                            if x == 'BIN':
                                self.i1d = BinToDec(eval(self.i1 + '.val'))
                            elif x == 'DEC':
                                self.i1d = (eval(self.i1 + '.val'))
                            elif x == 'HEX':
                                self.i1d = HexToDec(eval(self.i1 + '.val'))
                            elif x == 'BOOL':
                                if (eval(self.i1 + '.val')) == True:
                                    self.i1d = 1
                                else:
                                    self.i1d = 0
        s = True
        if type(self.i2) == bool:
            if self.i2 == True:
                self.i2d = 1
            else:
                self.i2d = 0
        else:
            i2s = str(self.i2)
            for i in range(len(i2s)):
                if s == True:
                    if i2s[i] in '10':
                        s = True
                    else:
                        s = False
                    try:
                        self.i2d = BinToDec(self.i2)
                    except:
                        pass
                else: 
                    if self.i2 == hex(self.i2):
                        self.i2d = HexToDec(self.i2)
                    else:
                        try:
                            self.i2 = int(self.i2)
                            self.i2d = self.i2
                        except:
                            x = eval(self.i2 + '.format')
                            if x == 'BIN':
                                self.i2d = BinToDec(eval(self.i2 + '.val'))
                            elif x == 'DEC':
                                self.i2d = (eval(self.i2 + '.val'))
                            elif x == 'HEX':
                                self.i2d = HexToDec(eval(self.i2 + '.val'))
                            elif x == 'BOOL':
                                if (eval(self.i2 + '.val')) == True:
                                    self.i2d = 1
                                else:
                                    self.i2d = 0
                                
                            
        
            
    def __init__(self, text):
        self.idcode, self.indent, self.op, self.ints = text.split(' | ')
        self.text = text
        #leaves room for preference in whitespaces
        try:
            self.i1, self.i2 = self.ints.split(', ')
        except: 
            self.i1, self.i2 = self.ints.split(',')
        self.i2, self.endp = self.i2.split(' ')

        #return to decimal state for calulations
        #add new access to i1 and i2 format functions
        try:
            self.i1d = eval(self.i1 + '.val')
            if self.idcode != '0000':
                self.i2d = eval(self.i2 + '.val')
            else:
                self.i2d = 0
            
        except:
            try:
                #variable that will never be used again
                xtrf = int(self.i2)
                self.stateofints()
            except:
                plh = self.i2
                self.i2 = 1010
                self.stateofints()
                self.i2 = plh
                self.i2d = 0

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
        else:
            #basic operations
            #self.val = eval(self.i1d, self.op, self.i2d) DID NOT WORK LOOK INTO ERROR
            if self.op == '+':
                self.val = self.i1d + self.i2d
            elif self.op == '-':
                self.val = self.i1d - self.i2d
            elif self.op == '*':
                self.val = self.i1d * self.i2d
            elif self.op == '/':
                self.val = self.i1d / self.i2d
            #system bypass
            if self.idcode != '0000':
                self.val = DecToBin(self.val)
                self.stateofval()
            else:
                self.val = 0
                self.format = 'OBJ'

            #triggers system call
            if self.idcode == '0000':
                #print function
                if self.op == '#':
                    tiaga.output(self.text, self.i2)
        
        

newline('C001 | 00 | + | 0100, 0100 ;')
newline('0000 | 00 | # | 0101, DEC ;')



