def f1(filePath, meanArea, seaHeight):
#Assumes filePath is correct and other parameters are valid.
  aboveSea = 0   # to store the the total area above the seaHeight parameter
  totalLand = 0  # to store the the total area above sea level (0.0)
  
  f = open(filePath,'r')
  for line in f:
    tokens = line.split()
    z = float(tokens[2])
    
    # adding up the above sea level height area
    if z > seaHeight:
      aboveSea += meanArea
    
    # adding up the area above 0.0 metre sea level
    if z > 0:
      totalLand += meanArea
  f.close()
  return (round(aboveSea,4), round(aboveSea/totalLand * 100,2))