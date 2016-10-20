import sys
# from pathlib import Path

def f1(filePath, meanArea, seaHeight):
#Assumes filePath is correct and other parameters are valid.
  aboveSea = 0
  totalLand = 0
  f = open(filePath,'r')
  # with open (filePath) as f: #iterate through lines of data file
  for line in f:
    tokens = line.split()
    z = float(tokens[2])
    if z > seaHeight:
      aboveSea += meanArea
    if z > 0:
      totalLand += meanArea
  f.close()
  return (round(aboveSea,4), round(aboveSea/totalLand * 100,2))
