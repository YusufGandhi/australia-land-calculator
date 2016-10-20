import math
import matplotlib.pyplot as plt

#Takes in a filePath and extracts data into the 3 lists passed to the function.
#longitudeList and latitudeList contain only one instance of each longitude and latitude.
#Function assumes the data is listed in rows.
def extract(filePath, longitudeList, latitudeList, elevationList):
	latitudeList.append(0) #Needed as previous element in latitude list is needed for comparison
	with open (filePath) as f: #iterate through lines of data file
		for line in f:
			tokens = line.split()
			if latitudeList[len(latitudeList)-1] != float(tokens[0]):
				latitudeList.append(float(tokens[0]))
			if len(latitudeList) == 2:
				longitudeList.append(float(tokens[1]))
			elevationList.append(float(tokens[2]))
	del latitudeList[0]

#Find the average diference between data points in degrees.
def getAverageDif(List):
	DifferenceList = []
	for i in range(1,len(List)):
		DifferenceList.append(abs(List[i]-List[i-1]))
	averageDif = sum(DifferenceList) / len(DifferenceList)
	return averageDif

#Adds the node (i,j) to a set which contains the neighbours of (i,j) or else
# adds that node to a new set if it has no neighbours in any sets.
#Only consideres the left neighbour and the upper 3 neighbours.
#This function is used for counting islands. Which is done by treating each data
# point as a node (i,j), and creating sets of nodes where each node in the set has
# at least one acjacent neighbour also in the set. Once completed a set contains
# all the nodes that are next to each other, i.e. all the nodes in a single landmass.
#The number of sets will be the number of islands.
#Function takes (i,j) and adds it to a set in a list of sets SetList.
def addNodeToSet(SetList, i,j ):
	#Counting Island Stuff
	FoundSets = [] #All sets that has a node adjacent to (i,j)
	if i != 0 and j != 0: # Non-Edge Case, node has 4 possible neighbours.
		for l in range(0,len(SetList)):
			if ( (i,j-1) in SetList[l] ) or ( (i-1,j-1) in SetList[l] ) or ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
				FoundSets.append(l)
		if len(FoundSets) == 0: # No node adjacent to (i,j), create new set.
			s = {(i,j)}
			SetList.append(s)
		elif len(FoundSets) == 1: # One set has node(s) adjacent to (i,j), add (i,j) to that set.
			SetList[FoundSets[0]].add((i,j))
		elif len(FoundSets) == 2:
			s = SetList[FoundSets[0]].union(SetList[FoundSets[1]]) # Two sets have node(s)
			if FoundSets[0] < FoundSets[1]:               # adjacent to (i,j). (i,j) is a merger node,
				del SetList[FoundSets[1]]                   # union both sets and add (i,j).
				del SetList[FoundSets[0]]
			elif FoundSets[0] > FoundSets[1]:
				del SetList[FoundSets[0]]
				del SetList[FoundSets[1]]
			s.add((i,j))
			SetList.append(s)
		elif len(FoundSets) > 2: # Physically impossible given only the 4 nodes we are considering.
			print("IMPOSSIBLE, SOMETHING BROKE")
	elif i == 0 and j != 0: # Edge case, top edge. (consider only left neighbour)
		for l in range(0,len(SetList)):
			if ( (i,j-1) in SetList[l] ):
				FoundSets.append(l)
		if len(FoundSets) == 0:
			s = {(i,j)}
			SetList.append(s)
		elif len(FoundSets) == 1:
			SetList[FoundSets[0]].add((i,j))
	elif i != 0 and j == 0: # Edge case, left edge. (consider only above and above right neighbour)
		for l in range(0,len(SetList)):
			if ( (i-1,j) in SetList[l] ) or ( (i-1,j+1) in SetList[l] ):
				FoundSets.append(l)
		if len(FoundSets) == 0:
			s = {(i,j)}
			SetList.append(s)
		elif len(FoundSets) == 1:
			SetList[FoundSets[0]].add((i,j))
	elif i == 0 and j == 0: # Edge case, top left corner node.
		SetList.append({(i,j)})	
	

#Returns aproximation 1 and 2 result and number of islands.
#Takes in the length of latitude and longitude list (dimension of data grid),
# meanArea for approximation 1, latBasedAreaList for approximation 2 and the new sea level height.
def landAboveSea(lenLatitudeList, lenLongitudeList, elevationList, meanArea, latBasedAreaList, height):
	aboveSea1 = 0
	totalLand1 = 0
	aboveSea2 = 0
	totalLand2 = 0
	SetList = []
	for i in range(0,lenLatitudeList): # (i,j) are co-ordinates of data points.
		for j in range(0,lenLongitudeList):
			if elevationList[i*lenLongitudeList+j] > 0.0:
				totalLand1 += meanArea
				totalLand2 += latBasedAreaList[i]
				if elevationList[i*lenLongitudeList+j] > height:
					aboveSea1 += meanArea
					aboveSea2 += latBasedAreaList[i]
					
					addNodeToSet(SetList, i,j)
		
	
	nrIslands = len(SetList)
	return (round(aboveSea1,4), round(aboveSea1/totalLand1 * 100,2), round(aboveSea2,4), round(aboveSea2/totalLand2 * 100,2), nrIslands)

def f4(filePath, height = -1, interval = 0.01):
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
		(fa1area, fa1percent, fa2area, fa2percent, nrIslands) = landAboveSea( \
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
	elif height == -1: #no height specified so to set of heights.
		#Find highest sea level
		maxSeaLevel = 0	
		for el in elevationList:
			maxSeaLevel = max(el, maxSeaLevel)
				

		total_area1 = [] #Record for plotting graphs.
		total_area2 = []
		intervalList = []
		spacing = maxSeaLevel * interval
		for k in range(0, int(1 / interval) + 1): # Iterate for each sea level height.
			(fa1area, fa1percent, fa2area, fa2percent, nrIslands) = landAboveSea( \
			len(latitudeList), len(longitudeList), elevationList, meanArea, \
			latBasedAreaList, k * spacing)

			print("Approximation 1: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, fa1area, fa1percent))
			print("Approximation 2: at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(k * spacing, fa2area, fa2percent))
			print("At sea level {:+.2f} there are {} islands".format(k * spacing, nrIslands))
			total_area1.append(fa1area)
			total_area2.append(fa2area)
			intervalList.append(k * spacing)
	
		# plotting the graph
		# plt.figure(1)
		plt.subplot(121)
		plt.plot(intervalList, total_area1)
		plt.title('Approximation 1')
		plt.ylabel('area above water')
		plt.xlabel('sea level increase')

		# plt.figure(2)
		plt.subplot(122)
		plt.plot(intervalList, total_area2)
		plt.title('Approximation 2')
		plt.ylabel('area above water')
		plt.xlabel('sea level increase')

		plt.show()

