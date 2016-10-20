from func1 import f1
import matplotlib.pyplot as plt

def f2(filePath, meanArea, interval):
	maxSeaLevel = 0	
	f = open(filePath,'r') #iterate through lines of data file
	for line in f:
		tokens = line.split()
		z = float(tokens[2])
		# checking if the current level is greater the current maximum
		maxSeaLevel = max(z, maxSeaLevel)
	
	f.close()		
	
	# the main program to loop through the intervals
	total_area = []
	intervalList = []
	spacing = maxSeaLevel * interval 
	for i in range(0, int(1 / interval) + 1):
		# calculating the area below the designated interval
		(area, percent) = f1(filePath, meanArea, i * spacing)
		# printing the output 
		print("at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(i * spacing, area, percent))
		
		# preparing the data for plotting 
		total_area.append(area)
		intervalList.append(i * spacing)
	
	# plotting the graph
	plt.plot(intervalList, total_area)
	plt.ylabel('area above water')
	plt.xlabel('sea level increase')
	plt.show()
	
