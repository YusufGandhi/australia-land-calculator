import math
# def f1(filePath, meanArea, seaHeight):
# #Assumes filePath is correct and other parameters are valid.
#   aboveSea = 0
#   totalLand = 0
#   with open (filePath) as f: #iterate through lines of data file
#     for line in f:
#       tokens = line.split()
#       z = float(tokens[2])
#       if z > seaHeight:
#         aboveSea += meanArea
#       if z > 0:
#         totalLand += meanArea
#   return (round(aboveSea,4), round(aboveSea/totalLand * 100,2))

# def f2(filePath, meanArea, interval):
# 	maxSeaLevel = 0	
# 	with open (filePath) as f: #iterate through lines of data file
# 		for line in f:
# 			tokens = line.split()
# 			z = float(tokens[2])
# 			maxSeaLevel = max(z, maxSeaLevel)
			
# 	# print (maxSeaLevel)
# 	total_area = []
# 	intervalList = []
# 	spacing = maxSeaLevel * interval
# 	for i in range(0, int(1 / interval) + 1):
# 		(area, percent) = f1(filePath, meanArea, i * spacing)
# 		print("at sea level {:+.2f}: {:.1f} km^2 ({:.2f}%)".format(i * spacing, area, percent))
# 		total_area.append(area)
# 		intervalList.append(i * spacing)
	
# 	# plotting the graph
# 	plt.plot(intervalList, total_area)
# 	plt.ylabel('area above water')
# 	plt.xlabel('sea level increase')
# 	plt.show()

def f3(filePath, height = 0):
	longitudeList = []
	latitudeList = [0]
	elevationList = []
	with open (filePath) as f: #iterate through lines of data file
		for line in f:
			tokens = line.split()
			if latitudeList[len(latitudeList)-1] != float(tokens[0]):
				latitudeList.append(float(tokens[0]))
			if len(latitudeList) == 2:
				longitudeList.append(float(tokens[1]))
			elevationList.append(float(tokens[2]))
	latitudeList = latitudeList[1:]
	# print(len(longitudeList))
	# print(len(latitudeList))



	i = 1
	longitudeDifferenceList = []
	latitudeDifferenceList = []

	for i in range(1,len(latitudeList)):
		latitudeDifferenceList.append(abs(latitudeList[i]-latitudeList[i-1]))
	averageLatitude = sum(latitudeDifferenceList) / len(latitudeDifferenceList)
	
	
	for i in range(1,len(longitudeList)):
		longitudeDifferenceList.append(abs(longitudeList[i]-longitudeList[i-1]))
	averageLongitude = sum(longitudeDifferenceList) / len(longitudeDifferenceList)


	# while i < len(longitudeList):
	# 	if abs(longitudeList[i] - longitudeList[i-1]) > 0 and abs(latitudeList[i] - latitudeList[i-1]) == 0.0:
	# 		longitudeDifferenceList.append(abs(longitudeList[i] - longitudeList[i-1]))
	# 	else:
	# 		latitudeDifferenceList.append(abs(latitudeList[i] - latitudeList[i-1]))
	# 	# the the difference of the latitude
	# 	# if abs(latitudeList[i] - latitudeList[i-1]) > 0:
	# 	# 	latitudeDifferenceList.append(abs(latitudeList[i] - latitudeList[i-1]))

	# 	i += 1
	# averageLongitude = sum(longitudeDifferenceList) / len(longitudeDifferenceList)
	# averageLatitude = sum(latitudeDifferenceList) / len(latitudeDifferenceList)

	verticalSpacing = averageLatitude * 40007/360
	horizontalSpacingList = []
	for lat in latitudeList:
		horizontalSpacingList.append(40075/360 * abs(math.cos(math.radians(lat))) * averageLongitude)
	averageHorizontalSpacing = sum(horizontalSpacingList) / len(horizontalSpacingList)

	
	aboveSea1 = 0
	totalLand1 = 0
	
	aboveSea2 = 0
	totalLand2 = 0
	for i in range(0,len(latitudeList)):
		for j in range(0,len(longitudeList)):
			if elevationList[i*len(longitudeList)+j] > 0.0:
				# print '.',
				totalLand1 += verticalSpacing*averageHorizontalSpacing
				totalLand2 += verticalSpacing*horizontalSpacingList[i]
				if elevationList[i*len(longitudeList)+j] > height:
					aboveSea1 += verticalSpacing*averageHorizontalSpacing
					aboveSea2 += verticalSpacing*horizontalSpacingList[i]
			# else:
			# 	print ' ',
		# print(' ')

	print("First functionality")
	print("===================")
	print("First Approximation:")
	print("--------------------")
	print("Area above sea level: {:.2f} km^2".format(aboveSea1))
	print("Percent area above sea level: {:.2f}%".format(aboveSea1/totalLand1*100))
	print("\nSecond Approximation")
	print("--------------------")
	print("Area above sea level: {:.2f} km^2".format(aboveSea2))
	print("Percent area above sea level: {:.2f}%".format(aboveSea2/totalLand2*100))

	# print(aboveSea)
	# print(totalLand)
	# print(aboveSea/totalLand*100)
	# while

f3('sydney250m.txt', 2)
