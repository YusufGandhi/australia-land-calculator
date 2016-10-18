from functionality1 import f1
#from pathlib import Path
import matplotlib.pyplot as plt


def f2(filePath, meanArea, interval):
	maxSeaLevel = 0	
	with open (filePath) as f: #iterate through lines of data file
		for line in f:
			tokens = line.split()
			z = float(tokens[2])
			maxSeaLevel = max(z, maxSeaLevel)
			
	# print (maxSeaLevel)
	total_area = []
	intervalList = []
	spacing = maxSeaLevel * interval
	for i in range(0, int(1 / interval) + 1):
		(area, percent) = f1(filePath, meanArea, i * spacing)
		print("at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(i * spacing, area, percent))
		total_area.append(area)
		intervalList.append(i * spacing)
	
	# plotting the graph
	plt.plot(intervalList, total_area)
	plt.ylabel('area above water')
	plt.xlabel('sea level increase')
	plt.show()
	# return (total_area, intervalList)



# if(len(sys.argv) < 4):
#  print("Not enough parameters. Review README file")
#  #print out what parameters the user needs to input.
# else: #Do rest of program
#  datFile = Path(sys.argv[1])
#  mvertical = float(sys.argv[2])
#  mhorizontal = float(sys.argv[3])
#  # seaHeight = float(sys.argv[4])
#  if datFile.is_file() and (mvertical > 0) and (mhorizontal > 0):
#    (area, percent) = f2(sys.argv[1], mvertical*mhorizontal, 0.01)
#    print("Area above sea level:", area, "km^2")
#    print("Percent area above sea level:", percent, "%")
#  else:
#    print("ERROR some parameters not valid, more useful error message coming in later version")
