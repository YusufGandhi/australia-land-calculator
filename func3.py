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
	latitudeList = []
	with open (filePath) as f: #iterate through lines of data file
		for line in f:
			tokens = line.split()
			latitudeList.append(float(tokens[0]))
			longitudeList.append(float(tokens[1]))

	# print(len(longitudeList))
	# print(len(latitudeList))
	i = 1
	longitudeDifferenceList = []
	latitudeDifferenceList = []
	while i < len(longitudeList):
		if abs(longitudeList[i] - longitudeList[i-1]) > 0 and abs(latitudeList[i] - latitudeList[i-1]) == 0.0:
			longitudeDifferenceList.append(abs(longitudeList[i] - longitudeList[i-1]))
		# else:
		# 	latitudeDifferenceList.append(abs(latitudeList[i] - latitudeList[i-1]))
		# the the difference of the latitude
		if abs(latitudeList[i] - latitudeList[i-1]) > 0:
			latitudeDifferenceList.append(abs(latitudeList[i] - latitudeList[i-1]))

		i += 1
	averageLongitude = sum(longitudeDifferenceList) / len(longitudeDifferenceList)
	averageLatitude = sum(latitudeDifferenceList) / len(latitudeDifferenceList)

	print(averageLongitude)
	print(averageLatitude)
	# i = 1
	# latitudeDifferenceList = []

	# while

f3('sydney250m.txt')
