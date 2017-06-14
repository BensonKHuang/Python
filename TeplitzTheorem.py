'''
Created on Jun 13, 2017

@author: Benson Huang & Harrison Teplitz
(A+t/B+t) = C/D, find t
'''
print("Teplitz Theorem: initial ratio and desired ratio")

while True: #numerator A
    try:
        numCurrent = float((input("current initial owned (e.g. 1) : ")))
    except ValueError:
        print("invalid input")
        continue
    if(numCurrent >= 0):
        break
    else:
        print("invalid input")
while True: #denominator B
    try:
        numCurrentTotal = float((input("current initial total (e.g. 5) : ")))
    except ValueError:
        print("invalid input")
        continue
    if (numCurrentTotal > numCurrent):
        break
    else:
        print("invalid input")
numRatio = (numCurrent/numCurrentTotal)
print ("initial ratio = " + str(numRatio))
while True: #C/D ratio
    try:
        numDesired = float((input("desired final ratio (e.g. 0.5) : ")))
    except ValueError:
        print("invalid input")
        continue
    if(numDesired > numRatio and numDesired < 1):
        break
    else:   
        print("invalid input")
desiredDen = float(1/numDesired)    #find reciprocal D/1    
finalIncr = ((numCurrentTotal - (desiredDen*numCurrent)) / ((desiredDen) - 1)) 
testFinal = round(finalIncr, 2)
if finalIncr > (testFinal - 0.000000001) and testFinal >= finalIncr: #tests for rounding error
    print("For desired ratio " + str(numDesired) + ", increase owned by " + str(testFinal))  
else:
    print("For desired ratio " + str(numDesired) + ", increase owned by " + str(finalIncr))
    
    