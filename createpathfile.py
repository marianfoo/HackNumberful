'''
Created on Nov 30, 2015

@author: marianbauersachs
'''
import time
import numpy as np

"""
    creating a pathfile for 8 movements
    this algorithm is given a content file which it cant find a path
    so it checks every path possible for 8 turns in total
    it is writing every path in a file
"""


target = 97
filename = "%d.png" % 97
outfilename = "%dout.png" % 97
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
f = open('pathfile5.txt', 'w')
deleteContent(f)

"""these function check if a coordinate is redundant"""
def checkreturn2(x,y,x2,y2):
    if(x==x2 and y==y2):
        return True
def checkreturn3(x,y,x1,y1,x2,y2,x3,y3):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x1==x3 and y1==y3)):
        return True
def checkreturn4(x,y,x1,y1,x2,y2,x3,y3,x4,y4):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4) \
       or(x2==x4 and y2==y4)):
        return True
def checkreturn5(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4)or(x==x5 and y==y5) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4)or(x1==x5 and y1==y5) \
       or(x2==x4 and y2==y4)or(x2==x5 and y2==y5) \
       or(x3==x5 and y3==y5)):
        return True
def checkreturn6(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4)or(x==x5 and y==y5)or(x==x6 and y==y6) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4)or(x1==x5 and y1==y5)or(x1==x6 and y1==y6) \
       or(x2==x4 and y2==y4)or(x2==x5 and y2==y5)or(x2==x6 and y2==y6) \
       or(x3==x5 and y3==y5)or(x3==x6 and y3==y6) \
       or(x4==x6 and y4==y6)):
        return True
def checkreturn7(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4)or(x==x5 and y==y5)or(x==x6 and y==y6)or(x==x7 and y==y7) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4)or(x1==x5 and y1==y5)or(x1==x6 and y1==y6)or(x1==x7 and y1==y7) \
       or(x2==x4 and y2==y4)or(x2==x5 and y2==y5)or(x2==x6 and y2==y6)or(x2==x7 and y2==y7) \
       or(x3==x5 and y3==y5)or(x3==x6 and y3==y6)or(x3==x7 and y3==y7) \
       or(x4==x6 and y4==y6)or(x4==x7 and y4==y7) \
       or(x5==x7 and y5==y7)):
        return True
def checkreturn8(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4)or(x==x5 and y==y5)or(x==x6 and y==y6)or(x==x7 and y==y7)or(x==x8 and y==y8) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4)or(x1==x5 and y1==y5)or(x1==x6 and y1==y6)or(x1==x7 and y1==y7)or(x1==x8 and y1==y8) \
       or(x2==x4 and y2==y4)or(x2==x5 and y2==y5)or(x2==x6 and y2==y6)or(x2==x7 and y2==y7)or(x2==x8 and y2==y8) \
       or(x3==x5 and y3==y5)or(x3==x6 and y3==y6)or(x3==x7 and y3==y7)or(x3==x8 and y3==y8) \
       or(x4==x6 and y4==y6)or(x4==x7 and y4==y7)or(x4==x8 and y4==y8) \
       or(x5==x7 and y5==y7)or(x5==x8 and y5==y8) \
       or(x6==x8 and y6==y8)):
        return True
def checkreturn9(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4)or(x==x5 and y==y5)or(x==x6 and y==y6)or(x==x7 and y==y7)or(x==x8 and y==y8)or(x==x9 and y==y9) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4)or(x1==x5 and y1==y5)or(x1==x6 and y1==y6)or(x1==x7 and y1==y7)or(x1==x8 and y1==y8)or(x1==x9 and y1==y9) \
       or(x2==x4 and y2==y4)or(x2==x5 and y2==y5)or(x2==x6 and y2==y6)or(x2==x7 and y2==y7)or(x2==x8 and y2==y8)or(x2==x9 and y2==y9) \
       or(x3==x5 and y3==y5)or(x3==x6 and y3==y6)or(x3==x7 and y3==y7)or(x3==x8 and y3==y8)or(x3==x9 and y3==y9) \
       or(x4==x6 and y4==y6)or(x4==x7 and y4==y7)or(x4==x8 and y4==y8)or(x4==x9 and y4==y9) \
       or(x5==x7 and y5==y7)or(x5==x8 and y5==y8)or(x5==x9 and y5==y9) \
       or(x6==x8 and y6==y8)or(x6==x9 and y6==y9) \
       or(x7==x9 and y7==y9)):
        return True
def checkreturn10(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10):
    if((x==x2 and y==y2)or(x==x3 and y==y3)or(x==x4 and y==y4)or(x==x5 and y==y5)or(x==x6 and y==y6)or(x==x7 and y==y7)or(x==x8 and y==y8)or(x==x9 and y==y9)or(x==x10 and y==y10) \
       or(x1==x3 and y1==y3)or(x1==x4 and y1==y4)or(x1==x5 and y1==y5)or(x1==x6 and y1==y6)or(x1==x7 and y1==y7)or(x1==x8 and y1==y8)or(x1==x9 and y1==y9)or(x1==x10 and y1==y10) \
       or(x2==x4 and y2==y4)or(x2==x5 and y2==y5)or(x2==x6 and y2==y6)or(x2==x7 and y2==y7)or(x2==x8 and y2==y8)or(x2==x9 and y2==y9)or(x2==x10 and y2==y10) \
       or(x3==x5 and y3==y5)or(x3==x6 and y3==y6)or(x3==x7 and y3==y7)or(x3==x8 and y3==y8)or(x3==x9 and y3==y9)or(x3==x10 and y3==y10) \
       or(x4==x6 and y4==y6)or(x4==x7 and y4==y7)or(x4==x8 and y4==y8)or(x4==x9 and y4==y9)or(x4==x10 and y4==y10) \
       or(x5==x7 and y5==y7)or(x5==x8 and y5==y8)or(x5==x9 and y5==y9)or(x5==x10 and y5==y10) \
       or(x6==x8 and y6==y8)or(x6==x9 and y6==y9)or(x6==x10 and y6==y10) \
       or(x7==x9 and y7==y9)or(x7==x10 and y7==y10)
       or(x8==x10 and y8==y10)):
        return True
    
"""this is the parameter for 'wall'"""
wall = 99

"""this functions return the values around the current position in the matrix"""
def returnCordX(i,x):
    x = x
    possiblex = [x-1  ,x-1  ,x-1  ,x  ,x+1  ,x+1  ,x+1 ,x]
    return possiblex[i]
def returnCordY(i,y):
    y = y
    possibley = [y-1  ,y  ,y+1  ,y+1  ,y+1  ,y  ,y-1  ,y-1]
    return possibley[i]
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
def readfiles():
    content = [[99, 99, 99, 99, 99, 99],
    [99, 1, 1, 1, 1, 99],
    [99, 0, 0, 0, 1, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 99, 99, 99, 99, 99]]
    #open file and reading file from tesser, skipping empty lines
    with open('%s.txt'%(outfilename)) as f_in:
        contenttemp = (line.rstrip() for line in f_in) 
        contenttemp = list(line for line in contenttemp if line) # Non-blank contenttemp in a list
        f_in.close()
#         with open('%s.txt'%(outfilename)) as f: 
#             contenttemp = f.readlines()
    #splitting every element in more elements, creating a 2D Matrix
            #deleting if there is a single zero standing somewhere
    length =  len(contenttemp)
    for i in range(0,length):
        contenttemp[i] = contenttemp[i].split()
    for index in range(4):
        for innerindex in range(4):
            content[index+1][innerindex+1] = contenttemp[index][innerindex]

    #converting everything to int
    for index in range(1,5):
        for innerindex in range (1,5):
                content[index][innerindex] = int(content[index][innerindex])
    for x in range(1,5):
                for y in range (1,5):
                    if(content[x][y] == 0):
                        raise TypeError
                    


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
content = [[99, 99, 99, 99, 99, 99],
    [99, 1, 1, 1, 1, 99],
    [99, 0, 0, 0, 1, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 0, 0, 0, 0, 99],
    [99, 99, 99, 99, 99, 99]]

def findeigthpath(minimumturns):
    turns = 1
    tupleX = 0
    tupleY = 0
    tuple1X =  0
    tuple1Y = 0
    tuple2X =  0
    tuple2Y = 0
    tuple3X =  0
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
    
    """starts on x 1 till x 4"""
    for x in range(1,5):
            print x
            """starts on y 1 till y 4"""
            for y in range (1,5):
                """check every number around the current position"""
                for i in range(8):#x[1]y[1]
                    #[1][1]
                    current1 = content[x][y] # is 1
                    
                    x1,y1 = returnCordX(i,x),returnCordY(i,y) #[1][2]
                    test1 = content[x1][y1] # is 1
                    
                    if(test1 != wall): #x[2]y[2]
                        """writes current path in pathfile"""
                        path = "%d %d %d %d \n" % (x,y,x1,y1)
                        f.write(path)
                        currentturns = 2
                        if((current1 + test1 == target) and (currentturns >= minimumturns)): #no, its 1
                            print "found first path content[%d][%d] and content[%d][%d]" % (x,y,x1,y1)
                            
                            print target
                            tupleX = getx(x)
                            tupleY = gety(y)
                            tuple1X =  getx(x1)
                            tuple1Y = gety(y1)
                            turns = 2
                            #print "content[%d][%d] and content[%d][%d]" % (tupleY,tupleX,tuple1Y,tuple1X)
                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                        
                        else:
                            result1 = current1 + test1 # is 2
                            for i in range(8):
                                x2,y2 = returnCordX(i,x1),returnCordY(i,y1) #[1][3]
                                test2 = content[x2][y2] # is 1
                                if not(checkreturn2(x,y,x2,y2)):
                                    if(test2 != wall):
                                        currentturns = 3
                                        path = "%d %d %d %d %d %d \n" % (x,y,x1,y1,x2,y2)
                                        f.write(path)
                                        if(result1 + test2 == target and (currentturns >= minimumturns)):
                                            print "found second path content[%d][%d] and content[%d][%d] and content[%d][%d]" % (x,y,x1,y1,x2,y2)
                                            turns = 3
                                            tupleX = getx(x)
                                            tupleY = gety(y)
                                            tuple1X =  getx(x1)
                                            tuple1Y = gety(y1)
                                            tuple2X =  getx(x2)
                                            tuple2Y = gety(y2)
                                            #print "content[%d][%d] and content[%d][%d] and content[%d][%d]" % (tupleY,tupleX,tuple1Y,tuple1X,tuple2X,tuple2Y)
                                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                                        else:
                                            result2 = result1 + test2 # is 3
                                            for i in range(8):
                                                x3,y3 = returnCordX(i,x2),returnCordY(i,y2) #[1][4]
                                                test3 = content[x3][y3] # is 1
                                                if not(checkreturn3(x,y,x1,y1,x2,y2,x3,y3)):
                                                    if(test3 != wall):
                                                        path = "%d %d %d %d %d %d %d %d \n" % (x,y,x1,y1,x2,y2,x3,y3)
                                                        f.write(path)
                                                        currentturns = 4
                                                        if(result2 + test3 == target and (currentturns >= minimumturns)):
                                                            print "found third path content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d]" % (x,y,x1,y1,x2,y2,x3,y3)
                                                            turns = 4
                                                            tupleX = getx(x)
                                                            tupleY = gety(y)
                                                            tuple1X =  getx(x1)
                                                            tuple1Y = gety(y1)
                                                            tuple2X =  getx(x2)
                                                            tuple2Y = gety(y2)
                                                            tuple3X =  getx(x3)
                                                            tuple3Y = gety(y3)
                                                            
                                                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                                                        else:
                                                            result3 = result2 + test3 # is 4
                                                            for i in range(8):
                                                                current4 = content[x3][y3] #is 1
                                                                x4,y4 = returnCordX(i,x3),returnCordY(i,y3) #[2][4]
                                                                test4 = content[x4][y4] # is 1
                                                                if not(checkreturn4(x,y,x1,y1,x2,y2,x3,y3,x4,y4)):
                                                                    if(test4 != wall):
                                                                        currentturns = 5
                                                                        path = "%d %d %d %d %d %d %d %d %d %d \n" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4)
                                                                        f.write(path)
                                                                        if(result3 + test4 == target and (currentturns >= minimumturns)):
                                                                            print "found fourth path content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d]" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4)
                                                                            turns = 5
                                                                            tupleX = getx(x)
                                                                            tupleY = gety(y)
                                                                            tuple1X =  getx(x1)
                                                                            tuple1Y = gety(y1)
                                                                            tuple2X =  getx(x2)
                                                                            tuple2Y = gety(y2)
                                                                            tuple3X =  getx(x3)
                                                                            tuple3Y = gety(y3)
                                                                            tuple4X =  getx(x4)
                                                                            tuple4Y = gety(y4)
                                                                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                                                                        else:
                                                                            result4 = result3 + test4 # is 4
                                                                            for i in range(8):
                                                                                current5 = content[x4][y4] #is 1
                                                                                x5,y5 = returnCordX(i,x4),returnCordY(i,y4) #[2][4]
                                                                                test5 = content[x5][y5] # is 1
                                                                                if not(checkreturn5(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)):
                                                                                    if(test5 != wall):
                                                                                        currentturns = 6
                                                                                        path = "%d %d %d %d %d %d %d %d %d %d %d %d \n" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
                                                                                        f.write(path)
                                                                                        if(result4 + test5 == target and (currentturns >= minimumturns)):
                                                                                            print "found fith path content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d]" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
                                                                                            turns = 6
                                                                                            tupleX = getx(x)
                                                                                            tupleY = gety(y)
                                                                                            tuple1X =  getx(x1)
                                                                                            tuple1Y = gety(y1)
                                                                                            tuple2X =  getx(x2)
                                                                                            tuple2Y = gety(y2)
                                                                                            tuple3X =  getx(x3)
                                                                                            tuple3Y = gety(y3)
                                                                                            tuple4X =  getx(x4)
                                                                                            tuple4Y = gety(y4)
                                                                                            tuple5X = getx(x5)
                                                                                            tuple5Y = gety(y5)
                                                                                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                                                                                        else:
                                                                                            result5 = result4 + test5 # is 4
                                                                                            for i in range(8):
                                                                                                x6,y6 = returnCordX(i,x5),returnCordY(i,y5) #[2][4]
                                                                                                test6 = content[x6][y6] # is 1
                                                                                                if not(checkreturn6(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)):
                                                                                                    if(test6 != wall):
                                                                                                        currentturns = 7
                                                                                                        path = "%d %d %d %d %d %d %d %d %d %d %d %d %d %d \n" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
                                                                                                        f.write(path)
                                                                                                        if(result5 + test6 == target and (currentturns >= minimumturns)):
                                                                                                            print "found six path content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d]" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
                                                                                                            turns = 7
                                                                                                            tupleX = getx(x)
                                                                                                            tupleY = gety(y)
                                                                                                            tuple1X =  getx(x1)
                                                                                                            tuple1Y = gety(y1)
                                                                                                            tuple2X =  getx(x2)
                                                                                                            tuple2Y = gety(y2)
                                                                                                            tuple3X =  getx(x3)
                                                                                                            tuple3Y = gety(y3)
                                                                                                            tuple4X =  getx(x4)
                                                                                                            tuple4Y = gety(y4)
                                                                                                            tuple5X = getx(x5)
                                                                                                            tuple5Y = gety(y5)
                                                                                                            tuple6X = getx(x6)
                                                                                                            tuple6Y = gety(y6)
                                                                                                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                                                                                                        else:
                                                                                                            result6 = result5 + test6 # is 4
                                                                                                            for i in range(8):
                                                                                                                x7,y7 = returnCordX(i,x6),returnCordY(i,y6) #[2][4]
                                                                                                                test7 = content[x7][y7] # is 1
                                                                                                                if not(checkreturn7(x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)):
                                                                                                                    if(test7 != wall):
                                                                                                                        currentturns = 8
                                                                                                                        path = "%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d \n" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
                                                                                                                        f.write(path)
                                                                                                                        if(result6 + test7 == target and (currentturns >= minimumturns)):
                                                                                                                            print "found seventh path content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d] and content[%d][%d]" % (x,y,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
                                                                                                                            turns = 8
                                                                                                                            tupleX = getx(x)
                                                                                                                            tupleY = gety(y)
                                                                                                                            tuple1X =  getx(x1)
                                                                                                                            tuple1Y = gety(y1)
                                                                                                                            tuple2X =  getx(x2)
                                                                                                                            tuple2Y = gety(y2)
                                                                                                                            tuple3X =  getx(x3)
                                                                                                                            tuple3Y = gety(y3)
                                                                                                                            tuple4X =  getx(x4)
                                                                                                                            tuple4Y = gety(y4)
                                                                                                                            tuple5X = getx(x5)
                                                                                                                            tuple5Y = gety(y5)
                                                                                                                            tuple6X = getx(x6)
                                                                                                                            tuple6Y = gety(y6)
                                                                                                                            tuple7X = getx(x7)
                                                                                                                            tuple7Y = gety(y7)
                                                                                                                            return tupleX,tupleY,tuple1X,tuple1Y,tuple2X,tuple2Y,tuple3X,tuple3Y,tuple4X,tuple4Y,tuple5X,tuple5Y,tuple6X,tuple6Y,tuple7X,tuple7Y,tuple8X,tuple8Y,tuple9X,tuple9Y,tuple10X,tuple10Y,turns
                                                                                                                        
                                                                                                                                                                    
starttime = time.time()                                                                                                                                                                    
findeigthpath(5)
endtime = time.time()
print (endtime-starttime)*1000
np.savetxt('out')