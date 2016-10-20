import math
import matplotlib.pyplot as plt

#global variable for togling images
ind = 0

#Takes in a filePath and extracts data into the 3 lists passed to the function.
def extract(filePath, longitudeList, latitudeList, elevationList):
	latitudeList.append(0)
	with open (filePath) as f: #iterate through lines of data file
		for line in f:
			tokens = line.split()
			if latitudeList[len(latitudeList)-1] != float(tokens[0]):
				latitudeList.append(float(tokens[0]))
			if len(latitudeList) == 2:
				longitudeList.append(float(tokens[1]))
			elevationList.append(float(tokens[2]))
	del latitudeList[0]

def getAverageDif(List):
	DifferenceList = []
	for i in range(1,len(List)):
		DifferenceList.append(abs(List[i]-List[i-1]))
	averageDif = sum(DifferenceList) / len(DifferenceList)
	return averageDif

def addNodeToSet(SetList, i,j ):
	#Counting Island Stuff
	FoundSets = []
	if i != 0 and j != 0:
		for l in range(0,len(SetList)):
			if ( (i,j-1) in SetList[l] ) or ( (i-1,j-1) in SetList[l] ) or ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
				FoundSets.append(l)
		if len(FoundSets) == 0:
			s = {(i,j)}
			SetList.append(s)
		elif len(FoundSets) == 1:
			SetList[FoundSets[0]].add((i,j))
		elif len(FoundSets) == 2:
			s = SetList[FoundSets[0]].union(SetList[FoundSets[1]])
			if FoundSets[0] < FoundSets[1]:
				del SetList[FoundSets[1]]
				del SetList[FoundSets[0]]
			elif FoundSets[0] > FoundSets[1]:
				del SetList[FoundSets[0]]
				del SetList[FoundSets[1]]
			s.add((i,j))
			SetList.append(s)
		elif len(FoundSets) > 2:
			print("IMPOSSIBLE, YOU JUST BROKE LOGIC")
	elif i == 0 and j != 0:
		for l in range(0,len(SetList)):
			if ( (i,j-1) in SetList[l] ):
				FoundSets.append(l)
		if len(FoundSets) == 0:
			s = {(i,j)}
			SetList.append(s)
		elif len(FoundSets) == 1:
			SetList[FoundSets[0]].add((i,j))
	elif i != 0 and j == 0:
		for l in range(0,len(SetList)):
			if ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
				FoundSets.append(l)
		if len(FoundSets) == 0:
			s = {(i,j)}
			SetList.append(s)
		elif len(FoundSets) == 1:
			SetList[FoundSets[0]].add((i,j))
	elif i == 0 and j == 0:
		SetList.append({(i,j)})
	#END SET COUNTING		
	

#Returns aproximation 1 and 2 result and number of islands.
def landAboveSea(lenLatitudeList, lenLongitudeList, elevationList, meanArea, latBasedAreaList, height):
	aboveSea1 = 0
	totalLand1 = 0
	aboveSea2 = 0
	totalLand2 = 0
	SetList = []
	picture = []
	for i in range(0,lenLatitudeList):
		row = []
		for j in range(0,lenLongitudeList):
			if elevationList[i*lenLongitudeList+j] > 0.0:
				totalLand1 += meanArea
				totalLand2 += latBasedAreaList[i]
				if elevationList[i*lenLongitudeList+j] > height:
					aboveSea1 += meanArea
					aboveSea2 += latBasedAreaList[i]
					
					addNodeToSet(SetList, i,j)
					
					row.append(1)
				else:
					row.append(0)
			else:
				row.append(0)
		picture.append(row)
	
	nrIslands = len(SetList)
	return (round(aboveSea1,4), round(aboveSea1/totalLand1 * 100,2), round(aboveSea2,4), round(aboveSea2/totalLand2 * 100,2), nrIslands, picture)

def f4i(filePath, height = -1, interval = 0.01):
	#Extract data from file.
	longitudeList = [] #List of all longitudes
	latitudeList = [] #List of all latitudes
	elevationList = [] #List of all elevations
	extract(filePath, longitudeList, latitudeList, elevationList)
	
	#Find the spacing between latitudes and longitudes in degrees.
	averageLatitudeDif = getAverageDif(latitudeList)
	averageLongitudeDif = getAverageDif(longitudeList)
	
	#Find the spacing between data points in km.
	verticalSpacing = averageLatitudeDif * 40007/360
	horizontalSpacingList = []
	for lat in latitudeList:
		horizontalSpacingList.append(40075/360 * abs(math.cos(math.radians(lat))) * averageLongitudeDif)
	averageHorizontalSpacing = sum(horizontalSpacingList) / len(horizontalSpacingList)

	#Find average area and area dependent on latitude
	meanArea = verticalSpacing*averageHorizontalSpacing
	latBasedAreaList = []
	for l in horizontalSpacingList:
		latBasedAreaList.append(l*verticalSpacing)

	if height >= 0: #User has specified a height so do just do 1 calc.
		(fa1area, fa1percent, fa2area, fa2percent, nrIslands, picture) = landAboveSea( \
			len(latitudeList), len(longitudeList), elevationList, meanArea, \
			latBasedAreaList, height)
		
		print("First functionality")
		print("===================")
		print("First Approximation:")
		print("--------------------")
		print("Area above sea level: {:.2f} km^2".format(fa1area))
		print("Percent area above sea level: {:.2f}%".format(fa2percent))
		print("\nSecond Approximation")
		print("--------------------")
		print("Area above sea level: {:.2f} km^2".format(fa2area))
		print("Percent area above sea level: {:.2f}%".format(fa2percent))
		print("--------------------")
		print("Number of disjoint land masses (Islands): {:}".format(nrIslands))
		
		plt.imshow(picture, extent=(0,len(picture[0]),0,len(picture)))
		plt.show()	
		
		
	elif height == -1:
		#Find highest sea level
		maxSeaLevel = 0	
		for el in elevationList:
			maxSeaLevel = max(el, maxSeaLevel)
				
		
		allpictures = []
		
		total_area1 = []
		total_area2 = []
		intervalList = []
		spacing = maxSeaLevel * interval
		for k in range(0, int(1 / interval) + 1):
			(fa1area, fa1percent, fa2area, fa2percent, nrIslands, picture) = landAboveSea( \
			len(latitudeList), len(longitudeList), elevationList, meanArea, \
			latBasedAreaList, k * spacing)

			print("Approximation 1: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, fa1area, fa1percent))
			print("Approximation 2: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, fa2area, fa2percent))
			print("At sea level {:+.2f} there are {} islands".format(k * spacing, nrIslands))
			total_area1.append(fa1area)
			total_area2.append(fa2area)
			intervalList.append(k * spacing)
			
			allpictures.append(picture)
		
		
		import numpy as np
		
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.imshow(allpictures[0], extent=(0,len(allpictures[0][0]),0,len(allpictures[0])))
		#ind = 0
		def onclick(event):
			global ind
			ind += 1
			if ind > int(1/interval):
				ind = 0
			ax.clear()
			ax.imshow(allpictures[ind], extent=(0,len(allpictures[ind][0]),0,len(allpictures[ind])))
			plt.draw()

		cid = fig.canvas.mpl_connect('button_press_event', onclick)
	
		# plotting the graph
		# plt.figure(1)
		#plt.subplot(121)
		#plt.plot(intervalList, total_area1)
		#plt.title('Approximation 1')
		#plt.ylabel('area above water')
		#plt.xlabel('sea level increase')

		# plt.figure(2)
		#plt.subplot(122)
		#plt.plot(intervalList, total_area2)
		#plt.title('Approximation 2')
		#plt.ylabel('area above water')
		#plt.xlabel('sea level increase')

		plt.show()

