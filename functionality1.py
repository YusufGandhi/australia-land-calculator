import sys
from pathlib import Path

def f1(filePath, meanArea, seaHeight):
#Assumes filePath is correct and other parameters are valid.
  aboveSea = 0
  totalLand = 0
  with open (filePath) as f: #iterate through lines of data file
    for line in f:
      tokens = line.split()
      z = float(tokens[2])
      if z > seaHeight:
        aboveSea += meanArea
      if z > 0:
        totalLand += meanArea
  return (round(aboveSea,4), round(aboveSea/totalLand * 100,2))


print(sys.argv[1])

if(len(sys.argv) < 5):
  print("Not enough parameters. Review README file")
  #print out what parameters the user needs to input.
else: #Do rest of program
  datFile = Path(sys.argv[1])
  mvertical = float(sys.argv[2])
  mhorizontal = float(sys.argv[3])
  seaHeight = float(sys.argv[4])
  if datFile.is_file() and (mvertical > 0) and (mhorizontal > 0) and (seaHeight > 0):
    (area, percent) = f1(sys.argv[1], mvertical*mhorizontal, seaHeight)
    print("Area above sea level:", area, "km^2")
    print("Percent area above sea level:", percent, "%")
  else:
    print("ERROR some parameters not valid, more useful error message coming in later version")
#read in user parameters: datafile path, mean spacing, sea level height.
#read in data file
#check data file validity
#check parameters given by user is valid.
#pass parameters to f1
