'''
Created on Nov 30, 2015

@author: marianbauersachs

'''
from __future__ import with_statement
import traceback
#from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os
import time
import sys
from __builtin__ import len

"""If True, does not execute Monkeyrunner Commands (for Eclipse IDE)"""
debugbool = True

"""Name of file which contains paths"""
pathfilename = "pathfile8sorted.txt"

"""connecting to device"""
print "Waiting for device!"

if not(debugbool): device = MonkeyRunner.waitForConnection()

print "Connected to device!"


"""returns x and y coordinates for touch events"""
def gety(n):
    n = str(n)
    if n in ('1'):
        return 180
    elif n in ('2'):
        return 330
    elif n in ('3'):
        return 470
    elif n in ('4'):
        return 620
        
def getx(n):
    n = str(n)
    if n in ('1'):
        return 440
    elif n in ('2'):
        return 580
    elif n in ('3'):
        return 730
    elif n in ('4'):
        return 880
    
"""deletes content of given file"""
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
    
"""finds string in given character"""
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

"""is comparing two given lists"""
def comp(list1, list2):
    for val in list1:
        if val in list2:
            return True
    return False

"""returns true if given argument is a number"""
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    return False

"""executes movements from point x,y to point 1x,1y"""
def makemoves(tupleX,tupleY,tuple1X,tuple1Y):
    """calculates the difference between the two points"""
    diffy = long(tupleY - tuple1Y)# = -270
    diffx = long(tupleX - tuple1X)# = 0
    """converts to long for a more precise calculation"""
    tupleX = long(tupleX)
    tupleY = long(tupleY)
    tuple1X = long(tuple1X)
    tuple1Y = long(tuple1Y)
    """preparation for logfile"""
    coordinates = "tupleX %d tupleY %d tuple1X %d tuple 1Y %d \n" % (tupleX,tupleY,tuple1X,tuple1Y)
    logdiff = "diffy %d diffx %d \n" % (diffy,diffx)
    f.write(coordinates)
    f.write(logdiff)
    """executes ten movements from point x,y to point 1x,1y"""
    for i in range(1, 11):    
        """
            depending in which direction, the right movement gets executed
            if the difference between y and 1y is negativ and the difference
            between x and 1x is zero, diffy<0 and diffx == 0 is the right argument
        """
        
        if(diffy<0 and diffx == 0):                   
            device.touch(tupleY + abs((diffy/10)) *i, tupleX, MonkeyDevice.MOVE)    
            movestring = "diffy<0 and diffx == 0 \n"
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY + abs((diffy/10)) *i,tupleX)
        elif(diffy>0 and diffx == 0):
            device.touch(tupleY - abs((diffy/10)) *i, tupleX, MonkeyDevice.MOVE)  
            movestring = "diffy>0 and diffx == 0 \n" 
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY - abs((diffy/10)) *i,tupleX)
        elif(diffy == 0 and diffx < 0):                   
            device.touch(tupleY, tupleX + abs((diffx/10)) * i, MonkeyDevice.MOVE)  
            movestring = "diffy == 0 and diffx < 0 \n"   
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY ,tupleX + abs((diffx/10)) * i)  
        elif(diffy == 0 and diffx > 0):
            device.touch(tupleY, tupleX - abs((diffx/10)) * i, MonkeyDevice.MOVE) 
            movestring = "diffy == 0 and diffx > 0 \n"   
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY, tupleX - abs((diffx/10)) * i)
        elif(diffy>0 and diffx < 0):
            device.touch(tupleY - abs((diffy/10)) *i, tupleX + abs((diffx/10)) * i, MonkeyDevice.MOVE) 
            movestring = "diffy>0 and diffx < 0\n"   
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY - abs((diffy/10)) *i, tupleX + abs((diffx/10)) * i)
        elif(diffy>0 and diffx > 0):
            device.touch(tupleY - abs((diffy/10)) *i, tupleX - abs((diffx/10)) * i, MonkeyDevice.MOVE)  
            movestring = "diffy>0 and diffx > 0 \n"    
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY - abs((diffy/10)) *i, tupleX - abs((diffx/10)) * i)
        elif(diffy<0 and diffx < 0):
            device.touch(tupleY + abs((diffy/10)) *i, tupleX + abs((diffx/10)) * i, MonkeyDevice.MOVE)  
            movestring = "diffy>0 and diffx > 0 \n"  
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY + abs((diffy/10)) *i, tupleX + abs((diffx/10)) * i) 
        elif(diffy<0 and diffx > 0):
            device.touch(tupleY + abs((diffy/10)) *i, tupleX - abs((diffx/10)) * i, MonkeyDevice.MOVE) 
            movestring = "diffy>0 and diffx > 0\n"    
            movestring2 = "tupleY %d + tupleX %d \n" %(tupleY + abs((diffy/10)) *i, tupleX - abs((diffx/10)) * i) 
        """is waiting given times between all ten movements"""
        time.sleep(waitbetweenmoves) 
        f.write(movestring2)   
    f.write(movestring)   
    
"""takes a screenshot from current number, and returns it as target number"""                 
def screentarget():
    os.system("screencapture -x -t png -R 926,130,72,72  number.png")
    os.system("tesseract number.png number -psm 6 -l syx quiet")
    with open('number.txt') as f: 
                target = f.read()
    target = int(target)
    return target

"""takes a screenshot of the 4x4 Matrix creates a file"""
def screenshot():
    os.system("screencapture -x -t png -R 795,270,324,324  %s" % (filename))
    
"""convert file to more readable png file for OCR // fuzz is a value to try different till OCR can read it"""
def convert(fuzz):
    os.system("convert %s -trim +repage -fuzz %s -fill white -opaque '#B1EEFC' -fill black +opaque white  -morphology dilate diamond:1 -quiet %s" %(filename,fuzz,outfilename))
    
"""converts png file to txt file"""
def tesser():  
    os.system("tesseract %s %s -psm 6 -l syx quiet" % (outfilename,outfilename))

"""reads the from the OCR created file and returns the content list"""
def readfiles():
    """this is the empty content list"""
    """numbers are surrounded by a 'wall' = 99"""
    content = [[99, 99, 99, 99, 99, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 99, 99, 99, 99, 99]]
    """open file and reading file from tesser, skipping empty lines"""
    with open('%s.txt'%(outfilename)) as f_in:
        contenttemp = (line.rstrip() for line in f_in) 
        contenttemp = list(line for line in contenttemp if line) # Non-blank contenttemp in a list
        f_in.close()

    length =  len(contenttemp)
    print len(contenttemp[0])
    """splitting every element in more elements, creating a 2D Matrix"""
    for i in range(0,length):
        contenttemp[i] = contenttemp[i].split()
    """raising TypeError if length of contenttemp is larger then 4, if OCR is successful, no Error here"""
    for i in range(0,length):
        if(len(contenttemp[i])>4):
            raise TypeError

    """integrating contenttemp to the already created content list"""
    for index in range(4):
        for innerindex in range(4):
            content[index+1][innerindex+1] = contenttemp[index][innerindex]   
     
    """converting content to int"""
    for index in range(1,5):
        for innerindex in range (1,5):
                content[index][innerindex] = int(content[index][innerindex])
    """raise TypeError if a 0 exists in content, if OCR is successful, no Error here"""
    for x in range(1,5):
                for y in range (1,5):
                    if(content[x][y] == 0):
                        raise TypeError
    
    """raises TypeError if 'border' is not 99, if OCR is successful, no Error here"""
    for y in range (0,5):
        if(content[0][y] != 99):
            print"true"
            raise TypeError
    for y in range (0,6):
        if(content[5][y] != 99):
            print"true"
            raise TypeError
    for x in range(0,6):
        if(content[x][5] != 99):
            print"true"
            raise TypeError
    for x in range(0,6):
        if(content[x][5] != 99):
            print"true"
            raise TypeError
    return content

"""reads given pathfile in a list"""
def readpathfile():
    with open(pathfilename) as f:
        possiblepaths = f.readlines()
    length = len(possiblepaths)
    
    """splitting strings in sublists and converting to int"""
    for i in range(length):
        possiblepaths[i] = possiblepaths[i].split()
    for i in range(length):
        for j in range(len(possiblepaths[i])):
                possiblepaths[i][j] = int(possiblepaths[i][j])
    return possiblepaths,length
    
"""prededfined tuples"""

tupleX = 0
tupleY = 0
tuple1X  = 0
tuple1Y = 0
tuple2X = 0
tuple2Y = 0
tuple3X = 0
tuple3Y = 0
tuple4X = 0
tuple4Y = 0
tuple5X = 0
tuple5Y = 0
tuple6X = 0
tuple6Y = 0
tuple7X = 0
tuple7Y = 0
tuple8X = 0
tuple8Y = 0
tuple9X = 0
tuple9Y = 0
tuple10X = 0
tuple10Y = 0

"""creates times for IDE"""
if (debugbool):
    screenendtime = time.time()
    screenstarttime = time.time()
    tesserendtime = time.time()
    tesserstarttime =time.time()


"""predefining old and new content lists"""
oldcontent = [[99, 99, 99, 99, 99, 99],
        [99, 1, 1, 1, 1, 99],
        [99, 0, 0, 0, 1, 99],
        [99, 0, 0, 0, 0, 99],
        [99, 0, 0, 0, 0, 99],
        [99, 99, 99, 99, 99, 99]]
content = [[99, 99, 99, 99, 99, 99],
        [99, 1, 1, 1, 1, 99],
        [99, 0, 0, 0, 1, 99],
        [99, 0, 0, 0, 0, 99],
        [99, 0, 0, 0, 0, 99],
        [99, 99, 99, 99, 99, 99]]

"""
    checking given content list for target, using pathlist 
    to try out everyfile till target is hit
"""
def checktarget(possiblepaths,length,target,content):
    """for loop starts, length is length of possiblepath or possible paths beeing tried"""
    for i in range(length):
        """temp is for every new line zero"""
        temp = 0
        """defining how many possible tuples are in one line"""
        skip = [2]
        if(len(possiblepaths[i]) == 4):
            skip = [2]
            l = 4
        if(len(possiblepaths[i]) == 6):
            skip = [2,4]
            l = 6
        if(len(possiblepaths[i]) == 8):
            skip = [2,4,6]
            l = 8
        if(len(possiblepaths[i]) == 10):
            skip = [2,4,6,8]
            l = 10
        if(len(possiblepaths[i]) == 12):
            skip = [2,4,6,8,10]
            l = 12
        if(len(possiblepaths[i]) == 14):
            skip = [2,4,6,8,10,12]
            l = 14
        if(len(possiblepaths[i]) == 16):
            skip = [2,4,6,8,10,12,14]
            l = 16
        """
            temp starts with the first x,y number in the line, e.g. content[1][1] = number in 4x4 Matrix = 4
            first line in pathfile could look like this '1 1 1 2' = look for content[1][1] and content[1][2]
        """
        temp = content[possiblepaths[i][0]][possiblepaths[i][1]]
        for j in skip:
            """temp is adding second tuple in line in pathfile, like temp + content[1][2], depending how long line in pathfile is"""
            temp = temp  + content[possiblepaths[i][j]][possiblepaths[i][j+1]]
        if (temp == target):    
            """if length of line in pathfile is 4, it gets and returns the coordinates for x,y and x1 and y1 and the turns needed"""          
            if(l == 4):
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X =  getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                turns = 2
                
                
                print temp
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'turns':turns }
                
            if(l == 6):
                
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X =  getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                tuple2X =  getx(possiblepaths[i][4])
                tuple2Y = gety(possiblepaths[i][5])
                turns = 3
                
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'x2':tuple2X,'y2':tuple2Y, 'turns':turns }
            if(l == 8):
                
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X =  getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                tuple2X =  getx(possiblepaths[i][4])
                tuple2Y = gety(possiblepaths[i][5])
                tuple3X =  getx(possiblepaths[i][6])
                tuple3Y = gety(possiblepaths[i][7])
                turns = 4
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'x2':tuple2X,'y2':tuple2Y,'x3':tuple3X,'y3':tuple3Y, 'turns':turns }
            if(l == 10):
                
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X =  getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                tuple2X =  getx(possiblepaths[i][4])
                tuple2Y = gety(possiblepaths[i][5])
                tuple3X =  getx(possiblepaths[i][6])
                tuple3Y = gety(possiblepaths[i][7])
                tuple4X =  getx(possiblepaths[i][8])
                tuple4Y = gety(possiblepaths[i][9])
                turns = 5
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'x2':tuple2X,'y2':tuple2Y,'x3':tuple3X,'y3':tuple3Y,'x4':tuple4X,'y4':tuple4Y, 'turns':turns }
            if(l == 12):
                
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X =  getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                tuple2X =  getx(possiblepaths[i][4])
                tuple2Y = gety(possiblepaths[i][5])
                tuple3X =  getx(possiblepaths[i][6])
                tuple3Y = gety(possiblepaths[i][7])
                tuple4X =  getx(possiblepaths[i][8])
                tuple4Y = gety(possiblepaths[i][9])
                tuple5X = getx(possiblepaths[i][10])
                tuple5Y = gety(possiblepaths[i][11])
                turns = 6
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'x2':tuple2X,'y2':tuple2Y,'x3':tuple3X,'y3':tuple3Y,'x4':tuple4X,'y4':tuple4Y,\
                         'x5':tuple5X,'y5':tuple5Y,'turns':turns }
            if(l == 14):
                
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X =  getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                tuple2X =  getx(possiblepaths[i][4])
                tuple2Y = gety(possiblepaths[i][5])
                tuple3X =  getx(possiblepaths[i][6])
                tuple3Y = gety(possiblepaths[i][7])
                tuple4X =  getx(possiblepaths[i][8])
                tuple4Y = gety(possiblepaths[i][9])
                tuple5X = getx(possiblepaths[i][10])
                tuple5Y = gety(possiblepaths[i][11])
                tuple6X = getx(possiblepaths[i][12])
                tuple6Y = gety(possiblepaths[i][13])
                turns = 7
                
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'x2':tuple2X,'y2':tuple2Y,'x3':tuple3X,'y3':tuple3Y,'x4':tuple4X,'y4':tuple4Y,\
                         'x5':tuple5X,'y5':tuple5Y,'x6':tuple6X,'y6':tuple6Y,'turns':turns }
            if(l == 16):
                
                tupleX = getx(possiblepaths[i][0])
                tupleY = gety(possiblepaths[i][1])
                tuple1X = getx(possiblepaths[i][2])
                tuple1Y = gety(possiblepaths[i][3])
                tuple2X = getx(possiblepaths[i][4])
                tuple2Y = gety(possiblepaths[i][5])
                tuple3X = getx(possiblepaths[i][6])
                tuple3Y = gety(possiblepaths[i][7])
                tuple4X = getx(possiblepaths[i][8])
                tuple4Y = gety(possiblepaths[i][9])
                tuple5X = getx(possiblepaths[i][10])
                tuple5Y = gety(possiblepaths[i][11])
                tuple6X = getx(possiblepaths[i][12])
                tuple6Y = gety(possiblepaths[i][13])
                tuple7X = getx(possiblepaths[i][14])
                tuple7Y = gety(possiblepaths[i][15])
                turns = 8
                return {'x':tupleX, 'y':tupleY ,'x1':tuple1X,'y1':tuple1Y,'x2':tuple2X,'y2':tuple2Y,'x3':tuple3X,'y3':tuple3Y,'x4':tuple4X,'y4':tuple4Y,\
                     'x5':tuple5X,'y5':tuple5Y,'x6':tuple6X,'y6':tuple6Y,'x7':tuple7X,'y7':tuple7Y,'turns':turns }

"""before loop it is reading the pathfile and saves time"""
print "reading path file"
readfiletimestart = time.time()
possiblepaths,pathfilelength = readpathfile()
readfiletimeend = time.time()
print "pathfile read"

"""asking for user input which number to start with"""
firstnumber = int(raw_input('which number to start with'))
lastnumber = 101
rangetuple = range(firstnumber,lastnumber)
"""starting for loop for execution"""
for i in rangetuple:
    starttime = time.time()
    filename = "%d.png" % i
    outfilename = "%dout.png" % i

    print "screencapture and OCR are executed"

    screenstarttime = time.time()
    """different values for convert screenshot in a list"""
    fuzzed = ["15%","20%","25%","35%","40%"]
    if not(debugbool):
        """taking screenshot of 4x4 Matrix"""
        screenshot()
        for fuzz in fuzzed:
            try:
                """trying different fuzz values until no execption is thrown"""
                if not (debugbool):
                    convert(fuzz)
                if not(debugbool):
                    tesser()
                content = readfiles()
    
            except Exception,e:
                
                
                e = sys.exc_info()[0]
                continue
            break
    """reading files into content list"""
    if(debugbool):content = readfiles()
    
    """if oldcontent is equal to new content, function is retrying to read 4x4 Matrix"""
    if not (debugbool):
        if (oldcontent[1][1] == content[1][1] and oldcontent[2][2] == content[2][2] and oldcontent[3][3] == content[3][3] and oldcontent[4][4] == content[4][4]) : 
            print "last check didnt work. Try again...."
            """sending touch events to pause and continue the game"""
            device.touch(65, 69, 'DOWN_AND_UP')
            time.sleep(1.0)
            device.touch(400, 614, 'DOWN_AND_UP')
            time.sleep(1.5)
            """retrying to read 4x4 Matrix for all fuzz values"""
            screenshot()
            for fuzz in fuzzed:
                try:
                    
                    if not (debugbool):
                        convert(fuzz)
                    if not(debugbool):
                        tesser()
                    content = readfiles()
                    
        
                except Exception,e:
                    
                    e = sys.exc_info()[0]
                    continue
                break
    screenendtime = time.time() 
    """assign new content to old to check if it worked or not"""
    oldcontent[1][1] = content[1][1]
    oldcontent[2][2] = content[2][2]
    oldcontent[3][3] = content[3][3]
    oldcontent[4][4] = content[4][4]
    """checking which number is the target number"""
    if not (debugbool):target = screentarget()
    turns=1
    print "Checking Number %d" %(target)
    calctime = time.time()   
    """executing function to find path"""
    result = checktarget(possiblepaths,pathfilelength,target,content)
    
    """assigning tuples for execution regarding the number of turns"""
    turns = result['turns']
    tupleX = result['x']
    tupleY = result['y']
    tuple1X = result['x1']
    tuple1Y = result['y1']
    if (turns == 3 ):
        tuple2X = result['x2']
        tuple2Y = result['y2']
    elif (turns == 4):
        tuple2X = result['x2']
        tuple2Y = result['y2']
        tuple3X = result['x3']
        tuple3Y = result['y3']
    elif (turns == 5):
        tuple2X = result['x2']
        tuple2Y = result['y2']
        tuple3X = result['x3']
        tuple3Y = result['y3']
        tuple4X = result['x4']
        tuple4Y = result['y4']
    elif (turns == 6):
        tuple2X = result['x2']
        tuple2Y = result['y2']
        tuple3X = result['x3']
        tuple3Y = result['y3']
        tuple4X = result['x4']
        tuple4Y = result['y4']
        tuple5X = result['x5']
        tuple5Y = result['y5']
    elif (turns == 7):
        tuple2X = result['x2']
        tuple2Y = result['y2']
        tuple3X = result['x3']
        tuple3Y = result['y3']
        tuple4X = result['x4']
        tuple4Y = result['y4']
        tuple5X = result['x5']
        tuple5Y = result['y5']
        tuple6X = result['x6']
        tuple6Y = result['y6']
    elif (turns == 8):
        tuple2X = result['x2']
        tuple2Y = result['y2']
        tuple3X = result['x3']
        tuple3Y = result['y3']
        tuple4X = result['x4']
        tuple4Y = result['y4']
        tuple5X = result['x5']
        tuple5Y = result['y5']
        tuple6X = result['x6']
        tuple6Y = result['y6']
        tuple7X = result['x7']
        tuple7Y = result['y7']
    
    calcendtime = time.time()
    movementstarttime = time.time()
    if not(debugbool): 
        """open logfile and deleting content"""
        f = open('log.txt', 'w')
        deleteContent(f)
        waitbetweenmoves = 0.03
        """touch.Down event for first tuple"""
        device.touch(tupleY, tupleX, MonkeyDevice.DOWN)  
        """executing movements according to number of turns""" 
        if(turns == 11):                                                 
            print "making eleven moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            makemoves(tuple4X,tuple4Y,tuple5X,tuple5Y)
            makemoves(tuple5X,tuple5Y,tuple6X,tuple6Y)
            makemoves(tuple7X,tuple7Y,tuple8X,tuple8Y)
            makemoves(tuple7X,tuple7Y,tuple8X,tuple8Y)
            makemoves(tuple8X,tuple8Y,tuple9X,tuple9Y)
            makemoves(tuple9X,tuple9Y,tuple10X,tuple10Y)
            device.touch(tuple10Y, tuple10X, MonkeyDevice.UP)  
        elif(turns == 10):                                                 
            print "making ten moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            makemoves(tuple4X,tuple4Y,tuple5X,tuple5Y)
            makemoves(tuple5X,tuple5Y,tuple6X,tuple6Y)
            makemoves(tuple7X,tuple7Y,tuple8X,tuple8Y)
            makemoves(tuple7X,tuple7Y,tuple8X,tuple8Y)
            makemoves(tuple8X,tuple8Y,tuple9X,tuple9Y)
            device.touch(tuple9Y, tuple9X, MonkeyDevice.UP)  
        elif(turns == 9):                                                 
            print "making nine moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            makemoves(tuple4X,tuple4Y,tuple5X,tuple5Y)
            makemoves(tuple5X,tuple5Y,tuple6X,tuple6Y)
            makemoves(tuple7X,tuple7Y,tuple8X,tuple8Y)
            device.touch(tuple8Y, tuple8X, MonkeyDevice.UP)  
        elif(turns == 8):                                                 
            print "making eight moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            makemoves(tuple4X,tuple4Y,tuple5X,tuple5Y)
            makemoves(tuple5X,tuple5Y,tuple6X,tuple6Y)
            makemoves(tuple6X,tuple6Y,tuple7X,tuple7Y)
            device.touch(tuple7Y, tuple7X, MonkeyDevice.UP)  
        elif(turns == 7):                                                 
            print "making seven moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            makemoves(tuple4X,tuple4Y,tuple5X,tuple5Y)
            makemoves(tuple5X,tuple5Y,tuple6X,tuple6Y)
            device.touch(tuple6Y, tuple6X, MonkeyDevice.UP)  
        elif(turns == 6):                                                 
            print "making six moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            makemoves(tuple4X,tuple4Y,tuple5X,tuple5Y)
            device.touch(tuple5Y, tuple5X, MonkeyDevice.UP)        
        elif(turns == 5):                                                 
            print "making five moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            makemoves(tuple3X,tuple3Y,tuple4X,tuple4Y)
            device.touch(tuple4Y, tuple4X, MonkeyDevice.UP)        
        elif(turns == 4):    
            print "making four moves"                                                 
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            makemoves(tuple2X,tuple2Y,tuple3X,tuple3Y)
            device.touch(tuple3Y, tuple3X, MonkeyDevice.UP)         
        elif(turns == 3):  
            print "making three moves"       
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            makemoves(tuple1X,tuple1Y,tuple2X,tuple2Y)
            device.touch(tuple2Y, tuple2X, MonkeyDevice.UP)                                                 
        elif(turns == 2):  
            print "making two moves"
            makemoves(tupleX,tupleY,tuple1X,tuple1Y)
            device.touch(tuple1Y, tuple1X, MonkeyDevice.UP)  
        
    movementendtime = time.time()                                                               
    endtime = time.time()
    
    """printing time for single events"""
    print "time for screencapture in miliseconds (inlcuding failure)"
    print (screenendtime-screenstarttime)*1000
    print "time to execute movements in miliseconds"
    print (movementendtime-movementstarttime)*1000
    print "calc time needed in miliseconds"
    print (calcendtime-calctime)*1000
    
    """waiting after execution of movements"""
    print "waiting..."
    time.sleep(0.9)
    
    """checking when number are appereard to continue loop"""
    filenameproceed = "%dproceed.png" % target
    outfilenameproceed = "%dproceed.png" % target
    if not(debugbool):
        print "waiting for numbers to appear..."
        targetnumber = ""
        
        """loop breaks if OCR returns a number"""
        while not(is_number(targetnumber) ):
            os.system("screencapture -x -t png -R 795,287,54,37  %s" % (filenameproceed)) 
            os.system("convert %s -trim +repage -fuzz %s -fill white -fill black +opaque white -quiet %s" %(filenameproceed,"60%",filenameproceed))
            os.system("tesseract %s %s -psm 6 -l syx quiet" % (filenameproceed,outfilenameproceed))
            with open('%dproceed.png.txt'%(target)) as f: 
                targetnumber = f.read()
                
    """waiting for security"""         
    time.sleep(0.8)
    finaltime = time.time()
    print "time for total move in seconds"
    print (finaltime-starttime)
    if(target == 99):
        print "reached 100. Congrats!"
        break
